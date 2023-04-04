# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WidgetDataDownload.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_DownloadWidget(object):
    def setupUi(self, DownloadWidget):
        if not DownloadWidget.objectName():
            DownloadWidget.setObjectName(u"DownloadWidget")
        DownloadWidget.resize(575, 377)
        DownloadWidget.setStyleSheet(u"QFrame{background-color:rgb(248, 248, 248);border-color: rgb(204, 204, 204);border-size:2px;border-radius:10px;}\n"
"QFrame#MainFrame{background-color: rgb(255, 255, 255);}\n"
"QPushButton{border: 2px solid grey; border-radius: 10px;}\n"
"QScrollArea{background-color: rgba(255, 255, 255, 204);border: none;outline:0px;}\n"
"#LogScrollAreaContents{background-color: rgb(250,250,250);border: none;border-radius:5px;outline:0px;}\n"
"#LogScrollAreaContents > QFrame{background:transparent;}")
        self.gridLayout = QGridLayout(DownloadWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.MainFrame = QFrame(DownloadWidget)
        self.MainFrame.setObjectName(u"MainFrame")
        self.MainFrame.setFrameShape(QFrame.StyledPanel)
        self.MainFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.MainFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_5 = QFrame(self.MainFrame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.frame_5)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.L0 = QLabel(self.frame)
        self.L0.setObjectName(u"L0")

        self.horizontalLayout.addWidget(self.L0)

        self.DataSourceBox = QComboBox(self.frame)
        self.DataSourceBox.addItem("")
        self.DataSourceBox.addItem("")
        self.DataSourceBox.setObjectName(u"DataSourceBox")

        self.horizontalLayout.addWidget(self.DataSourceBox)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 3)

        self.verticalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(self.frame_5)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.L1 = QLabel(self.frame_2)
        self.L1.setObjectName(u"L1")

        self.horizontalLayout_2.addWidget(self.L1)

        self.DataTypeBox = QComboBox(self.frame_2)
        self.DataTypeBox.setObjectName(u"DataTypeBox")

        self.horizontalLayout_2.addWidget(self.DataTypeBox)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 3)

        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame_5)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.L2 = QLabel(self.frame_3)
        self.L2.setObjectName(u"L2")

        self.horizontalLayout_3.addWidget(self.L2)

        self.DataPeriodBox = QComboBox(self.frame_3)
        self.DataPeriodBox.setObjectName(u"DataPeriodBox")

        self.horizontalLayout_3.addWidget(self.DataPeriodBox)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 3)

        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame_5)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy1)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.L3 = QLabel(self.frame_4)
        self.L3.setObjectName(u"L3")

        self.horizontalLayout_4.addWidget(self.L3)

        self.DataEpisodeBox = QComboBox(self.frame_4)
        self.DataEpisodeBox.setObjectName(u"DataEpisodeBox")

        self.horizontalLayout_4.addWidget(self.DataEpisodeBox)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 3)

        self.verticalLayout_2.addWidget(self.frame_4)


        self.verticalLayout.addWidget(self.frame_5)

        self.LogScrollArea = QScrollArea(self.MainFrame)
        self.LogScrollArea.setObjectName(u"LogScrollArea")
        self.LogScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.LogScrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.LogScrollArea.setWidgetResizable(True)
        self.LogScrollArea.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.LogScrollAreaContents = QWidget()
        self.LogScrollAreaContents.setObjectName(u"LogScrollAreaContents")
        self.LogScrollAreaContents.setGeometry(QRect(0, 0, 557, 133))
        self.LogScrollAreaContentsLayout = QVBoxLayout(self.LogScrollAreaContents)
        self.LogScrollAreaContentsLayout.setObjectName(u"LogScrollAreaContentsLayout")
        self.LogScrollArea.setWidget(self.LogScrollAreaContents)

        self.verticalLayout.addWidget(self.LogScrollArea)

        self.ButtonWidgets = QWidget(self.MainFrame)
        self.ButtonWidgets.setObjectName(u"ButtonWidgets")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.ButtonWidgets.sizePolicy().hasHeightForWidth())
        self.ButtonWidgets.setSizePolicy(sizePolicy2)
        self.horizontalLayout_5 = QHBoxLayout(self.ButtonWidgets)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.RefreshButton = QPushButton(self.ButtonWidgets)
        self.RefreshButton.setObjectName(u"RefreshButton")

        self.horizontalLayout_5.addWidget(self.RefreshButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.DownloadButton = QPushButton(self.ButtonWidgets)
        self.DownloadButton.setObjectName(u"DownloadButton")

        self.horizontalLayout_5.addWidget(self.DownloadButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_5.setStretch(1, 1)
        self.horizontalLayout_5.setStretch(3, 1)

        self.verticalLayout.addWidget(self.ButtonWidgets)


        self.gridLayout.addWidget(self.MainFrame, 0, 0, 1, 1)


        self.retranslateUi(DownloadWidget)

        QMetaObject.connectSlotsByName(DownloadWidget)
    # setupUi

    def retranslateUi(self, DownloadWidget):
        DownloadWidget.setWindowTitle(QCoreApplication.translate("DownloadWidget", u"Form", None))
        self.L0.setText(QCoreApplication.translate("DownloadWidget", u"\u6570\u636e\u6e90", None))
        self.DataSourceBox.setItemText(0, QCoreApplication.translate("DownloadWidget", u"https://sekai.best/", None))
        self.DataSourceBox.setItemText(1, QCoreApplication.translate("DownloadWidget", u"https://pjsek.ai/", None))

        self.L1.setText(QCoreApplication.translate("DownloadWidget", u"\u5267\u60c5\u7c7b\u578b", None))
        self.L2.setText(QCoreApplication.translate("DownloadWidget", u"\u5267\u60c5\u671f\u6570", None))
        self.L3.setText(QCoreApplication.translate("DownloadWidget", u"\u5267\u60c5\u8bdd\u6570", None))
        self.RefreshButton.setText(QCoreApplication.translate("DownloadWidget", u"\u5237\u65b0", None))
        self.DownloadButton.setText(QCoreApplication.translate("DownloadWidget", u"\u5f00\u59cb\u4e0b\u8f7d", None))
    # retranslateUi

