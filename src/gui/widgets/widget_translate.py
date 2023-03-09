import os
import re
import sys

import yaml
from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtCore import Signal

from gui.design.WidgetTranslate import Ui_Form as Ui_Translate
from gui.design.WidgetTranslateIcon import Ui_Form as Ui_CharaIcon
from gui.design.WidgetTranslateItem import Ui_WidgetTranslateItem as Ui_TranslateItem
from gui.design.WidgetTranslateLines import Ui_Form as Ui_TranslateLines
from script.tools import read_json


class WidgetCharaIcon(Ui_CharaIcon, QtWidgets.QWidget):
    def __init__(self, chara: str):
        super().__init__()
        self.setupUi(self)
        self.LabelIcon.setText("")
        self.LabelName.setText(chara)


class WidgetTranslateLines(Ui_TranslateLines, QtWidgets.QWidget):
    def __init__(self, string):
        super().__init__()
        self.setupUi(self)
        self.string = string
        self.TextBrowserOrigin.setText(self.string)
        self.TextEditTranslate.textChanged.connect(self.changeTextColor)
        self.ClearButton.clicked.connect(self.TextEditTranslate.clear)

    def changeTextColor(self):
        len_origin = len(self.TextBrowserOrigin.text())
        len_translate = len(self.TextEditTranslate.text().replace("...", "…"))
        if len_translate > 30:
            self.TextEditTranslate.setStyleSheet(f"color: rgb(255, 0, 0);")
        else:
            self.TextEditTranslate.setStyleSheet("")
        if len_translate:
            self.TextLengthLabel.setText(f"{len_translate}/{len_origin} ")
        else:
            self.TextLengthLabel.clear()

    @property
    def translatedString(self):
        return self.TextEditTranslate.text()

    @translatedString.setter
    def translatedString(self, value: str):
        self.TextEditTranslate.setText(value)


class WidgetTranslateItem(Ui_TranslateItem, QtWidgets.QWidget):
    def __init__(self, data: dict, num: int):
        super().__init__()
        self.setupUi(self)
        self.data = data
        self.num = num
        self.LabelNumber.setText(str(num))
        self.lines = []
        if s := self.data.get("WindowDisplayName"):
            self.chara = s
            self.LabelType.setText("对话")
            self.strings = self.data.get("Body").split("\n")
            self.type = "dialog"
        else:
            self.chara = ""
            if self.data.get("EffectType") == 18:
                self.LabelType.setText("角标")
                self.type = "tag"
            else:
                self.LabelType.setText("横幅")
                self.type = "banner"
            self.strings = [self.data.get("StringVal")]
        self.CharaWidget = WidgetCharaIcon(self.chara)
        self.FrameCharaLayout.addWidget(self.CharaWidget)

        for string in self.strings:
            line = WidgetTranslateLines(string)
            self.WidgetLinesLayout.addWidget(line)
            self.lines.append(line)
        self.setFixedHeight(66 * len(self.lines))

    @property
    def translated(self):
        res = []
        for line in self.lines:
            res.append(line.translatedString)
        return r"\N".join(res)

    @translated.setter
    def translated(self, value: str):
        strings = value.replace(r"\N", "\n").split("\n")
        if len(strings) != len(self.lines):
            p = ["" for _ in self.lines]
            for index, string in enumerate(strings):
                p[index] = string
            strings = p
        for line, string in zip(self.lines, strings):
            line.translatedString = string


class ListWidgetItem(QtWidgets.QListWidgetItem):
    def __init__(self):
        super().__init__()
        self.num = None


class RightClickEnabledButton(QtWidgets.QPushButton):
    def __init__(self, text=None, name=None):
        super().__init__()
        if text:
            self.setText(text)
        if name:
            self.setObjectName(name)

    rightClicked = Signal()
    clicked = Signal()

    def mousePressEvent(self, evt):
        super().mousePressEvent(evt)
        # 为右键单击事件建立信号
        if evt.button() == QtCore.Qt.MouseButton.RightButton:
            self.rightClicked.emit()
        elif evt.button() == QtCore.Qt.MouseButton.LeftButton:
            self.clicked.emit()


class TranslateWidget(Ui_Translate, QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__()
        self.trans_file = None
        self.data = None
        self.data_file = None
        self.setupUi(self)
        from gui.gui_main import MainUi
        self.parent: MainUi = parent
        self.lines: list[WidgetTranslateItem] = []

        self.ButtonLoad.clicked.connect(self.load_json)
        self.ButtonClear.clicked.connect(self.clearItem)
        self.ButtonOpen.clicked.connect(self.load_text)

        self.ButtonSave.deleteLater()
        self.ButtonSave = RightClickEnabledButton("保存", "ButtonSave")
        self.horizontalLayout.addWidget(self.ButtonSave)

        self.ButtonSave.clicked.connect(self.save_file_yaml)
        self.ButtonSave.rightClicked.connect(self.save_file_txt)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event: QtGui.QDragEnterEvent) -> None:
        path = event.mimeData().text()
        if path.endswith(".json"):
            event.accept()
        elif path.endswith((".txt", ".yml")):
            if self.data_file and self.data:
                event.accept()
            else:
                event.ignore()
        else:
            event.ignore()

    def dropEvent(self, event: QtGui.QDropEvent):
        path = event.mimeData().text().replace('file:///', '')
        if path.lower().endswith((".json", ".asset")):
            self.load_json(path)
        else:
            self.load_text(path)

    def load_json(self, file_name_choose=None):
        if not file_name_choose:
            file_name_choose, _ = QtWidgets.QFileDialog.getOpenFileName(
                self, "选取文件", dir=self.parent.choose_file_root,
                filter=f"剧情数据文件 (*.json,*.asset);;全部文件 (*)")
        if file_name_choose and os.path.exists(file_name_choose):
            self.parent.choose_file_root = os.path.split(file_name_choose)[0]
            self.clearItem()
            self.data_file = file_name_choose
            self.data = read_json(self.data_file)
            se_count = 0
            td_count = 0
            total_count = 0
            for item in self.data.get("Snippets"):
                if item["Action"] == 1:
                    self.newItem(self.data["TalkData"][td_count], total_count)
                    total_count += 1
                    td_count += 1
                elif item["Action"] == 6:
                    data = self.data["SpecialEffectData"][se_count]
                    if data['EffectType'] == 8:
                        self.newItem(data, total_count)
                        total_count += 1
                    elif data['EffectType'] == 18:
                        self.newItem(data, total_count)
                        total_count += 1
                    se_count += 1

    def clearItem(self):
        for i in range(self.ListWidgetLine.count()):
            self.ListWidgetLine.removeItemWidget(self.ListWidgetLine.takeItem(i))
        self.lines.clear()
        self.data_file = None
        self.data = None

    def newItem(self, data, item_id):
        line = WidgetTranslateItem(data, item_id + 1)
        if line.data.get("TalkCharacters"):
            cid = line.data.get("TalkCharacters")[0].get("Character2dId")
            for c in self.data['AppearCharacters']:
                if c['Character2dId'] == cid:
                    if c['CostumeType'][:2].isdigit():
                        chara_id = str(int(c['CostumeType'][:2]))
                        icon_path = f"asset/icon/chr_{chara_id}.png"
                        if getattr(sys, 'frozen', False):
                            icon_path = os.path.join(sys._MEIPASS, icon_path)
                        if os.path.exists(icon_path):
                            line.CharaWidget.LabelIcon.setPixmap(
                                QtGui.QPixmap(icon_path).scaledToWidth(
                                    50, QtCore.Qt.TransformationMode.SmoothTransformation))
        item = ListWidgetItem()
        item.num = item_id
        item.setSizeHint(QtCore.QSize(self.ListWidgetLine.width(), line.size().height()))
        item.setSizeHint(line.size() + QtCore.QSize(-60, 0))
        self.ListWidgetLine.addItem(item)
        self.ListWidgetLine.setItemWidget(item, line)
        self.lines.append(line)

    def save_file_txt(self):
        if [line for line in self.lines if line.type == 'tag']:
            msg = QtWidgets.QMessageBox.question(
                self, "SekaiText - 保存", "目前的翻译文档内有角标，保存为旧版txt格式会丢失该部分信息\n是否继续？",
                QtWidgets.QMessageBox.StandardButton.Yes, QtWidgets.QMessageBox.StandardButton.No
            )
            if msg == QtWidgets.QMessageBox.StandardButton.No:
                return
        result = []
        if self.data_file:
            filename = QtWidgets.QFileDialog.getSaveFileName(
                self, "保存",
                os.path.split(self.trans_file)[0] if self.trans_file else "" or self.parent.choose_file_root,
                "SekaiText文件(*.txt);;all files(*.*)")
            if filename[1]:
                for line in self.lines:
                    if line.CharaWidget.LabelName.text():
                        string = line.CharaWidget.LabelName.text() + "："
                    else:
                        string = ""
                    string += line.translated
                    result.append(string)
                with open(filename[0], 'w', encoding='utf8') as fp:
                    fp.writelines("\n".join(result))
                msg = QtWidgets.QMessageBox(
                    icon=QtWidgets.QMessageBox.Icon.NoIcon,
                    text=f"已保存到 {filename[0]}", parent=self
                )
                msg.setWindowTitle("SekaiText")
                msg.exec_()

    def save_file_yaml(self):
        if self.data_file:
            filename = QtWidgets.QFileDialog.getSaveFileName(
                self, "保存",
                os.path.split(self.trans_file)[0] if self.trans_file else "" or self.parent.choose_file_root,
                "SekaiSubtitle翻译文件(*.yml);;all files(*.*)")
            if filename[1]:
                data = {"dialog": [], "tag": [], "banner": []}
                for line in self.lines:
                    if line.type in data.keys():
                        data[line.type].append(line.translated)
                with open(filename[0], 'w', encoding='utf8') as fp:
                    fp.write(yaml.dump(data))
                msg = QtWidgets.QMessageBox(
                    icon=QtWidgets.QMessageBox.Icon.NoIcon,
                    text=f"已保存到 {filename[0]}", parent=self
                )
                msg.setWindowTitle("SekaiText")
                msg.exec_()

    # Action 1 TalkData
    # Action 2 LayoutData
    # Action 4 LayoutData
    # Action 6 SpecialEffectData
    # Action 7 SoundData
    # Action 8 ScenarioSnippetCharacterLayoutModes

    def load_text(self, file_name_choose=None):
        if not self.data:
            msg = QtWidgets.QMessageBox(
                icon=QtWidgets.QMessageBox.Icon.Warning, text=f"请先载入一个数据文件", parent=self
            )
            msg.setWindowTitle("SekaiText")
            msg.exec_()
            msg.close()
            return
        if not file_name_choose:
            file_name_choose, _ = QtWidgets.QFileDialog.getOpenFileName(
                self, "选取文件", dir=os.getcwd(),
                filter=f"SekaiText文件 (*.txt *.yml);;全部文件 (*)")
        if file_name_choose and os.path.exists(file_name_choose):
            self.trans_file = file_name_choose
            self.EditTitle.setText(os.path.splitext(os.path.split(file_name_choose)[-1])[0])

            if os.path.splitext(file_name_choose)[-1].lower() == ".txt":
                pattern_body = re.compile(r"^(?P<name>\S*)：(?P<body>.+)$")
                pattern_place = re.compile(r"^(?P<place>\S[^：]*)$")
                with open(file_name_choose, 'r', encoding='utf-8') as fp:
                    data = fp.readlines()
                res = []
                for data_string in data:
                    if data_string:
                        if s := re.match(pattern_body, data_string.strip()):
                            res.append(s.group("body").split(r"\N"))
                        elif s := re.match(pattern_place, data_string.strip()):
                            res.append([s.group("place")])
                limited_lines = [line for line in self.lines if line.type in ["dialog", "banner"]]
                if len(res) == len(limited_lines):
                    for lines, widget in zip(res, limited_lines):
                        for index, string in enumerate(lines):
                            widget.lines[index].TextEditTranslate.setText(string)
                else:
                    for line_index, lines in enumerate(res):
                        widget = limited_lines[line_index]
                        for index, string in enumerate(lines):
                            widget.lines[index].TextEditTranslate.setText(string)
            elif os.path.splitext(file_name_choose)[-1].lower() == ".yml":
                with open(file_name_choose, 'r', encoding='utf-8') as fp:
                    data = yaml.load(fp, yaml.Loader)
                for line_type in ["banner", "tag", "dialog"]:
                    index_list = [index for index, line in enumerate(self.lines) if line.type == line_type]
                    index_count = len(index_list)
                    if index_count == len(data[line_type]):
                        for index_of_data, index_of_widget in enumerate(index_list):
                            self.lines[index_of_widget].translated = data[line_type][index_of_data]
