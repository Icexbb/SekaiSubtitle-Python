import os
import re
import sys

from PySide6 import QtWidgets, QtGui, QtCore
from PySide6.QtGui import QFont

from gui.design.WidgetSetting import Ui_Form
from script.tools import save_json, read_json


class SettingWidget(QtWidgets.QWidget, Ui_Form):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        self.load_chibi()
        self.pushButton.clicked.connect(self.change_config)
        self.root = os.path.join(os.path.expanduser('~'), "SekaiSubtitle", "setting")
        os.makedirs(self.root, exist_ok=True)
        self.config_file = os.path.join(self.root, "config.json")
        self.SettingProxyEdit.setValidator(
            QtGui.QRegularExpressionValidator(QtCore.QRegularExpression(
                r"([a-zA-Z0-9][-a-zA-Z0-9]{0,62}(\.[a-zA-Z0-9][-a-zA-Z0-9]{0,62})+\.?)|"
                r"((25[0-5])|(2[0-4]\d)|(1\d\d)|([1-9]\d)|\d)(\.((25[0-5])|(2[0-4]\d)|(1\d\d)|([1-9]\d)|\d)){3}")))
        self.SettingProxyTypeCombo.currentTextChanged.connect(self.setProxyState)
        self._last_dir = None
        self.load_config()
        self.SettingAnimatedCheck.setChecked(False)
        self.SettingAnimatedCheck.setEnabled(False)
        self.save_config()

    @property
    def last_dir(self):
        return self._last_dir

    @last_dir.setter
    def last_dir(self, value):
        self._last_dir = value
        self.save_config()

    def setProxyState(self):
        self.SettingProxyHostSpin.setEnabled(self.SettingProxyTypeCombo.currentIndex())
        self.SettingProxyEdit.setEnabled(self.SettingProxyTypeCombo.currentIndex())

    @property
    def proxy(self):
        if self.SettingProxyTypeCombo.currentIndex() == 0:
            return None
        p_type = self.SettingProxyTypeCombo.currentText()
        p_host = self.SettingProxyEdit.text()
        p_port = self.SettingProxyHostSpin.value()
        proxy = f"{p_type}{p_host}:{p_port}"
        return proxy

    @proxy.setter
    def proxy(self, value):
        s = re.match(r'(?P<type>socks5:\/\/|http:\/\/)'
                     r'(?P<host>(([a-zA-Z0-9][-a-zA-Z0-9]{0,62}(\.[a-zA-Z0-9][-a-zA-Z0-9]{0,62})+\.?)|'
                     r'((25[0-5])|(2[0-4]\d)|(1\d\d)|([1-9]\d)|\d)(\.((25[0-5])|(2[0-4]\d)|(1\d\d)|([1-9]\d)|\d)){3}))'
                     r':(?P<port>\d{1,5})', value)
        if s:
            p_port = int(s.group("port"))
            p_host = s.group("host")
            p_type = s.group('type')
            self.SettingProxyEdit.setText(p_host)
            self.SettingProxyHostSpin.setValue(p_port)
            self.SettingProxyTypeCombo.setCurrentText(p_type)
        else:
            raise ValueError("Proxy Not Match Pattern")

    def load_chibi(self):
        icon_path = "asset/chibi"
        if getattr(sys, 'frozen', False):
            icon_path = os.path.join(sys._MEIPASS, icon_path)
        list_chibi = [chibi.removesuffix(".png") for chibi in os.listdir(icon_path)]
        self.SettingChibiSelect.addItem("随机")
        for chibi in list_chibi:
            self.SettingChibiSelect.addItem(chibi)

    def save_config(self):
        proxy = self.proxy
        font: QFont = self.SettingFontComboBox.currentFont()
        start_immediate = self.SettingStartImmediateCheck.isChecked()
        chibi = self.SettingChibiSelect.currentText()
        animated = self.SettingAnimatedCheck.isChecked()
        update = self.SettingStartupUpdateCheck.isChecked()
        adjust_window = self.SettingStartAdjustWindowCheck.isChecked()
        typer_interval = self.SettingTyperSpin.value()
        config = {
            "proxy": proxy, "font": font.toString(), "start_immediate": start_immediate, "chibi": chibi,
            "animated": animated, "update": update, "last_dir": self.last_dir,
            "adjust_window": adjust_window, "typer_interval": typer_interval
        }
        save_json(self.config_file, config)

    def change_config(self):
        self.save_config()
        self.parent.restart()

    def load_config(self):
        config = read_json(self.config_file)
        if "proxy" in config:
            self.proxy = config["proxy"]
        if "font" in config:
            self.SettingFontComboBox.setFont(config["font"])
        if "start_immediate" in config:
            self.SettingStartImmediateCheck.setChecked(config['start_immediate'])
        if "chibi" in config:
            self.SettingChibiSelect.setCurrentText(config['chibi'])
        else:
            self.SettingChibiSelect.setCurrentIndex(0)
        if "animated" in config:
            self.SettingAnimatedCheck.setChecked(config['animated'])
        if "update" in config:
            self.SettingStartupUpdateCheck.setChecked(config['update'])
        else:
            self.SettingStartupUpdateCheck.setChecked(True)
        if "last_dir" in config:
            self.last_dir = config['last_dir']
        else:
            self.last_dir = os.getcwd()
        if "adjust_window" in config:
            self.SettingStartAdjustWindowCheck.setChecked(config["adjust_window"])
        else:
            self.SettingStartAdjustWindowCheck.setChecked(True)
        if "typer_interval" in config:
            self.SettingTyperSpin.setValue(config["typer_interval"])

    def get_config(self, config_field=None) -> dict | str:
        config = read_json(self.config_file)
        if config_field:
            return config.get(config_field)
        else:
            return config
