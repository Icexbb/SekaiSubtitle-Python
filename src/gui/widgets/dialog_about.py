import os
import sys

from PySide6 import QtWidgets
from PySide6.QtCore import QUrl
from PySide6.QtGui import QIcon, QDesktopServices, QPixmap

from gui.design.WindowDialogAbout import Ui_Dialog


class AboutDialog(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("关于Sekai Subtitle")
        self.iconPath = "asset"
        if getattr(sys, 'frozen', False):
            self.iconPath = os.path.join(sys._MEIPASS, self.iconPath)
        titleIcon = os.path.join(self.iconPath, "icon.png")
        if os.path.exists(titleIcon):
            self.IconLabel.setPixmap(QPixmap(titleIcon).scaledToHeight(self.IconLabel.height()))
            self.setWindowIcon(QIcon(titleIcon))
        GroupIcon = os.path.join(self.iconPath, "PJS字幕组.png")
        if os.path.exists(titleIcon):
            self.GroupLabel.setPixmap(QPixmap(GroupIcon).scaledToHeight(self.GroupLabel.height()))
        self.CloseButton.clicked.connect(self.close)
        self.PageButton.clicked.connect(self.openGithub)

    def openGithub(self):
        QDesktopServices.openUrl(QUrl("https://github.com/Icexbb/SekaiSubtitle-Python"))
