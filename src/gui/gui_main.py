import sys

from PySide6 import QtWidgets, QtCore, QtGui
from qframelesswindow import FramelessMainWindow

from gui.widgets.qt_main import Ui_MainWindow
from gui.widgets.widget_subtitleProcess import ProcessWidget
from gui.widgets.widget_titlebar import TitleBar


class MainUi(FramelessMainWindow, Ui_MainWindow):
    _startPos = None
    _endPos = None
    _isTracking = None

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Sekai Subtitle")
        self.setObjectName("Sekai Subtitle")

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.FormProcessWidget = ProcessWidget(self.ProcessFrame)
        self.ProcessGridLayout.addWidget(self.FormProcessWidget, 0, 0, 1, 1)
        self.TitleBar = TitleBar(self)
        self.TitleBar.TitleLabel.setText("SekaiSubtitle Python Alpha")
        self.setTitleBar(self.TitleBar)
        self.FuncButtonText.clicked.connect(self.NotCompleteWarning)
        self.FuncButtonDownload.clicked.connect(self.NotCompleteWarning)
        self.FuncButtonSetting.clicked.connect(self.NotCompleteWarning)

    # 鼠标移动事件
    def mouseMoveEvent(self, a0: QtGui.QMouseEvent):
        if self._startPos:
            self._endPos = a0.position() - self._startPos
            # 移动窗口
            self.move(self.pos() + self._endPos.toPoint())

    # 鼠标按下事件
    def mousePressEvent(self, a0: QtGui.QMouseEvent):
        # 根据鼠标按下时的位置判断是否在QFrame范围内
        if self.childAt(a0.position().x(), a0.position().y()).objectName() in ["MainFrame", "TitleBar", "TitleLabel"]:
            # 判断鼠标按下的是左键
            if a0.button() == QtCore.Qt.MouseButton.LeftButton:
                self._isTracking = True
                # 记录初始位置
                self._startPos = QtCore.QPoint(a0.position().x(), a0.position().y())

    # 鼠标松开事件
    def mouseReleaseEvent(self, a0: QtGui.QMouseEvent):
        if a0.button() == QtCore.Qt.MouseButton.LeftButton:
            self._isTracking = False
            self._startPos = None
            self._endPos = None

    # 鼠标双击事件
    def mouseDoubleClickEvent(self, a0: QtGui.QMouseEvent):
        if self.childAt(a0.position().x(), a0.position().y()).objectName() == "MainFrame":
            if a0.button() == QtCore.Qt.LeftButton:
                self.maxOrNormal()

    def NotCompleteWarning(self):
        QtWidgets.QMessageBox.warning(
            self, "错误", "模块暂未完成，敬请期待", QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.Yes
        )


def start_gui():
    app = QtWidgets.QApplication(sys.argv)
    main_ui = MainUi()
    main_ui.show()
    app.exec()


if __name__ == '__main__':
    start_gui()
