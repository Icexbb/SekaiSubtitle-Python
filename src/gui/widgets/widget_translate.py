import datetime
import os
import re

import yaml
from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtCore import Signal

from gui.design.WidgetTranslate import Ui_Form as Ui_Translate
from gui.design.WidgetTranslateIcon import Ui_Form as Ui_CharaIcon
from gui.design.WidgetTranslateItem import Ui_WidgetTranslateItem as Ui_TranslateItem
from gui.design.WidgetTranslateLines import Ui_Form as Ui_TranslateLines
from script.data import get_asset_path
from script.tools import read_json


class WidgetCharaIcon(Ui_CharaIcon, QtWidgets.QWidget):
    def __init__(self, chara: str):
        super().__init__()
        self.setupUi(self)
        self.LabelIcon.setText("")
        self.LabelName.setText(chara)


class WidgetTranslateLines(Ui_TranslateLines, QtWidgets.QWidget):
    def __init__(self, parent, string,check_text=True):
        super().__init__()
        self.check_text = check_text
        self.setupUi(self)
        self.parent: WidgetTranslateItem = parent
        self.string = string
        self.TextBrowserOrigin.setText(self.string)
        self.TextEditTranslate.textChanged.connect(self.checkText)
        self.ClearButton.clicked.connect(self.TextEditTranslate.clear)
        self.parent.parent.type_signal.connect(self.changeProcessType)
        self.changeProcessType(self.parent.parent.ProcessType)

    def checkText(self):
        text = self.TextEditTranslate.text()
        if text and self.check_text:
            text = text.replace('…', '...')
            text = text.replace('(', '（').replace(')', '）')
            text = text.replace(',', '，').replace('?', '？').replace('!', '！')
            text = text.replace('欸', '诶')
            self.TextEditTranslate.setText(text)

            check_result = self.contentCheck(text)
            self.WarningLabel.setText(check_result)
            if check_result:
                self.WidgetDown.setStyleSheet("#WidgetDown{background-color: rgba(255, 150, 150, 50);}")
            else:
                self.WidgetDown.setStyleSheet("")
        self.changeTextColor()
        self.parent.parent.change_signal.emit()

    @staticmethod
    def contentCheck(text):
        normal_end = ['、', '，', '。', '？', '！', '~', '♪', '☆', '.', '—']
        unusual_end = ['）', '」', '』', '”']
        result = ''
        if text[-1] in normal_end:
            if '.，' in text or '.。' in text:
                result += "\n【「……。」和「……，」只保留省略号】"
        elif text[-1] in unusual_end:
            if len(text) > 1 and text[-2] not in normal_end:
                result += "\n【句尾缺少逗号句号】"
        else:
            result += "\n【句尾缺少逗号句号】"
        if "—" in text:
            if len(text.split("—")) != len(text.split("——")) * 2 - 1:
                result += "\n【破折号用双破折——，或者视情况删掉】"
        return result.strip()

    def changeProcessType(self, value):
        if value:
            self.WidgetMiddle.setHidden(False)
            self.setFixedHeight(94)
        else:
            self.WidgetMiddle.setHidden(True)
            self.setFixedHeight(64)

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

    def loadTranslated(self, value: str):
        self.translatedString = value
        self.TextBrowserTranslated.setText(value)


class WidgetTranslateItem(Ui_TranslateItem, QtWidgets.QWidget):
    def __init__(self, parent, data: dict, num: int):
        super().__init__()
        self.setupUi(self)
        self.parent: TranslateWidget = parent
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
        self.parent.type_signal.connect(self.changeProcess)
        for string in self.strings:
            line = WidgetTranslateLines(self, string,bool(self.type=="dialog"))
            self.WidgetLinesLayout.addWidget(line)
            self.lines.append(line)
        self.changeProcess(self.parent.ProcessType)

    def changeProcess(self, value):
        if value:
            self.setFixedHeight(94 * len(self.lines) + 1)
        else:
            self.setFixedHeight(64 * len(self.lines) + 1)

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
            line.loadTranslated(string)


class ListWidgetItem(QtWidgets.QListWidgetItem):
    def __init__(self):
        super().__init__()
        self.num = None


class RightClickEnabledButton(QtWidgets.QPushButton):
    def __init__(self, text=None, name=None, parent=None):
        super().__init__(parent=parent)
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


scrollBarSheet = '''
QScrollBar {background: transparent;width: 4px;margin-top: 132px;margin-bottom: 0;padding-right: 2px;}
QScrollBar {margin-top: 0px;}
QScrollBar::sub-line {background: transparent;}/*隐藏上箭头*/
QScrollBar::add-line {background: transparent;}/*隐藏下箭头*/
QScrollBar::handle {
background: rgb(122, 122, 122);border: 2px solid rgb(128, 128, 128);border-radius: 1px;min-height: 32px;
}
QScrollBar::add-page:vertical,QScrollBar::sub-page:vertical {background: none;}

background: transparent;
border:None;
'''


class TranslateWidget(Ui_Translate, QtWidgets.QWidget):
    type_signal = Signal(int)
    change_signal = Signal()

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
        self.horizontalLayout_5.addWidget(self.ButtonSave)

        self.ButtonSave.clicked.connect(self.save_file_yaml)
        self.ButtonSave.rightClicked.connect(self.save_file_txt)
        self.setAcceptDrops(True)

        self.RadioTrans.setChecked(True)
        self._ProcessType = 0

        self.RadioTrans.clicked.connect(self.changeProcess)
        self.RadioCheck.clicked.connect(self.changeProcess)
        self.RadioProof.clicked.connect(self.changeProcess)

        self.EditTitle.setValidator(QtGui.QRegularExpressionValidator(
            # r'(?!((^(con|CON)$)|^(con|CON)/..*|(^(prn|PRN)$)|^(prn|PRN)/..*|(^(aux|AUX)$)|^(aux|AUX)/..*|'
            # r'(^(nul|NUL)$)|^(nul|NUL)/..*|(^(com|COM)[1-9]$)|^(com|COM)[1-9]/..*|'
            # r'(^(lpt|LPT)[1-9]$)|^(lpt|LPT)[1-9]/..*)|^\s+|.*\s$)'
            '^[^:*?"<>|/\\]{0,255}$'))
        self.Timer = QtCore.QTimer()
        self.Timer.start()
        self.Timer.setInterval(1000)
        self.Timer.timerEvent = self.AutoSave
        self.change_signal.connect(self.AutoSaveChange)
        self.autoSavePath = os.path.join(os.path.expanduser('~/Documents'), "SekaiSubtitle", "AutoSave")

        self.ScrollContentsLayout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        self.ScrollContentsLayout.setSpacing(2)
        # self.ScrollContents.setStyleSheet(scrollBarSheet)

    def AutoSaveChange(self):
        filename = f"[AutoSave]{self.filePrefix}" \
                 f"{self.EditTitle.text() or os.path.splitext(os.path.split(self.data_file)[-1])[0]}.yml"

        result = self.write_yml(os.path.join(os.path.split(self.data_file)[0], filename), check=True)
        if result:
            timer = QtCore.QTimer()
            self.AutoSaveLabel.setText("已自动保存到数据文件目录")
            timer.singleShot(5000, lambda: self.AutoSaveLabel.setText(""))

    def AutoSave(self, _):
        if self.data_file:
            self.Timer.setInterval(int(1000 * 60 * self.parent.FormSettingWidget.get_config('translate_save_interval')))
            os.makedirs(self.autoSavePath, exist_ok=True)
            prefix = f"[AutoSave]{self.filePrefix}" \
                     f"{self.EditTitle.text() or os.path.splitext(os.path.split(self.data_file)[-1])[0]}"
            time_str = datetime.datetime.now().strftime("%y%m%d-%H%M")

            while True:
                exists = sorted([file for file in os.listdir(self.autoSavePath) if file.startswith(prefix)])
                if len(exists) < 10:
                    break
                else:
                    fn = exists.pop(0)
                    os.remove(os.path.join(self.autoSavePath, fn))

            filename = f"{prefix}_{time_str}.yml"
            result = self.write_yml(os.path.join(self.autoSavePath, filename), check=True)
            if result:
                timer = QtCore.QTimer()
                self.AutoSaveLabel.setText("已自动保存到‘文档/SekaiSubtitle/AutoSave’")
                timer.singleShot(5000, lambda: self.AutoSaveLabel.setText(""))
        else:
            self.Timer.setInterval(1000)

    @property
    def ProcessType(self):
        return self._ProcessType

    @ProcessType.setter
    def ProcessType(self, value: int):
        self._ProcessType = value
        self.type_signal.emit(value)

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
                filter=f"剧情数据文件 (*.json;*.asset);;全部文件 (*.*)")
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
        # while self.ListWidgetLine.count():
        #     self.ListWidgetLine.removeItemWidget(self.ListWidgetLine.takeItem(0))
        for line in self.lines:
            self.ScrollContentsLayout.removeWidget(line)
            line.deleteLater()
        self.lines.clear()
        self.data_file = None
        self.data = None
        self.AutoSave(None)

    def newItem(self, data, item_id):
        line = WidgetTranslateItem(self, data, item_id + 1)
        if line.data.get("TalkCharacters"):
            cid = line.data.get("TalkCharacters")[0].get("Character2dId")
            for c in self.data['AppearCharacters']:
                if c['Character2dId'] == cid:
                    if c['CostumeType'][:2].isdigit():
                        chara_id = str(int(c['CostumeType'][:2]))
                        icon_path = get_asset_path(f'icon/chr_{chara_id}.png')
                        if os.path.exists(icon_path):
                            line.CharaWidget.LabelIcon.setPixmap(
                                QtGui.QPixmap(icon_path).scaledToWidth(
                                    50, QtCore.Qt.TransformationMode.SmoothTransformation))

        self.lines.append(line)
        self.ScrollContentsLayout.addWidget(line)

    @property
    def filePrefix(self):
        return f"【{'翻译' if not self.ProcessType else '校对' if self.ProcessType == 1 else '合意'}】"

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
            path = os.path.split(self.trans_file)[0] \
                if self.trans_file else os.path.split(self.data_file)[0] or self.parent.choose_file_root
            filename = QtWidgets.QFileDialog.getSaveFileName(
                self, "保存", dir=os.path.join(path, f"{self.filePrefix}{self.EditTitle.text()}.txt"),
                filter="SekaiText文件(*.txt)")
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
            path = os.path.split(self.trans_file)[0] \
                if self.trans_file else os.path.split(self.data_file)[0] or self.parent.choose_file_root
            filename = QtWidgets.QFileDialog.getSaveFileName(
                self, "保存", dir=os.path.join(path, f"{self.filePrefix}{self.EditTitle.text()}.yml"),
                filter="SekaiSubtitle翻译文件(*.yml)"
            )
            if filename[0]:
                self.write_yml(filename[0])
                msg = QtWidgets.QMessageBox(
                    icon=QtWidgets.QMessageBox.Icon.NoIcon, text=f"已保存到 {filename[0]}", parent=self
                )
                msg.setWindowTitle("SekaiText")
                msg.exec_()

    def write_yml(self, file, check=False):
        data = {"dialog": [], "tag": [], "banner": []}
        for line in self.lines:
            if line.type in data.keys():
                data[line.type].append(line.translated)
        if check:
            if not "".join(data['dialog'] + data['tag'] + data['banner']).replace(r"\N", "\n").strip():
                return False
        with open(file, 'w', encoding='utf8') as fp:
            fp.write(yaml.dump(data, allow_unicode=True))
        return True

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
                self, "选取文件", dir=os.path.split(self.data_file)[0] if self.data_file else os.getcwd(),
                filter=f"SekaiText文件 (*.txt;*.yml);;全部文件 (*.*)")
        if file_name_choose and os.path.exists(file_name_choose):
            self.trans_file = file_name_choose

            title = os.path.splitext(os.path.split(file_name_choose)[-1])[0].removeprefix("【翻译】").removeprefix(
                "【校对】").removeprefix("【合意】")
            self.EditTitle.setText(title)

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
                            widget.lines[index].loadTranslated(string)
                else:
                    for line_index, lines in enumerate(res):
                        widget = limited_lines[line_index]
                        for index, string in enumerate(lines):
                            widget.lines[index].loadTranslated(string)
            elif os.path.splitext(file_name_choose)[-1].lower() == ".yml":
                with open(file_name_choose, 'r', encoding='utf-8') as fp:
                    data = yaml.load(fp, yaml.Loader)
                for line_type in ["banner", "tag", "dialog"]:
                    index_list = [index for index, line in enumerate(self.lines) if line.type == line_type]
                    index_count = len(index_list)
                    if index_count == len(data[line_type]):
                        for index_of_data, index_of_widget in enumerate(index_list):
                            self.lines[index_of_widget].translated = data[line_type][index_of_data]

    def changeProcess(self):
        if self.RadioTrans.isChecked():
            self.ProcessType = 0
        elif self.RadioProof.isChecked():
            self.ProcessType = 1
        else:
            self.ProcessType = 2

    # Action 1 TalkData
    # Action 2 LayoutData
    # Action 4 LayoutData
    # Action 6 SpecialEffectData
    # Action 7 SoundData
    # Action 8 ScenarioSnippetCharacterLayoutModes
