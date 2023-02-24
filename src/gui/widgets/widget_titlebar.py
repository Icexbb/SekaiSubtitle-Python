from PySide6 import QtCore, QtWidgets, QtGui

from gui.design.WidgetTitleBar import Ui_TitleBar as Bar


class TitleBar(Bar, QtWidgets.QWidget):

    def __init__(self, parent: QtWidgets.QMainWindow | QtWidgets.QDialog):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        self.WindowMinButton.clicked.connect(self.parent.showMinimized)
        self.WindowMaxButton.clicked.connect(self.maxOrNormal)
        self.WindowCloseButton.clicked.connect(self.queryExit)
        # 切换最大化与正常大小

    def maxOrNormal(self):
        if self.parent.isMaximized():
            self.parent.showNormal()
        else:
            self.parent.showMaximized()

    # 弹出警告提示窗口确认是否要关闭
    def queryExit(self):
        self.parent.close()

    def mouseDoubleClickEvent(self, a0: QtGui.QMouseEvent):  # 鼠标双击事件
        if a0.button() == QtCore.Qt.MouseButton.LeftButton:
            self.maxOrNormal()
