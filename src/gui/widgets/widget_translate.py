import os
import re
import sys

from PySide6 import QtWidgets, QtCore, QtGui

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
        # elif len_translate > len_origin:
        #    waring = int((1 - min((len_translate - len_origin) / (len_origin * 0.5), 1)) * 160) + 60
        #    ss = f"color: rgb(255, {max(60, waring)}, 60);"
        #    self.TextEditTranslate.setStyleSheet(ss)
        else:
            self.TextEditTranslate.setStyleSheet("")
        if len_translate:
            self.TextLengthLabel.setText(f"{len_translate}/{len_origin} ")
        else:
            self.TextLengthLabel.clear()

    @property
    def translatedString(self):
        return self.TextEditTranslate.text()


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
        else:
            self.chara = ""
            self.LabelType.setText("位置")
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


class ListWidgetItem(QtWidgets.QListWidgetItem):
    def __init__(self):
        super().__init__()
        self.num = None


class TranslateWidget(Ui_Translate, QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__()
        self.trans_file = None
        self.data = None
        self.data_file = None
        self.setupUi(self)
        self.parent = parent
        self.lines: list[WidgetTranslateItem] = []

        self.ButtonLoad.clicked.connect(self.load_json)
        self.ButtonSave.clicked.connect(self.save_file)
        self.ButtonOpen.clicked.connect(self.load_text)
        self.ButtonClear.clicked.connect(self.clearItem)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event: QtGui.QDragEnterEvent) -> None:
        path = event.mimeData().text()
        if path.endswith(".json"):
            event.accept()
        elif path.endswith(".txt"):
            if self.data_file and self.data:
                event.accept()
            else:
                event.ignore()
        else:
            event.ignore()

    def dropEvent(self, event: QtGui.QDropEvent):
        path = event.mimeData().text().replace('file:///', '')
        if path.endswith((".json", ".asset")):
            self.load_json(path)
        else:
            self.load_text(path)

    def load_json(self, file_name_choose=None):
        if not file_name_choose:
            file_name_choose, _ = QtWidgets.QFileDialog.getOpenFileName(
                self, "选取文件", dir=os.getcwd(),
                filter=f"JSON文件 (*.json);;全部文件 (*)")
        if file_name_choose and os.path.exists(file_name_choose):
            self.clearItem()
            self.data_file = file_name_choose
            self.data = read_json(self.data_file)
            se_count = 0
            td_count = 0
            total_count = 0
            for item in self.data.get("Snippets"):
                if item["Action"] == 1:
                    self.newItem(self.data["TalkData"][td_count], total_count)
                    td_count += 1
                    total_count += 1
                elif item["Action"] == 6:
                    data = self.data["SpecialEffectData"][se_count]
                    if data['EffectType'] == 8:
                        self.newItem(data, total_count)
                    se_count += 1
                    total_count += 1

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

    def save_file(self):
        result = []
        if self.data_file:
            filename = QtWidgets.QFileDialog.getSaveFileName(
                self, "保存", os.path.split(self.trans_file)[0] if self.trans_file else "" or os.getcwd(),
                "SekaiText文件(*.txt);;all files(*.*)")
            filepath, filename = os.path.split(filename[0])
            for line in self.lines:
                if line.CharaWidget.LabelName.text():
                    string = line.CharaWidget.LabelName.text() + "："
                else:
                    string = ""
                string += line.translated
                result.append(string)
            with open(os.path.join(filepath, filename), 'w', encoding='utf8') as fp:
                fp.writelines("\n".join(result))
            msg = QtWidgets.QMessageBox(
                icon=QtWidgets.QMessageBox.Icon.NoIcon,
                text=f"已保存到 {os.path.join(filepath, filename)}", parent=self
            )
            msg.setWindowTitle("SekaiText")
            msg.exec_()
            msg.close()

        # Action 1 TalkData
        # Action 2 LayoutData
        # Action 4 LayoutData
        # Action 6 SpecialEffectData
        # Action 7 SoundData
        # Action 8 ScenarioSnippetCharacterLayoutModes

    def load_text(self, file_name_choose=None):
        if not self.data:
            msg = QtWidgets.QMessageBox(
                icon=QtWidgets.QMessageBox.Icon.Warning,
                text=f"请先载入一个Json文件", parent=self
            )
            msg.setWindowTitle("SekaiText")
            msg.exec_()
            msg.close()
            return
        if not file_name_choose:
            file_name_choose, _ = QtWidgets.QFileDialog.getOpenFileName(
                self, "选取文件", dir=os.getcwd(),
                filter=f"SekaiText文件 (*.txt);;全部文件 (*)")
        if file_name_choose and os.path.exists(file_name_choose):
            self.trans_file = file_name_choose
            self.EditTitle.setText(os.path.splitext(os.path.split(file_name_choose)[-1])[0])
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
            if len(res) == len(self.lines):
                for lines, widget in zip(res, self.lines):
                    for index, string in enumerate(lines):
                        widget.lines[index].TextEditTranslate.setText(string)
            else:
                for line_index, lines in enumerate(res):
                    widget = self.lines[line_index]
                    for index, string in enumerate(lines):
                        widget.lines[index].TextEditTranslate.setText(string)
