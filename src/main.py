# -*- coding: utf-8 -*-
import sys

from PySide6 import QtWidgets, QtGui

from gui.gui_main import handleException, MainUi, EXIT_CODE_REBOOT
from script.data import get_asset_path


def start_gui(st: int = 0):
    try:
        app = QtWidgets.QApplication(sys.argv)
    except RuntimeError:
        app = QtWidgets.QApplication.instance()
    if not st:
        splash = QtWidgets.QSplashScreen(QtGui.QPixmap(get_asset_path("icon.png")))
        splash.show()
    else:
        splash = None
    window = MainUi()
    window.show()
    if splash:
        splash.finish(window)
    exit_code = app.exec()
    if exit_code == EXIT_CODE_REBOOT:
        start_gui(st + 1)


if __name__ == '__main__':
    sys.excepthook = handleException
    start_gui()
