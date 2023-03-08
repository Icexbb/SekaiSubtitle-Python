import os.path

from PySide6 import QtWidgets, QtCore

from gui.design.WidgetProcessBar import Ui_ProgressBarWidget
from gui.thread_process import VideoProcessThread


class ProgressBar(QtWidgets.QWidget, Ui_ProgressBarWidget):
    signal = QtCore.Signal(dict)

    def __init__(self, parent, data):
        super().__init__()
        self.id = f"{hash(self)}"
        self.processing = False
        self.setupUi(self)
        from gui.widgets.widget_subtitle import ProcessWidget
        self.parent: ProcessWidget = parent
        self.ProgressBar.setMaximum(0)
        self.StartButton.clicked.connect(self.toggle_process)
        self.DeleteButton.clicked.connect(self.delete_process)

        self.taskInfo: dict = data
        self.video = self.taskInfo.get("video")
        self.font = self.taskInfo.get("font")

        if self.taskInfo.get("dryrun"):
            self.dryrun = True
        else:
            self.dryrun = False
        self.json = self.taskInfo.get("json")
        self.translate = self.taskInfo.get("translate")
        self.Thread: VideoProcessThread = None
        self.staff = self.taskInfo.get("staff")

        self.TaskNameString = os.path.splitext(os.path.split(self.video)[-1])[0]
        self.TaskName.setText(self.TaskNameString)
        self.TaskName.repaint()
        self.timer = QtCore.QTimer(self)
        self.signal.connect(self.parent.ProcessSignalFromChild)
        self.LogShowButton.clicked.connect(self.showLog)
        self.logShowing = False
        self.setFixedHeight(100)

    def showLog(self):
        self.logShowing = not self.logShowing
        if self.logShowing:
            self.setFixedHeight(200)
            self.LogShowButton.setText("∧")
        else:
            self.setFixedHeight(100)
            self.LogShowButton.setText("<")
        self.signal.emit({"id": self.id, 'data': self.size()})

    def toggle_process(self):
        if not self.processing:
            self.Thread = VideoProcessThread(self, self.video, self.json, self.translate, self.font, self.dryrun,
                                             self.staff)
            self.Thread.signal_data.connect(self.signal_process)
            self.StartButton.setStyleSheet("background-color:rgb(255,255,100);")
            self.StatusLogList.clear()
            self.Thread.start()
            self.processing = True
        else:
            self.pause_process()

    def pause_process(self):
        self.Thread.signal_stop.emit(True)
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
            pass
            # self.StatusLog.setText(msg['data'])
            new_item = QtWidgets.QListWidgetItem()
            new_item.setText(msg['data'])
            self.StatusLogList.addItem(new_item)
            self.StatusLogList.scrollToItem(new_item)
            # self.strings.append(msg['data'] + "\n")
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
                time_spend = data.get("time")
                percent = self.ProgressBar.value() / (self.ProgressBar.maximum() or 1) * 100
                fps = self.ProgressBar.value() / (time_spend or 1)
                eta = (self.ProgressBar.maximum() - self.ProgressBar.value()) / (fps or 1)
                self.PercentLabel.setText(f"FPS: {fps / 2:.1f} ETA: {eta:.1f}s {percent:.1f}%")
                if not self.processing:
                    self.PercentLabel.setText("")

        self.PercentLabel.repaint()
        self.ProgressBar.repaint()
        self.TaskStatus.repaint()
