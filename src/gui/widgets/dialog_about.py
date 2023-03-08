import json
import os
import sys

from PySide6 import QtWidgets, QtNetwork, QtCore
from PySide6.QtCore import QUrl, Qt, SIGNAL
from PySide6.QtGui import QIcon, QDesktopServices, QPixmap
from packaging.version import Version

from gui.design.WindowDialogAbout import Ui_Dialog


class AboutDialog(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, parent):
        super().__init__()
        self.isStartup = False
        self.parent = parent
        self.setupUi(self)
        self.setWindowTitle("关于Sekai Subtitle")
        self.iconPath = "asset"
        if getattr(sys, 'frozen', False):
            self.iconPath = os.path.join(sys._MEIPASS, self.iconPath)
        title_icon = os.path.join(self.iconPath, "icon.png")
        if os.path.exists(title_icon):
            self.IconLabel.setPixmap(
                QPixmap(title_icon).scaledToHeight(self.IconLabel.height(), Qt.TransformationMode.SmoothTransformation))
            self.setWindowIcon(QIcon(title_icon))
        group_icon = os.path.join(self.iconPath, "PJS字幕组.png")
        if os.path.exists(title_icon):
            self.GroupLabel.setPixmap(
                QPixmap(group_icon).scaledToHeight(self.GroupLabel.height(),
                                                   Qt.TransformationMode.SmoothTransformation))
        self.CloseButton.clicked.connect(self.close)
        self.PageButton.clicked.connect(self.open_github)
        self.LabelVersion.setText(self.parent.version)
        self.UpdateButton.clicked.connect(self.check_update)
        self.update_nam = QtNetwork.QNetworkAccessManager()
        self.connect(self.update_nam, SIGNAL("finished(QNetworkReply*)"),
                     lambda reply: self.receive_update(reply, self.parent.version))

    def check_update(self):
        self.update_nam.get(QtNetwork.QNetworkRequest(QtCore.QUrl(self.parent.update_url)))

    def receive_update(self, reply: QtNetwork.QNetworkReply, version: str):
        er = reply.error()
        if er == QtNetwork.QNetworkReply.NetworkError.NoError:
            bytes_string = reply.readAll()
            data_string = str(bytes_string, 'utf-8')
            data = json.loads(data_string)
            tag = Version(data['tag_name'])
            now = Version(version)
            if tag > now:
                msg = QtWidgets.QMessageBox.question(
                    self, "检查更新", f"有新版本可用：{tag}\n{data['body']}",
                    QtWidgets.QMessageBox.StandardButton.Yes, QtWidgets.QMessageBox.StandardButton.No,
                )
                if msg == QtWidgets.QMessageBox.StandardButton.Yes:
                    QDesktopServices.openUrl(QUrl(data['html_url']))
            else:
                QtWidgets.QMessageBox.information(self, "检查更新", "暂无新版本")
        else:
            QtWidgets.QMessageBox.critical(self, "检查更新", f"检查版本更新时遇到错误\n{reply.errorString()}")

    def open_github(self):
        QDesktopServices.openUrl(QUrl(self.LabelPage.text()))
