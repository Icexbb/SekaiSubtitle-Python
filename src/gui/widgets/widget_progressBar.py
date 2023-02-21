import os.path

from PySide6 import QtWidgets, QtCore

from gui.thread_process_new import VideoProcessThread
from gui.widgets.qt_taskProgressBar import Ui_ProgressBarWidget


class ProgressBar(QtWidgets.QWidget, Ui_ProgressBarWidget):
    signal = QtCore.Signal(dict)

    def __init__(self, parent, data):
        super().__init__()
        self.id = f"{hash(self)}"
        self.processing = False
        self.setupUi(self)
        self.parent = parent
        self.ProgressBar.setMaximum(0)
        self.StartButton.clicked.connect(self.toggle_process)
        self.DeleteButton.clicked.connect(self.delete_process)

        self.taskInfo = data
        self.video = self.taskInfo.get("video")
        self.json = self.taskInfo.get("json")
        self.translate = self.taskInfo.get("translate")
        self.Thread: VideoProcessThread = None

        self.TaskNameString = os.path.splitext(os.path.split(self.video)[-1])[0]
        self.TaskName.setText(self.TaskNameString)
        self.TaskName.repaint()
        self.timer = QtCore.QTimer(self)
        # self.timer.timeout.connect(self.update_content)
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
            self.Thread = VideoProcessThread(self, self.video, self.json, self.translate)
            self.Thread.signal_data.connect(self.signal_process)
            self.processing = True
            self.StartButton.setStyleSheet("background-color:rgb(255,255,100);")
            # self.StatusLog.setText("")
            self.StatusLogList.clear()

            self.Thread.start()
        else:
            self.Thread.signal_data.emit({"type": "stop", "data": None})
            self.signal_process({"type": int, "data": 0})
            self.signal_process({"type": bool, "data": False})
            self.StartButton.setStyleSheet(None)
            self.Thread.terminate()
            self.Thread = None

            # self.StatusLog.setText("")

    def delete_process(self):
        if self.processing:
            self.Thread.terminate()

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
            elif data == 1:
                self.processing = True
                self.TaskStatus.setText("处理中")
            elif data == 2:
                self.processing = False
                self.TaskStatus.setText("已完成")
            elif data == 3:
                self.processing = False
                self.TaskStatus.setText("队列中")
            elif data == 4:
                self.processing = False
                self.TaskStatus.setText("错误")
        elif msg['type'] == bool:
            if msg['data']:
                self.ProgressBar.setMaximum(1)
                self.ProgressBar.setValue(1)
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

        self.ProgressBar.repaint()
        self.TaskStatus.repaint()