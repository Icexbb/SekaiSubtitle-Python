import os
from queue import Queue

from PySide6 import QtWidgets, QtGui, QtCore

from gui.design.WidgetSubtitleProcess import Ui_ProcessWidget
from gui.design.WidgetSubtitleTaskAccept import Ui_AccWidget
from gui.widgets.dialog_makeTaskDialog import NewTaskDialog
from gui.widgets.widget_progressBar import ProgressBar


class NewDialogThread(QtCore.QThread):
    def __init__(self, queue, signal):
        super().__init__()
        self.queue: Queue = queue
        self.signal: QtCore.Signal = signal

    def run(self) -> None:
        while True:
            path = self.queue.get()
            if path:
                self.signal.emit(path)


class TaskAcceptWidget(QtWidgets.QWidget, Ui_AccWidget):
    signal = QtCore.Signal(str)

    def __init__(self, parent):
        super().__init__()
        self.newPath = None
        self.setupUi(self)
        self.setAcceptDrops(True)
        self.parent = parent
        self.queue = Queue()
        self.NewDialogThread = NewDialogThread(self.queue, self.signal)
        self.NewDialogThread.start()

    def dragEnterEvent(self, event: QtGui.QDragEnterEvent) -> None:
        path = event.mimeData().text()
        if path.endswith((".mp4", ".mkv", ".wmv", ".avi", ".json", ".asset", ".txt", ".yml")):
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event: QtGui.QDropEvent):
        path = event.mimeData().text().removeprefix('file:///')
        if path.endswith((".mp4", ".mkv", ".wmv", ".avi", ".json", ".asset", ".txt", ".yml")):
            self.queue.put(path)

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            self.signal.emit("")


class ListWidgetItem(QtWidgets.QListWidgetItem):
    def __init__(self):
        super().__init__()
        self.id = None


class ProcessWidget(QtWidgets.QWidget, Ui_ProcessWidget):
    def __init__(self, parent):
        super().__init__()
        from gui.gui_main import MainUi
        self.parent: MainUi = parent
        self.setupUi(self)
        self.setAcceptDrops(True)
        self.tempAcceptFile = None
        self.TaskAcceptWidget = TaskAcceptWidget(self)
        self.TaskAcceptWidget.signal.connect(self.NewTaskDialog)
        self.horizontalLayout.addWidget(self.TaskAcceptWidget)

        self.StopAllButton.clicked.connect(self.stop_all)
        self.StartAllButton.clicked.connect(self.start_all)
        self.ClearAllButton.clicked.connect(self.clear_all)

        self.bars = []

    @property
    def font(self):
        return self.parent.font

    @property
    def start_immediate(self):
        return self.parent.immediate_start

    def NewTaskDialog(self, path: str):
        dialog = NewTaskDialog(self.parent)
        dialog.signal.connect(self.ProcessSignal)

        if path and os.path.exists(path):
            if path.lower().endswith((".mp4", ".mkv", ".wmv", ".avi",)):
                dialog.VideoSelector.FileLabel.setText(path)
                dialog.VideoSelector.fileSelected = path
            elif path.lower().endswith((".json", ".asset")):
                dialog.JsonSelector.FileLabel.setText(path)
                dialog.JsonSelector.fileSelected = path
            elif path.lower().endswith((".txt", ".yml")):
                dialog.TranslateSelector.FileLabel.setText(path)
                dialog.TranslateSelector.fileSelected = path
        dialog.show()
        dialog.exec()

    def ProcessSignal(self, data: dict):
        bar = ProgressBar(self, data)
        item = ListWidgetItem()
        item.id = bar.id
        item.setSizeHint(bar.size())
        self.ProcessingListWidget.addItem(item)
        self.ProcessingListWidget.setItemWidget(item, bar)
        self.bars.append(bar)
        if self.start_immediate:
            bar.toggle_process()

    def ProcessSignalFromChild(self, data):
        child_id = data.get("id")
        child_data = data.get("data")

        count = self.ProcessingListWidget.count()
        for i in range(count):
            item = self.ProcessingListWidget.item(i)
            if item and item.id == child_id:
                if isinstance(child_data, int):
                    self.ProcessingListWidget.removeItemWidget(self.ProcessingListWidget.takeItem(i))
                else:
                    self.ProcessingListWidget.item(i).setSizeHint(child_data)
        for bar in self.bars:
            if bar.id == child_id:
                if child_data == 0:
                    self.bars.remove(bar)
                # else:
                # self.setFixedHeight(child_data)
                # bar.setFixedSize(child_data)

    def resizeEvent(self, event: QtGui.QResizeEvent) -> None:
        count = self.ProcessingListWidget.count()
        width = self.ProcessingListWidget.size().width()
        for i in range(count):
            item: ListWidgetItem = self.ProcessingListWidget.item(i)
            for bar in self.bars:
                if bar.id == item.id:
                    height = bar.size().height()
                    size = QtCore.QSize(width, height)
                    item.setSizeHint(size)
                    bar.resize(size)

    def start_all(self):
        for bar in self.bars:
            if not bar.processing:
                bar.toggle_process()

    def stop_all(self):
        for bar in self.bars:
            if bar.processing:
                bar.toggle_process()

    def clear_all(self):
        self.stop_all()
        count = self.ProcessingListWidget.count()
        while count:
            self.ProcessingListWidget.removeItemWidget(self.ProcessingListWidget.takeItem(0))
            count = self.ProcessingListWidget.count()
        self.bars.clear()
