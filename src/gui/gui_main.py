import datetime
import json
import os
import platform
import random
import sys
import traceback

from PySide6 import QtWidgets, QtCore, QtGui, QtNetwork
from PySide6.QtCore import QUrl, SIGNAL
from PySide6.QtGui import QIcon, QFont, QMovie, QDesktopServices
from packaging.version import Version
from qframelesswindow import FramelessMainWindow

from gui.design.WindowMain import Ui_MainWindow
from gui.widgets.dialog_about import AboutDialog
from gui.widgets.widget_download import DownloadWidget
from gui.widgets.widget_setting import SettingWidget
from gui.widgets.widget_subtitle import ProcessWidget
from gui.widgets.widget_titlebar import TitleBar
from gui.widgets.widget_translate import TranslateWidget

EXIT_CODE_REBOOT = -11231351

PROGRAM_NAME = "Sekai Subtitle"
VERSION = "v0.5.0"


class MainUi(FramelessMainWindow, Ui_MainWindow):
    _startPos = None
    _endPos = None
    _isTracking = None

    def __init__(self):
        super().__init__()
        self.icon = None
        self.version = VERSION
        self.setupUi(self)
        self.setWindowTitle(PROGRAM_NAME)
        self.setObjectName(PROGRAM_NAME)

        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)

        self.FormSettingWidget = SettingWidget(self)
        self.FormProcessWidget = ProcessWidget(self)
        self.FormDownloadWidget = DownloadWidget(self)
        self.FormTranslateWidget = TranslateWidget(self)
        self.MainLayout = QtWidgets.QStackedLayout()
        self.CenterFrame.setLayout(self.MainLayout)
        self.MainLayout.addWidget(self.FormProcessWidget)
        self.MainLayout.addWidget(self.FormDownloadWidget)
        self.MainLayout.addWidget(self.FormTranslateWidget)
        self.MainLayout.addWidget(self.FormSettingWidget)

        self.load_icon()
        self.load_random_chibi()

        self.TitleBar = TitleBar(self)
        self.TitleBar.TitleLabel.setText(PROGRAM_NAME)
        self.setTitleBar(self.TitleBar)
        self.FuncButtonSubtitle.clicked.connect(lambda: self.switchWidget(0, QtCore.QSize(650, 450)))
        self.FuncButtonDownload.clicked.connect(lambda: self.switchWidget(1, QtCore.QSize(650, 450)))
        self.FuncButtonText.clicked.connect(lambda: self.switchWidget(2, QtCore.QSize(1280, 720)))
        self.FuncButtonSetting.clicked.connect(lambda: self.switchWidget(3, QtCore.QSize(650, 450)))
        self.FuncButtonAbout.clicked.connect(self.AboutWindow)
        self.switchWidget(0, QtCore.QSize(650, 450))

        if self.FormSettingWidget.get_config("update"):
            self.update_url = "https://api.github.com/repos/Icexbb/SekaiSubtitle-Python/releases/latest"
            self.update_nam = QtNetwork.QNetworkAccessManager()
            self.connect(self.update_nam, SIGNAL("finished(QNetworkReply*)"), self.receive_update)
            self.check_update()

    def check_update(self):
        self.update_nam.get(QtNetwork.QNetworkRequest(QtCore.QUrl(self.update_url)))

    def receive_update(self, reply: QtNetwork.QNetworkReply):
        er = reply.error()
        if er == QtNetwork.QNetworkReply.NetworkError.NoError:
            bytes_string = reply.readAll()
            data_string = str(bytes_string, 'utf-8')
            data = json.loads(data_string)
            tag = Version(data['tag_name'])
            now = Version(self.version)
            if tag > now:
                msg = QtWidgets.QMessageBox.question(
                    self, "检查更新", f"有新版本可用：{tag}\n{data['body']}",
                    QtWidgets.QMessageBox.StandardButton.Yes, QtWidgets.QMessageBox.StandardButton.No,
                )
                if msg == QtWidgets.QMessageBox.StandardButton.Yes:
                    QDesktopServices.openUrl(QUrl(data['html_url']))
        else:
            QtWidgets.QMessageBox.critical(self, "检查更新", f"检查版本更新时遇到错误\n{reply.errorString()}")

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
            self.FigureLabel.setText("")
            raise e

    def load_icon(self):
        icon_path = "asset"
        if getattr(sys, 'frozen', False):
            icon_path = os.path.join(sys._MEIPASS, icon_path)
        if platform.system() == "Darwin":
            title_icon = os.path.join(icon_path, "icon.icns")
        else:
            title_icon = os.path.join(icon_path, "icon.ico")
        self.icon = title_icon
        if os.path.exists(title_icon):
            self.setWindowIcon(QIcon(title_icon))

    def AboutWindow(self):
        dia = AboutDialog(self)
        dia.exec_()

    def switchWidget(self, index: int, size: QtCore.QSize):
        self.MainLayout.setCurrentIndex(index)
        if self.adjust_window:
            self.resize(size)
            self.center()

    def center(self):
        cp = QtGui.QGuiApplication.primaryScreen().geometry().center()
        size = self.geometry()
        self.move((cp.x() - size.width() / 2), (cp.y() - size.height() / 2))

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

    @property
    def max_ram(self):
        return int(self.FormSettingWidget.get_config()["ram"])

    @property
    def choose_file_root(self):
        return str(self.FormSettingWidget.get_config()["last_dir"])

    @property
    def adjust_window(self):
        return bool(self.FormSettingWidget.get_config()["adjust_window"])

    @choose_file_root.setter
    def choose_file_root(self, value: str):
        self.FormSettingWidget.last_dir = value

    def restart(self):
        # qDebug("Performing application reboot...")
        self.close()
        QtWidgets.QApplication.exit(EXIT_CODE_REBOOT)


def handleException(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        return sys.__excepthook__(exc_type, exc_value, exc_traceback)
    exception = str("".join(traceback.format_exception(exc_type, exc_value, exc_traceback)))
    dialog = QtWidgets.QDialog()
    os.makedirs("data/log", exist_ok=True)
    filename = os.path.realpath(f"data/log/Exception-{datetime.datetime.now().strftime('%Y-%m-%d-%H:%M:%S')}.txt")
    with open(filename, 'w', encoding="utf-8") as fp:
        fp.write(exception)
    dialog.setAttribute(QtCore.Qt.WidgetAttribute.WA_DeleteOnClose)
    msg = QtWidgets.QMessageBox(dialog)
    msg.setIcon(QtWidgets.QMessageBox.Icon.Critical)
    msg.setText(f'程序异常,请将{filename}发送给开发者')
    msg.setWindowTitle(PROGRAM_NAME)
    msg.setDetailedText(exception)
    msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)

    msg.exec_()


def start_gui():
    start_time = 0
    try:
        QtWidgets.QApplication.setAttribute(QtCore.Qt.ApplicationAttribute.AA_EnableHighDpiScaling, True)
        QtWidgets.QApplication.setAttribute(QtCore.Qt.ApplicationAttribute.AA_UseHighDpiPixmaps, True)
    except AttributeError:
        pass
    icon_path = "asset"
    if getattr(sys, 'frozen', False):
        icon_path = os.path.join(sys._MEIPASS, icon_path)
    splash = None
    while True:
        try:
            app = QtWidgets.QApplication(sys.argv)
        except RuntimeError:
            app = QtWidgets.QApplication.instance()
        sys.excepthook = handleException
        if not start_time:
            splash = QtWidgets.QSplashScreen(QtGui.QPixmap(os.path.join(icon_path, "icon.png")))
            splash.show()
        window = MainUi()
        window.show()
        if not start_time and splash:
            splash.finish(window)
            splash = None
        exit_code = app.exec_()
        start_time += 1
        if exit_code != EXIT_CODE_REBOOT:
            break
