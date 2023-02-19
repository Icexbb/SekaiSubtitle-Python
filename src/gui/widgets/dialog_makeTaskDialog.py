import os

from PySide6 import QtCore, QtWidgets, QtGui
from qframelesswindow import FramelessDialog

from gui.widgets.widget_titlebar import TitleBar
from gui.widgets.qt_fileSelect import Ui_SelectWidget as Selector
from gui.widgets.qt_taskMakeDialog import Ui_NewSubProcessDialog as Dialog


class FileSelector(QtWidgets.QWidget, Selector):
    def __init__(self, parent, filetype: str, filetype_list: list):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        self.HintLabel.setText(f"{filetype}文件")
        self.acceptFileTypes = filetype_list
        self.setAcceptDrops(True)
        self.SelectButton.clicked.connect(self.chooseFile)

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        # if self.childAt(event.position().x(), event.position().y()).objectName() == "SelectButton":
        if event.button() == QtCore.Qt.MouseButton.RightButton:
            self.FileLabel.setText("未选择")

    def chooseFile(self):
        file_name_choose, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, "选取文件", dir=os.getcwd(), filter=f"视频文件 ({' '.join(self.acceptFileTypes)});;全部文件 (*)"
        )
        if file_name_choose and os.path.exists(file_name_choose):
            self.FileLabel.setText(file_name_choose)

    @property
    def fileSelected(self):
        filepath = self.FileLabel.text()
        return filepath if os.path.exists(filepath) else None

    def dragEnterEvent(self, event: QtGui.QDragEnterEvent) -> None:
        if event.mimeData().text().endswith(tuple(self.acceptFileTypes)):  # 如果是.srt结尾的路径接受
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event: QtGui.QDropEvent) -> None:
        path = event.mimeData().text().replace('file:///', '')  # 删除多余开头
        if os.path.exists(path):
            self.FileLabel.setText(path)


class NewTaskDialog(FramelessDialog, Dialog):
    signal = QtCore.Signal(dict)

    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("新任务")
        self.setObjectName("New Task")

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.parent = parent

        self.TitleBar = TitleBar(self)

        self.TitleBar.WindowMaxButton.setHidden(True)
        self.TitleBar.WindowMinButton.setHidden(True)
        self.TitleBar.mouseDoubleClickEvent = lambda x: {None}
        self.setTitleBar(self.TitleBar)


        self.VideoSelector = FileSelector(self, "视频", ['*.mp4', '*.avi', '*.wmv', "*.mkv"])
        self.JsonSelector = FileSelector(self, "数据", ['*.json'])
        self.TranslateSelector = FileSelector(self, "翻译", ['*.txt'])
        self.VideoSelector.FileLabel.textChanged.connect(self.fileAutoSelect)

        self.SelectBoxLayout.addWidget(self.VideoSelector)
        self.SelectBoxLayout.addWidget(self.JsonSelector)
        self.SelectBoxLayout.addWidget(self.TranslateSelector)
        self.EmitButton.clicked.connect(self.emitTask)

    def fileAutoSelect(self):
        video_file = self.VideoSelector.fileSelected
        if video_file and os.path.exists(video_file):
            file_prefix = os.path.splitext(video_file)[0]
            predict_json = file_prefix + ".json"
            predict_translate = file_prefix + ".txt"
            if os.path.exists(predict_json):
                self.JsonSelector.FileLabel.setText(predict_json)
            if os.path.exists(predict_translate):
                self.VideoSelector.FileLabel.setText(predict_translate)

    def emitTask(self):
        video_file = self.VideoSelector.fileSelected
        json_file = self.JsonSelector.fileSelected
        translate_file = self.TranslateSelector.fileSelected
        data = {"video": video_file, "json": json_file, "translate": translate_file}
        if video_file and json_file:
            self.signal.emit(data)
            self.close()
        else:
            t = []
            if not video_file:
                t.append("视频文件")
            if not json_file:
                t.append("数据文件")
            msg = "必须选择" + "、".join(t)
            QtWidgets.QMessageBox.warning(
                self, "错误", msg, QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.Yes
            )

    _startPos = None
    _endPos = None
    _isTracking = None

    # 鼠标移动事件
    def mouseMoveEvent(self, a0: QtGui.QMouseEvent):
        if self._startPos:
            self._endPos = a0.position() - self._startPos
            # 移动窗口
            self.move(self.pos() + self._endPos.toPoint())

    def mousePressEvent(self, a0: QtGui.QMouseEvent):
        # 根据鼠标按下时的位置判断是否在QFrame范围内
        if self.childAt(a0.position().x(), a0.position().y()).objectName() in ["MainFrame", "TitleBar"]:
            # 判断鼠标按下的是左键
            if a0.button() == QtCore.Qt.MouseButton.LeftButton:
                self._isTracking = True
                # 记录初始位置
                self._startPos = QtCore.QPoint(a0.position().x(), a0.position().y())

    # 鼠标松开事件
    def mouseReleaseEvent(self, a0: QtGui.QMouseEvent):
        if a0.button() == QtCore.Qt.MouseButton.LeftButton:
            self._isTracking = False
            self._startPos = None
            self._endPos = None

