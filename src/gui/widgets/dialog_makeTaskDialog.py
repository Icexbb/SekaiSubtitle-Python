import os

from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtCore import Signal
from qframelesswindow import FramelessDialog

from gui.design.WidgetNewTaskSelector import Ui_SelectWidget as Selector
from gui.design.WindowDialogNewSubTask import Ui_NewSubProcessDialog as Dialog
from gui.widgets.widget_titlebar import TitleBar


class FileSelector(QtWidgets.QWidget, Selector):
    select_signal = Signal()

    def __init__(self, parent, filetype: str, filetype_list: list):
        super().__init__()
        self.setupUi(self)
        self.parent: NewTaskDialog = parent
        self.HintLabel.setText(f"{filetype}文件")
        self.acceptFileTypes = filetype_list
        self.setAcceptDrops(True)
        self.SelectButton.clicked.connect(lambda: self.chooseFile())
        self._fileSelected = None

    @property
    def fileSelected(self):
        return self._fileSelected

    @fileSelected.setter
    def fileSelected(self, value):
        self._fileSelected = value
        self.select_signal.emit()
        if value:
            if isinstance(value, list):
                self.FileLabel.setText(",".join([os.path.split(file)[-1] for file in value]))
            else:
                self.FileLabel.setText(os.path.split(value)[-1])
        else:
            self.FileLabel.setText("未选择")

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        if event.button() == QtCore.Qt.MouseButton.RightButton:
            self.fileSelected = None

    def chooseFile(self):
        if ("*.json" in self.acceptFileTypes) or self.parent.dryrun:
            files, _ = QtWidgets.QFileDialog.getOpenFileNames(
                self, "选取文件", dir=self.parent.parent.choose_file_root,
                filter=f"可接受的文件 ({' '.join(self.acceptFileTypes)});;全部文件 (*)")
            if files:
                if len(files) == 1:
                    self.fileSelected = files[0]
                else:
                    self.fileSelected = files
                self.parent.parent.choose_file_root = os.path.split(files[0])[0]
        else:
            file_name_choose, _ = QtWidgets.QFileDialog.getOpenFileName(
                self, "选取文件", dir=self.parent.parent.choose_file_root,
                filter=f"可接受的文件 ({' '.join(self.acceptFileTypes)});;全部文件 (*)")
            if file_name_choose and os.path.exists(file_name_choose):
                self.fileSelected = file_name_choose
                self.parent.parent.choose_file_root = os.path.split(file_name_choose)[0]

    def clearSelect(self):
        self.fileSelected = None

    def dragEnterEvent(self, event: QtGui.QDragEnterEvent) -> None:
        if event.mimeData().text().endswith(tuple([filetype.removeprefix("*") for filetype in self.acceptFileTypes])):
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event: QtGui.QDropEvent) -> None:
        path = event.mimeData().text().replace('file:///', '')  # 删除多余开头
        if os.path.exists(path):
            self.fileSelected = path


class NewTaskDialog(FramelessDialog, Dialog):
    signal = QtCore.Signal(dict)

    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("新任务")
        self.setObjectName("New Task")

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        from gui.gui_main import MainUi
        self.parent: MainUi = parent

        self.TitleBar = TitleBar(self)

        self.TitleBar.WindowMaxButton.setHidden(True)
        self.TitleBar.WindowMinButton.setHidden(True)
        self.TitleBar.mouseDoubleClickEvent = lambda x: {None}
        self.setTitleBar(self.TitleBar)

        self.VideoSelector = FileSelector(self, "视频", ['*.mp4', '*.avi', '*.wmv', "*.mkv"])
        self.JsonSelector = FileSelector(self, "数据", ['*.json', ".asset"])
        self.TranslateSelector = FileSelector(self, "翻译", ['*.txt'])

        self.setAcceptDrops(True)
        self.SelectBoxLayout.addWidget(self.VideoSelector)
        self.SelectBoxLayout.addWidget(self.JsonSelector)
        self.SelectBoxLayout.addWidget(self.TranslateSelector)
        self.EmitButton.clicked.connect(self.emitTask)

        self.DryRunCheck.stateChanged.connect(self.dryrun_stage_changed)
        self.VideoSelector.select_signal.connect(self.fileAutoSelect)

    @property
    def dryrun(self):
        return self.DryRunCheck.isChecked()

    def fileAutoSelect(self):
        video_file = self.VideoSelector.fileSelected
        if not self.dryrun:
            if isinstance(video_file, str) or (isinstance(video_file, list) and len(video_file) == 1):
                video_file = video_file[0] if isinstance(video_file, list) else video_file
                if video_file and os.path.exists(video_file):
                    file_prefix: str = os.path.splitext(video_file)[0]
                    predict_json = file_prefix + ".json"
                    predict_translate = file_prefix + ".txt"
                    if os.path.exists(predict_json):
                        self.JsonSelector.fileSelected = predict_json
                    if os.path.exists(predict_translate):
                        self.TranslateSelector.fileSelected = predict_translate
        else:
            self.clear_auto_select()

    def clear_auto_select(self):
        self.JsonSelector.clearSelect()
        self.TranslateSelector.clearSelect()

    def dryrun_stage_changed(self):
        self.TranslateSelector.setEnabled(not self.dryrun)
        self.JsonSelector.setEnabled(not self.dryrun)
        if self.dryrun:
            self.clear_auto_select()
        else:
            self.fileAutoSelect()

    def emitTask(self):
        video_files = self.VideoSelector.fileSelected
        json_file = self.JsonSelector.fileSelected
        translate_file = self.TranslateSelector.fileSelected

        if self.dryrun:
            if isinstance(video_files, list):
                pass
            else:
                video_files = [video_files]
            for video_file in video_files:
                data = {"video": video_file, "dryrun": True, "font": self.parent.font}
                self.signal.emit(data)
            if not video_files:
                QtWidgets.QMessageBox.warning(
                    self, "错误", "必须选择视频文件",
                    QtWidgets.QMessageBox.StandardButton.Yes, QtWidgets.QMessageBox.StandardButton.Yes
                )
            else:
                self.close()
        else:
            data = {"video": video_files, "json": json_file, "translate": translate_file, "font": self.parent.font}
            if video_files and json_file:
                self.signal.emit(data)
                self.close()
            else:
                t = []
                if not video_files:
                    t.append("视频文件")
                if not json_file:
                    t.append("数据文件")
                msg = "必须选择" + "、".join(t)
                QtWidgets.QMessageBox.warning(
                    self, "错误", msg,
                    QtWidgets.QMessageBox.StandardButton.Yes, QtWidgets.QMessageBox.StandardButton.Yes
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
