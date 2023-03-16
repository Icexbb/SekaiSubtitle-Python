import datetime
import os

from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtCore import Signal
from qframelesswindow import FramelessDialog

from gui.design.WidgetNewTaskSelector import Ui_SelectWidget as Selector
from gui.design.WidgetSubtitleTimebar import Ui_Form as TimeSelector
from gui.design.WindowDialogNewSubTask import Ui_NewSubProcessDialog as Dialog
from gui.widgets.dialog_makeStaffInfo import NewStaffDialog
from gui.widgets.widget_titlebar import TitleBar
from script.tools import timedelta_to_string


class SubtitleTimeSelector(QtWidgets.QWidget, TimeSelector):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        self._vtime = None
        self.RightSpin.valueChanged.connect(self.repaint_timeline)
        self.LeftSpin.valueChanged.connect(self.repaint_timeline)
        self.LLabel.setText("")
        self.RLabel.setText("")
        self.CLabel.setText("")
        self.video_fps = 60

    def repaint_timeline(self):
        total_length = self.widget.width() - 10
        left_per = self.LeftSpin.value() / self.video_frames
        right_per = 1 - self.RightSpin.value() / self.video_frames
        self.LeftSpin.setMaximum(self.RightSpin.value())
        self.RightSpin.setMinimum(self.LeftSpin.value())

        self.LLabel.setText(
            timedelta_to_string(datetime.timedelta(seconds=(1 / self.video_fps) * self.LeftSpin.value())))
        self.RLabel.setText(
            timedelta_to_string(datetime.timedelta(seconds=(1 / self.video_fps) * self.RightSpin.value())))
        self.CLabel.setText(
            timedelta_to_string(
                datetime.timedelta(seconds=(1 / self.video_fps) * (self.RightSpin.value() - self.LeftSpin.value())))
        )
        self.VRight.setFixedWidth(int(max(5, right_per * total_length + 5)))
        self.VLeft.setFixedWidth(int(max(5, left_per * total_length + 5)))

    @property
    def video_frames(self):
        return self._vtime

    @video_frames.setter
    def video_frames(self, value: int):
        self._vtime = value
        self.LeftSpin.setMaximum(self.video_frames)
        self.RightSpin.setMaximum(self.video_frames)
        self.RightSpin.setValue(self.video_frames)

    @property
    def duration(self):
        if self.LeftSpin.value() == 0 and self.RightSpin.value() == self.RightSpin.maximum():
            return None
        return [self.LeftSpin.value(), self.RightSpin.value()]


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

        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        from gui.gui_main import MainUi
        self.parent: MainUi = parent
        self.TitleBar = TitleBar(self)

        self.TitleBar.WindowMaxButton.setHidden(True)
        self.TitleBar.WindowMinButton.setHidden(True)
        self.TitleBar.mouseDoubleClickEvent = lambda x: {None}
        self.setTitleBar(self.TitleBar)

        self.VideoSelector = FileSelector(self, "视频", ['*.mp4', '*.avi', '*.wmv', "*.mkv"])
        self.JsonSelector = FileSelector(self, "数据", ['*.json', ".asset"])
        self.TranslateSelector = FileSelector(self, "翻译", ['*.txt', "*.yml"])
        self.VideoTimeSelector = SubtitleTimeSelector(self)

        self.setAcceptDrops(True)
        self.SelectBoxLayout.addWidget(self.VideoSelector)
        self.SelectBoxLayout.addWidget(self.JsonSelector)
        self.SelectBoxLayout.addWidget(self.TranslateSelector)
        self.SelectBoxLayout.addWidget(self.VideoTimeSelector)
        self.VideoTimeSelector.setEnabled(False)
        self.EmitButton.clicked.connect(self.emitTask)
        self.staff_line = []
        self.StaffAddButton.clicked.connect(lambda: self.add_staff())
        self.StaffAddButton.setFocusPolicy(QtGui.Qt.FocusPolicy.NoFocus)
        self.EmitButton.setFocusPolicy(QtGui.Qt.FocusPolicy.StrongFocus)

        self.DryRunCheck.stateChanged.connect(self.dryrun_stage_changed)
        self.VideoSelector.select_signal.connect(self.fileAutoSelect)
        self.VideoSelector.select_signal.connect(self.setVideoTime)
        self.setVideoTime()

    def setVideoTime(self):
        if self.dryrun:
            self.VideoTimeSelector.setEnabled(False)
        else:
            self.VideoTimeSelector.setEnabled(True)

        if self.VideoSelector.fileSelected:
            if isinstance(self.VideoSelector.fileSelected,
                          list) and len(self.VideoSelector.fileSelected) == 1:
                f = self.VideoSelector.fileSelected[0]
            elif isinstance(self.VideoSelector.fileSelected, str):
                f = self.VideoSelector.fileSelected
            else:
                return
            import cv2
            v = cv2.VideoCapture(f)
            video_frames = v.get(cv2.CAP_PROP_FRAME_COUNT)
            video_fps = v.get(cv2.CAP_PROP_FPS)
            self.VideoTimeSelector.video_frames = video_frames
            self.VideoTimeSelector.video_fps = video_fps
        else:
            self.VideoTimeSelector.setEnabled(False)
        # self.VideoTimeSelector.setHidden(True)

    def add_staff(self, file=None):
        preload_data = {}
        if self.TranslateSelector.fileSelected:
            name = self.TranslateSelector.FileLabel.text()
            name = name.lower() \
                .removeprefix("【合意】").removeprefix("【校对】").removeprefix("【翻译】") \
                .removesuffix(".txt").removesuffix(".yml")
            preload_data["prefix"] = f"字幕制作 by PJS字幕组\n{name}"
        dialog = NewStaffDialog(self, preload_data)
        if file and os.path.exists(file):
            if file.endswith(".json"):
                dialog.load(file)
        dialog.signal.connect(
            lambda data: {
                self.staff_line.append(data),
                self.StaffAddButton.setText(f"已有Staff行*{len(self.staff_line)}")
            }
        )
        dialog.exec()
        dialog.close()

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
                    for ext in [".json", ".asset"]:
                        predict_json = file_prefix + ext
                        if os.path.exists(predict_json):
                            self.JsonSelector.fileSelected = predict_json
                    for ext in [".txt", ".yml"]:
                        predict_translate = file_prefix + ext
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
        self.StaffAddButton.setEnabled(not self.dryrun)
        if self.dryrun:
            self.staff_line.clear()
            self.StaffAddButton.setText("添加Staff行")
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
                data = {"video": video_file, "dryrun": True, "font": self.parent.font, "staff": self.staff_line}
                if len(video_files) == 1:
                    data["duration"] = self.VideoTimeSelector.duration
                self.signal.emit(data)
            if not video_files:
                QtWidgets.QMessageBox.warning(
                    self, "错误", "必须选择视频文件",
                    QtWidgets.QMessageBox.StandardButton.Yes, QtWidgets.QMessageBox.StandardButton.Yes
                )
            else:
                self.close()
        else:
            data = {
                "video": video_files, "json": json_file, "translate": translate_file,
                "font": self.parent.font, "staff": self.staff_line,
                "duration": self.VideoTimeSelector.duration}
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
