# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WindowMain.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(640, 480)
        MainWindow.setStyleSheet(u"QWidget#MainFrame{background-color: rgb(255, 255, 255);border-color: rgb(204, 204,\n"
"                204);border-size: 2px;border-radius:20px;}\n"
"                QFrame#CenterFrame{border-radius:20px;background-color: rgb(238, 238, 238);}\n"
"                QFrame#MenuFrame{ border-radius:20px; background-color: rgba(238, 238, 238,128);}\n"
"                #MenuFrame QPushButton{font: 500 14pt \"Microsoft YaHei UI\";border:none}\n"
"            ")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.MainFrame = QWidget(self.centralwidget)
        self.MainFrame.setObjectName(u"MainFrame")
        self.MainFrame.setStyleSheet(u"")
        self.gridLayout_2 = QGridLayout(self.MainFrame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(-1, 40, -1, -1)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.MenuFrame = QFrame(self.MainFrame)
        self.MenuFrame.setObjectName(u"MenuFrame")
        self.MenuFrame.setMinimumSize(QSize(150, 0))
        self.MenuFrame.setMaximumSize(QSize(150, 16777215))
        self.MenuFrame.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(self.MenuFrame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.widget = QWidget(self.MenuFrame)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.FuncButtonSubtitle = QPushButton(self.widget)
        self.FuncButtonSubtitle.setObjectName(u"FuncButtonSubtitle")

        self.horizontalLayout_2.addWidget(self.FuncButtonSubtitle)


        self.verticalLayout_4.addWidget(self.widget)

        self.widget_3 = QWidget(self.MenuFrame)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.FuncButtonDownload = QPushButton(self.widget_3)
        self.FuncButtonDownload.setObjectName(u"FuncButtonDownload")

        self.horizontalLayout_3.addWidget(self.FuncButtonDownload)


        self.verticalLayout_4.addWidget(self.widget_3)

        self.widget_6 = QWidget(self.MenuFrame)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.FuncButtonText = QPushButton(self.widget_6)
        self.FuncButtonText.setObjectName(u"FuncButtonText")

        self.horizontalLayout_7.addWidget(self.FuncButtonText)


        self.verticalLayout_4.addWidget(self.widget_6)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.FigureLabel = QLabel(self.MenuFrame)
        self.FigureLabel.setObjectName(u"FigureLabel")
        self.FigureLabel.setMinimumSize(QSize(130, 130))
        self.FigureLabel.setMaximumSize(QSize(130, 130))
        self.FigureLabel.setLayoutDirection(Qt.LeftToRight)
        self.FigureLabel.setAutoFillBackground(False)
        self.FigureLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.FigureLabel)

        self.widget_5 = QWidget(self.MenuFrame)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.FuncButtonSetting = QPushButton(self.widget_5)
        self.FuncButtonSetting.setObjectName(u"FuncButtonSetting")

        self.horizontalLayout_6.addWidget(self.FuncButtonSetting)

        self.FuncButtonAbout = QPushButton(self.widget_5)
        self.FuncButtonAbout.setObjectName(u"FuncButtonAbout")

        self.horizontalLayout_6.addWidget(self.FuncButtonAbout)


        self.verticalLayout_4.addWidget(self.widget_5)


        self.horizontalLayout.addWidget(self.MenuFrame)

        self.CenterFrame = QFrame(self.MainFrame)
        self.CenterFrame.setObjectName(u"CenterFrame")
        self.CenterFrame.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.CenterFrame)


        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.MainFrame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.FuncButtonSubtitle.setText(QCoreApplication.translate("MainWindow", u"\u81ea\u52a8\u8f74\u673a", None))
        self.FuncButtonDownload.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u4e0b\u8f7d", None))
        self.FuncButtonText.setText(QCoreApplication.translate("MainWindow", u"SekaiText", None))
        self.FigureLabel.setText("")
        self.FuncButtonSetting.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
        self.FuncButtonAbout.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
    # retranslateUi

