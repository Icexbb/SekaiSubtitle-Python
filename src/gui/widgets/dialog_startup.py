import os
import sys

from PySide6 import QtGui, QtCore
from PySide6.QtWidgets import QDialog
from gui.design.WindowDialogStartup import Ui_Dialog


class StartUpDialog(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.iconPath = "asset"

        if getattr(sys, 'frozen', False):
            self.iconPath = os.path.join(sys._MEIPASS, self.iconPath)
        icon = os.path.join(self.iconPath, "icon.png")
        self.IconLabel.setPixmap(
            QtGui.QPixmap(icon).scaledToHeight(
                self.IconLabel.height(), QtCore.Qt.TransformationMode.SmoothTransformation)
        )
