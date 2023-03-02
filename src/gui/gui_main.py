import os
import platform
import random
import sys

from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtGui import QIcon, QFont, QMovie
from qframelesswindow import FramelessMainWindow

from gui.design.WindowMain import Ui_MainWindow
from gui.widgets.dialog_about import AboutDialog
from gui.widgets.widget_download import DownloadWidget
from gui.widgets.widget_setting import SettingWidget
from gui.widgets.widget_subtitle import ProcessWidget
from gui.widgets.widget_titlebar import TitleBar

EXIT_CODE_REBOOT = -11231351


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

        self.FormProcessWidget = ProcessWidget(self)
        self.FormSettingWidget = SettingWidget(self)
        self.FormDownloadWidget = DownloadWidget(self)
        self.MainLayout = QtWidgets.QStackedLayout()
        self.CenterFrame.setLayout(self.MainLayout)
        self.MainLayout.addWidget(self.FormProcessWidget)
        self.MainLayout.addWidget(self.FormDownloadWidget)
        self.MainLayout.addWidget(self.FormSettingWidget)

        self.load_icon()
        self.load_random_chibi()

        self.TitleBar = TitleBar(self)
        self.TitleBar.TitleLabel.setText("SekaiSubtitle Alpha")
        self.setTitleBar(self.TitleBar)
        self.FuncButtonSubtitle.clicked.connect(self.switchToSubtitle)
        self.FuncButtonText.clicked.connect(self.NotCompleteWarning)
        self.FuncButtonDownload.clicked.connect(self.switchToDownload)
        self.FuncButtonSetting.clicked.connect(self.switchToSetting)
        self.FuncButtonAbout.clicked.connect(self.AboutWindow)
        self.switchToSubtitle()

    def load_random_chibi(self):
        icon_path = "asset"
        if getattr(sys, 'frozen', False):
            icon_path = os.path.join(sys._MEIPASS, icon_path)
        try:
            select = self.FormSettingWidget.get_config("chibi")
            animated = self.FormSettingWidget.get_config("animated")

            if select == "随机":
                if animated:
                    root = os.path.join(icon_path + "/chibi_gif/")
                    chara = random.choice(os.listdir(root))
                    cloth = random.choice(os.listdir(os.path.join(root, chara)))
                    motion = random.choice(os.listdir(os.path.join(root, chara, cloth)))
                    i = os.path.join(root, chara, cloth, motion)
                else:
                    i = os.path.join(icon_path + "/chibi/" + random.choice(os.listdir(icon_path + "/chibi")))
            else:
                if animated:
                    root = os.path.join(icon_path + "/chibi_gif/")
                    chara = select
                    cloth = random.choice(os.listdir(os.path.join(root, chara)))
                    motion = random.choice(os.listdir(os.path.join(root, chara, cloth)))
                    i = os.path.join(root, chara, cloth, motion)
                else:
                    i = os.path.join(icon_path + f"/chibi/{select}.png")
                    if not os.path.exists(i):
                        i = os.path.join(icon_path + "/chibi/" + random.choice(os.listdir(icon_path + "/chibi")))
            if animated:
                movie = QMovie(i)
                movie.setCacheMode(QtGui.QMovie.CacheMode.CacheAll)
                movie.setScaledSize(self.FigureLabel.size())
                movie.start()
                self.FigureLabel.setMovie(movie)
            else:
                self.FigureLabel.setPixmap(
                    QtGui.QPixmap(i).scaledToHeight(self.FigureLabel.height(),
                                                    QtCore.Qt.TransformationMode.SmoothTransformation))
        except BaseException as e:
            print(e)
            self.FigureLabel.setText("")

    def load_icon(self):
        icon_path = "asset"
        if getattr(sys, 'frozen', False):
            icon_path = os.path.join(sys._MEIPASS, icon_path)
        if platform.system() == "Darwin":
            title_icon = os.path.join(icon_path, "icon.icns")
        else:
            title_icon = os.path.join(icon_path, "icon.ico")
        if os.path.exists(title_icon):
            self.setWindowIcon(QIcon(title_icon))

    def AboutWindow(self):
        dia = AboutDialog()
        dia.exec_()

    def switchToSubtitle(self):
        self.MainLayout.setCurrentIndex(0)

    def switchToDownload(self):
        self.MainLayout.setCurrentIndex(1)

    def switchToSetting(self):
        self.MainLayout.setCurrentIndex(2)

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

    def NotCompleteWarning(self):
        QtWidgets.QMessageBox.warning(
            self, "错误", "模块暂未完成，敬请期待",
            QtWidgets.QMessageBox.StandardButton.Yes, QtWidgets.QMessageBox.StandardButton.Yes
        )

    @property
    def proxy(self):
        return self.FormSettingWidget.get_config()["proxy"]

    @property
    def immediate_start(self):
        return self.FormSettingWidget.get_config()["start_immediate"]

    @property
    def font(self):
        return QFont(self.FormSettingWidget.get_config()["font"]).family()

    def restart(self):
        # qDebug("Performing application reboot...")
        self.close()
        QtWidgets.QApplication.exit(EXIT_CODE_REBOOT)


def start_gui():
    start_time = 0
    if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
    while True:
        try:
            app = QtWidgets.QApplication(sys.argv)
        except RuntimeError:
            app = QtWidgets.QApplication.instance()
        if not start_time:
            splash = QtWidgets.QSplashScreen(QtGui.QPixmap("asset/icon.png"))
            splash.show()
        window = MainUi()
        window.show()
        if not start_time:
            splash.finish(window)
        exit_code = app.exec_()
        start_time += 1
        if exit_code != EXIT_CODE_REBOOT:
            break


if __name__ == '__main__':
    start_gui()
