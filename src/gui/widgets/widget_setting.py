import os

from PySide6 import QtWidgets
from PySide6.QtGui import QFont

from gui.design.WidgetSetting import Ui_Form
from script.tools import save_json, read_json


class SettingWidget(QtWidgets.QWidget, Ui_Form):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        self.pushButton.clicked.connect(self.change_config)
        self.root = os.path.join(os.getcwd(), "data")
        os.makedirs(self.root, exist_ok=True)
        self.config_file = os.path.join(self.root, "config.json")
        self.load_config()

    def save_config(self):
        proxy = self.SettingProxyEdit.text()
        font: QFont = self.SettingFontComboBox.currentFont()
        start_immediate = self.SettingStartImmediateCheck.isChecked()
        config = {"proxy": proxy, "font": font.toString(), "start_immediate": start_immediate}
        save_json(self.config_file, config)

    def change_config(self):
        self.save_config()
        self.parent.restart()

    def load_config(self):
        config = read_json(self.config_file)
        if "proxy" in config:
            self.SettingProxyEdit.setText(config["proxy"])
        if "font" in config:
            self.SettingFontComboBox.setFont(config["font"])
        if "start_immediate" in config:
            self.SettingStartImmediateCheck.setChecked(config['start_immediate'])

    def get_config(self) -> dict:
        config = read_json(self.config_file)
        return config
