import json
import os
from datetime import timedelta

from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtCore import Signal
from PySide6.QtGui import QDoubleValidator
from qframelesswindow import FramelessDialog

from gui.design.WindowDialogStaff import Ui_NewStaffDialog
from gui.widgets.widget_titlebar import TitleBar
from script.tools import read_json, timedelta_to_string


class NewStaffDialog(FramelessDialog, Ui_NewStaffDialog):
    signal = Signal(dict)

    def __init__(self, parent, preload_data: dict = None):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.TitleBar = TitleBar(self)

        self.TitleBar.WindowMaxButton.setHidden(True)
        self.TitleBar.WindowMinButton.setHidden(True)
        self.TitleBar.mouseDoubleClickEvent = lambda x: {None}
        self.setTitleBar(self.TitleBar)
        self.EditDuration.setValidator(QDoubleValidator(0.0, 600.0, 2))

        self.ButtonSubmit.clicked.connect(lambda: {self.signal.emit(self.subtitle_data), self.close()})
        self.ButtonExport.clicked.connect(lambda: self.save())
        self.ButtonImport.clicked.connect(lambda: self.load())
        self.EditSubMaker.setText("SEKAI的轴姬")
        if preload_data:
            self.preload(preload_data)

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        if event.matches(QtGui.QKeySequence.StandardKey.Paste):
            pasted = QtWidgets.QApplication.clipboard().text().strip().split("\t")
            data = {}
            if len(pasted) in [4, 5, 6]:
                data = {"translator": pasted[0], "translate_proof": pasted[1], "subtitle_proof": pasted[-1]}
            elif len(pasted) in [3, 2]:
                data = {"translator": pasted[0], "translate_proof": pasted[1]}
            if len(pasted) == 7:
                data = {"recorder": pasted[0], "translator": pasted[1], "translate_proof": pasted[2],
                        "subtitle_proof": pasted[-1]}
            self.preload(data)
        FramelessDialog.keyPressEvent(self, event)

    def preload(self, data):
        if s := data.get("recorder"):
            self.EditRecord.setText(s)
        if s := data.get("translator"):
            self.EditTranslator.setText(s)
        if s := data.get("translate_proof"):
            self.EditTranslateProof.setText(s)
        if s := data.get("subtitle_maker"):
            self.EditSubMaker.setText(s)
        if s := data.get("subtitle_proof"):
            self.EditSubProof.setText(s)
        if s := data.get("prefix"):
            self.EditPrefix.setPlainText(s)
        if s := data.get("subfix"):
            self.EditSubfix.setPlainText(s)
        if data.get("position") in ['1', '3', '7', '9']:
            self.set_position_radio(int(data.get("position")))
        else:
            self.set_position_radio(1)
        if s := data.get("duration"):
            self.EditDuration.setText(str(s))
        else:
            self.EditDuration.setText("5")

    def set_position_radio(self, value):
        if value == 9:
            self.RadioPos1.setChecked(False)
            self.RadioPos3.setChecked(False)
            self.RadioPos7.setChecked(False)
            self.RadioPos9.setChecked(True)
        elif value == 1:
            self.RadioPos1.setChecked(True)
            self.RadioPos3.setChecked(False)
            self.RadioPos7.setChecked(False)
            self.RadioPos9.setChecked(False)
        elif value == 3:
            self.RadioPos1.setChecked(False)
            self.RadioPos3.setChecked(True)
            self.RadioPos7.setChecked(False)
            self.RadioPos9.setChecked(False)
        else:
            self.RadioPos1.setChecked(False)
            self.RadioPos3.setChecked(False)
            self.RadioPos7.setChecked(True)
            self.RadioPos9.setChecked(False)

    @property
    def data(self):
        position = 7
        if self.RadioPos1.isChecked():
            position = 1
        elif self.RadioPos3.isChecked():
            position = 3
        elif self.RadioPos7.isChecked():
            position = 7
        elif self.RadioPos9.isChecked():
            position = 9
        result = {
            "recorder": self.EditRecord.text(),
            "translator": self.EditTranslator.text(),
            "translate_proof": self.EditTranslateProof.text(),
            "subtitle_maker": self.EditSubMaker.text(),
            "subtitle_proof": self.EditSubProof.text(),
            "prefix": self.EditPrefix.toPlainText(),
            "subfix": self.EditSubfix.toPlainText(),
            "position": str(position),
            "duration": float(self.EditDuration.text())
        }
        return result

    def save(self):
        data = self.data
        filename = QtWidgets.QFileDialog.getSaveFileName(
            self, "保存", self.parent.parent.choose_file_root,
            "SekaiSubtitle StaffLine文件(*.Json);;all files(*.*)")
        if filename[0]:
            filepath, filename = os.path.split(filename[0])
            self.parent.parent.choose_file_root = filepath

            with open(os.path.join(filepath, filename), 'w', encoding='utf8') as fp:
                json.dump(data, fp, ensure_ascii=False, indent=4)
            msg = QtWidgets.QMessageBox(
                icon=QtWidgets.QMessageBox.Icon.NoIcon, text=f"已保存到 {os.path.join(filepath, filename)}", parent=self
            )
            msg.setWindowTitle("SekaiSubtitle")
            msg.exec_()
            msg.close()

    def load(self, file_name_choose=None):
        if not file_name_choose:
            file_name_choose, _ = QtWidgets.QFileDialog.getOpenFileName(
                self, "选取文件", dir=self.parent.parent.choose_file_root,
                filter=f"SekaiSubtitle StaffLine文件 (*.json);;全部文件 (*)")
        if file_name_choose and os.path.exists(file_name_choose):
            self.parent.parent.choose_file_root = os.path.split(file_name_choose)[0]
            data = read_json(file_name_choose)
            self.preload(data)

    @property
    def subtitle_body(self):
        string = ""
        if s := (self.data.get("prefix")).strip():
            string += f"{s}\n"
        if s := (self.data.get("recorder")).strip():
            string += f"录制：{s}\n"
        if s := (self.data.get("translator")).strip():
            string += f"翻译：{s}\n"
        if s := (self.data.get("translate_proof")).strip():
            string += f"翻校：{s}\n"
        if s := (self.data.get("subtitle_maker")).strip():
            string += f"时轴：{s}\n"
        if s := (self.data.get("subtitle_proof")).strip():
            string += f"轴校&压制：{s}\n"
        if s := (self.data.get("subfix")).strip():
            string += f"{s}\n"
        string = string.strip().replace("\n", r"\N")
        return string

    @property
    def subtitle_data(self):
        data = {
            'Layer': 1, 'Start': '0:00:00.00', 'End': timedelta_to_string(timedelta(seconds=self.data["duration"])),
            'Style': f"staff-{self.data['position']}", 'Name': 'staff', 'MarginL': 0, 'MarginR': 0, 'MarginV': 0,
            'Effect': '', 'Text': self.subtitle_body
        }
        return data

    _startPos = None
    _endPos = None
    _isTracking = None

    def mouseMoveEvent(self, a0: QtGui.QMouseEvent):
        if self._startPos:
            self._endPos = a0.position() - self._startPos
            self.move(self.pos() + self._endPos.toPoint())

    def mousePressEvent(self, a0: QtGui.QMouseEvent):
        if self.childAt(a0.position().x(), a0.position().y()).objectName() in ["MainFrame", "TitleBar"]:
            if a0.button() == QtCore.Qt.MouseButton.LeftButton:
                self._isTracking = True
                self._startPos = QtCore.QPoint(a0.position().x(), a0.position().y())

    # 鼠标松开事件
    def mouseReleaseEvent(self, a0: QtGui.QMouseEvent):
        if a0.button() == QtCore.Qt.MouseButton.LeftButton:
            self._isTracking = False
            self._startPos = None
            self._endPos = None
