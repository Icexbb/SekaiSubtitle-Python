import os
import re
import shutil
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
        self.root = os.path.join(os.path.expanduser('~/Documents'), "SekaiSubtitle", "setting")
        os.makedirs(self.root, exist_ok=True)
        self.config_file = os.path.join(self.root, "config.json")
        if not os.path.exists(self.config_file):
            old_file = os.path.join(os.path.expanduser('~'), "SekaiSubtitle", "setting", "config.json")
            if os.path.exists(old_file):
                shutil.move(old_file, self.config_file)
                shutil.rmtree(os.path.join(os.path.expanduser('~'), "SekaiSubtitle"))
        self.SettingProxyEdit.setValidator(
            QtGui.QRegularExpressionValidator(QtCore.QRegularExpression(
                r"([a-zA-Z0-9][-a-zA-Z0-9]{0,62}(\.[a-zA-Z0-9][-a-zA-Z0-9]{0,62})+\.?)|"
                r"((25[0-5])|(2[0-4]\d)|(1\d\d)|([1-9]\d)|\d)(\.((25[0-5])|(2[0-4]\d)|(1\d\d)|([1-9]\d)|\d)){3}")))
        self.SettingProxyTypeCombo.currentTextChanged.connect(self.setProxyState)
        self._last_dir = None
        try:
            self.load_config()
        except Exception as e:
            os.remove(self.config_file)
            self.load_config()
            QtWidgets.QMessageBox.warning(
                self, "载入错误", f"在载入设置文件时发生错误，已恢复默认设置，请检查设置内容:\n{e.__repr__()}",
                QtWidgets.QMessageBox.StandardButton.Ok)
        # self.SettingAnimatedCheck.setChecked(False)
        # self.SettingAnimatedCheck.setEnabled(False)
        self.save_config()
        self.setProxyState()
        self.scrollArea.setVerticalScrollBarPolicy(QtGui.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

    @property
    def last_dir(self):
        return self._last_dir

    @last_dir.setter
    def last_dir(self, value):
        self._last_dir = value
        self.save_config()

    def setProxyState(self):
        self.SettingProxyHostSpin.setHidden(not self.SettingProxyTypeCombo.currentIndex())
        self.SettingProxyEdit.setHidden(not self.SettingProxyTypeCombo.currentIndex())
        self.SettingProxyLabel.setHidden(not self.SettingProxyTypeCombo.currentIndex())

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
        if value:
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
        else:
            self.SettingProxyTypeCombo.setCurrentIndex(0)

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
        typer_interval = self.SettingTyperIntervalSpin.value()
        typer_fade_interval = self.SettingTyperFadeSpin.value()
        download_timeout = self.SettingTimeoutSpin.value()
        translate_save_interval = self.SettingSaveSpin.value()
        config = {
            "proxy": proxy, "font": font.toString(), "start_immediate": start_immediate, "chibi": chibi,
            "animated": animated, "update": update, "last_dir": self.last_dir,
            "adjust_window": adjust_window, "typer_interval": typer_interval,
            "typer_fade_interval": typer_fade_interval, "download_timeout": download_timeout,
            "translate_save_interval": translate_save_interval
        }
        save_json(self.config_file, config)

    def change_config(self):
        self.save_config()
        self.parent.restart()

    def load_config(self):
        config = read_json(self.config_file)
        try:
            self.proxy = config.get("proxy")
        except ValueError:
            QtWidgets.QMessageBox.warning(self, "Sekai Subtitle", "代理格式错误 请重新设置！",
                                          QtWidgets.QMessageBox.StandardButton.Yes,
                                          QtWidgets.QMessageBox.StandardButton.Yes)
        if "font" in config:
            self.SettingFontComboBox.setCurrentFont(QFont(config["font"]))
        if "chibi" in config:
            self.SettingChibiSelect.setCurrentText(config.get('chibi'))
        else:
            self.SettingChibiSelect.setCurrentIndex(0)
        if "update" in config:
            self.SettingStartupUpdateCheck.setChecked(bool(config['update']))
        else:
            self.SettingStartupUpdateCheck.setChecked(True)
        self.SettingStartImmediateCheck.setChecked(bool(config.get('start_immediate')))
        self.SettingAnimatedCheck.setChecked(bool(config.get('animated')))
        self.last_dir = config.get('last_dir') or os.getcwd()
        self.SettingStartAdjustWindowCheck.setChecked(bool(config.get("adjust_window")))
        self.SettingTyperIntervalSpin.setValue(config.get("typer_interval") or 80)
        self.SettingTyperFadeSpin.setValue(config.get('typer_fade_interval') or 50)
        self.SettingTimeoutSpin.setValue(config.get("download_timeout") or 0)
        self.SettingSaveSpin.setValue(config.get("translate_save_interval") or 5)

    def get_config(self, config_field=None) -> dict | str:
        config = read_json(self.config_file)
        if config_field:
            return config.get(config_field)
        else:
            return config
