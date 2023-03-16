import os.path

import numpy as np
import pyqtgraph as pg
from PySide6 import QtWidgets, QtCore

from gui.design.WidgetProcessBar import Ui_ProgressBarWidget
from gui.thread_process import VideoProcessThread


class ProgressBar(QtWidgets.QWidget, Ui_ProgressBarWidget):
    signal = QtCore.Signal(dict)

    def __init__(self, parent, data):
        super().__init__()
        self.GraphWidget = None
        self.id = f"{hash(self)}"
        self.processing = False
        self.setupUi(self)
        from gui.widgets.widget_subtitle import ProcessWidget
        self.parent: ProcessWidget = parent
        self.ProgressBar.setMaximum(0)
        self.StartButton.clicked.connect(self.toggle_process)
        self.DeleteButton.clicked.connect(self.delete_process)
        self.taskInfo: dict = data
        self.Thread: VideoProcessThread = None
        self.process_data = {
            "video": self.taskInfo.get("video"),
            "json": self.taskInfo.get("json"),
            "translate": self.taskInfo.get("translate"),
            "overwrite": True,
            "font": self.taskInfo.get("font"),
            "dryrun": bool(self.taskInfo.get("dryrun")),
            "staff": self.taskInfo.get("staff"),
            "typer_interval": self.parent.parent.typer_interval,
            "duration": self.taskInfo.get("duration"),
        }

        self.TaskNameString = os.path.splitext(os.path.split(self.process_data.get("video"))[-1])[0]
        self.TaskName.setText(self.TaskNameString)
        self.TaskName.repaint()
        self.timer = QtCore.QTimer(self)
        self.signal.connect(self.parent.ProcessSignalFromChild)
        self.LogShowButton.clicked.connect(self.showLog)
        self.logShowing = True
        self.time_frame_array = []
        self.fps_list = []
        self.setupPlot()
        self.showLog()

    def setupPlot(self):
        self.GraphWidget = pg.PlotWidget(self)
        self.GraphWidget.setBackground('w')
        self.GraphWidget.enableMouse(False)
        self.GraphWidget.mousePressEvent = lambda ev: None
        self.GraphWidget.mouseMoveEvent = lambda ev: None
        self.GraphWidget.mouseReleaseEvent = lambda ev: None
        self.GraphLayout.addWidget(self.GraphWidget)

    def updatePlot(self, limit: int = 0):
        self.GraphWidget.clear()
        if limit:
            values = self.fps_list[-max(limit, 1):]
            values_2 = self.fps_list[-max(limit * 2, 1):]
            self.GraphWidget.setYRange(max(0, min(values_2) - 20), max(values_2) + 20)
            x = np.linspace(max(1, len(self.fps_list) - len(values)), len(self.fps_list) + 1, len(values) + 1)

        else:
            values = self.fps_list[1:]
            self.GraphWidget.setYRange(max(0, min(values) - 20), max(values) + 20)
            x = np.linspace(0, len(self.fps_list), len(values) + 1)

        pen = pg.mkPen(width=1, color='b')
        self.GraphWidget.plot(x, values, stepMode="center", pen=pen)

    def showLog(self):
        self.logShowing = not self.logShowing
        if self.logShowing:
            self.setFixedHeight(200)
            self.LogShowButton.setText("∧")
            self.GraphWidget.setHidden(False)
        else:
            self.setFixedHeight(100)
            self.LogShowButton.setText("<")
            self.GraphWidget.setHidden(True)
        self.signal.emit({"id": self.id, 'data': self.size()})

    def toggle_process(self):
        if not self.processing:
            self.Thread = VideoProcessThread(self, self.process_data)
            self.Thread.signal_data.connect(self.signal_process)
            self.StartButton.setStyleSheet("background-color:rgb(255,255,100);")
            self.StatusLogList.clear()
            self.fps_list.clear()
            self.time_frame_array.clear()
            self.Thread.start()
            self.processing = True
        else:
            self.pause_process()

    def pause_process(self):
        self.Thread.signal_stop.emit()
        self.Thread.signal_data.emit({"type": "stop", "data": None})
        self.signal_process({"type": int, "data": 0})
        self.signal_process({"type": bool, "data": False})
        self.StartButton.setStyleSheet(None)
        self.PercentLabel.setText("")
        self.processing = False

    def delete_process(self):
        try:
            self.pause_process()
        except:
            pass
        self.signal.emit({"id": self.id, 'data': 0})

    def signal_process(self, msg):
        if msg['type'] == str:
            new_item = QtWidgets.QListWidgetItem()
            new_item.setText(msg['data'])
            self.StatusLogList.addItem(new_item)
            self.StatusLogList.scrollToItem(new_item)
        elif msg['type'] == int:
            data = msg['data']
            if data == 0:
                self.processing = False
                self.TaskStatus.setText("未开始")
                self.ProgressBar.setStyleSheet("")
            elif data == 1:
                self.processing = True
                self.TaskStatus.setText("处理中")
                self.ProgressBar.setStyleSheet("")
            elif data == 2:
                self.processing = False
                self.TaskStatus.setText("已完成")
                self.ProgressBar.setStyleSheet("")
            elif data == 3:
                self.processing = False
                self.TaskStatus.setText("队列中")
                self.ProgressBar.setStyleSheet("QProgressBar::chunk{background-color:#CCCC00;}")
            elif data == 4:
                self.processing = False
                self.TaskStatus.setText("错误")
                self.ProgressBar.setValue(self.ProgressBar.maximum())
                self.ProgressBar.setStyleSheet("QProgressBar::chunk{background-color:#FF0000;}")
        elif msg['type'] == bool:
            if msg['data']:
                self.ProgressBar.setValue(self.ProgressBar.maximum() - 1)
            else:
                self.ProgressBar.setMaximum(0)
                self.ProgressBar.setValue(0)
        elif msg['type'] == "stop":
            pass
        else:
            data = msg['data']
            if s := data.get("total"):
                self.ProgressBar.setMaximum(self.ProgressBar.maximum() + s)
            if data.get("done"):
                self.ProgressBar.setValue(self.ProgressBar.value() + 1)
                percent = self.ProgressBar.value() / (self.ProgressBar.maximum() or 1) * 100

                time_spend = data.get("time")
                self.time_frame_array.append(time_spend)

                compare_frame = max(len(self.time_frame_array) - 10, 0)
                compare_time = time_spend - self.time_frame_array[compare_frame]

                fps = (len(self.time_frame_array) - compare_frame) / (
                        time_spend - self.time_frame_array[compare_frame]) if compare_time else 0
                speed = self.ProgressBar.value() / (time_spend or 1)
                eta = (self.ProgressBar.maximum() - self.ProgressBar.value()) / (speed or 1)
                self.fps_list.append(fps)

                if data.get("end"):
                    self.updatePlot()
                    self.PercentLabel.setText(f"FPS: {speed:.1f} USE: {time_spend:.1f}s {percent:.1f}%")
                else:
                    self.updatePlot(min(1000, int(self.ProgressBar.maximum() / 20)))
                    self.PercentLabel.setText(f"FPS: {fps:.1f} ETA: {eta:.1f}s {percent:.1f}%")
                if not self.processing:
                    self.PercentLabel.setText("")

        self.PercentLabel.repaint()
        self.ProgressBar.repaint()
        self.TaskStatus.repaint()
