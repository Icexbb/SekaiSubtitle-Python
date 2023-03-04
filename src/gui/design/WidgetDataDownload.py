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
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_DownloadWidget(object):
    def setupUi(self, DownloadWidget):
        if not DownloadWidget.objectName():
            DownloadWidget.setObjectName(u"DownloadWidget")
        DownloadWidget.resize(653, 377)
        DownloadWidget.setStyleSheet(u"QFrame{background-color:rgb(248, 248, 248);border-color: rgb(204, 204, 204);border-size: 2px;border-radius:20px;}\n"
"QFrame#MainFrame{background-color: rgb(255, 255, 255);}\n"
"QPushButton{border: 2px solid grey; border-radius: 10px;}\n"
"")
        self.gridLayout = QGridLayout(DownloadWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.MainFrame = QFrame(DownloadWidget)
        self.MainFrame.setObjectName(u"MainFrame")
        self.MainFrame.setFrameShape(QFrame.StyledPanel)
        self.MainFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.MainFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.MainFrame)
        self.frame.setObjectName(u"frame")
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.DataSourceBox = QComboBox(self.frame)
        self.DataSourceBox.addItem("")
        self.DataSourceBox.addItem("")
        self.DataSourceBox.setObjectName(u"DataSourceBox")

        self.horizontalLayout.addWidget(self.DataSourceBox)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 3)

        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.MainFrame)
        self.frame_2.setObjectName(u"frame_2")
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.DataTypeBox = QComboBox(self.frame_2)
        self.DataTypeBox.setObjectName(u"DataTypeBox")

        self.horizontalLayout_2.addWidget(self.DataTypeBox)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 3)

        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.MainFrame)
        self.frame_3.setObjectName(u"frame_3")
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.DataPeriodBox = QComboBox(self.frame_3)
        self.DataPeriodBox.setObjectName(u"DataPeriodBox")

        self.horizontalLayout_3.addWidget(self.DataPeriodBox)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 3)

        self.verticalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.MainFrame)
        self.frame_4.setObjectName(u"frame_4")
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.DataEpisodeBox = QComboBox(self.frame_4)
        self.DataEpisodeBox.setObjectName(u"DataEpisodeBox")

        self.horizontalLayout_4.addWidget(self.DataEpisodeBox)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 3)

        self.verticalLayout.addWidget(self.frame_4)

        self.SavePlaceLabel = QLabel(self.MainFrame)
        self.SavePlaceLabel.setObjectName(u"SavePlaceLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SavePlaceLabel.sizePolicy().hasHeightForWidth())
        self.SavePlaceLabel.setSizePolicy(sizePolicy)
        self.SavePlaceLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.SavePlaceLabel)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.RefreshButton = QPushButton(self.MainFrame)
        self.RefreshButton.setObjectName(u"RefreshButton")

        self.horizontalLayout_5.addWidget(self.RefreshButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.DownloadButton = QPushButton(self.MainFrame)
        self.DownloadButton.setObjectName(u"DownloadButton")

        self.horizontalLayout_5.addWidget(self.DownloadButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_5.setStretch(1, 1)
        self.horizontalLayout_5.setStretch(3, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_5)


        self.gridLayout.addWidget(self.MainFrame, 0, 0, 1, 1)


        self.retranslateUi(DownloadWidget)

        QMetaObject.connectSlotsByName(DownloadWidget)
    # setupUi

    def retranslateUi(self, DownloadWidget):
        DownloadWidget.setWindowTitle(QCoreApplication.translate("DownloadWidget", u"Form", None))
        self.label.setText(QCoreApplication.translate("DownloadWidget", u"\u6570\u636e\u6e90", None))
        self.DataSourceBox.setItemText(0, QCoreApplication.translate("DownloadWidget", u"https://sekai.best/", None))
        self.DataSourceBox.setItemText(1, QCoreApplication.translate("DownloadWidget", u"https://pjsek.ai/", None))

        self.label_2.setText(QCoreApplication.translate("DownloadWidget", u"\u5267\u60c5\u7c7b\u578b", None))
        self.label_3.setText(QCoreApplication.translate("DownloadWidget", u"\u5267\u60c5\u671f\u6570", None))
        self.label_4.setText(QCoreApplication.translate("DownloadWidget", u"\u5267\u60c5\u8bdd\u6570", None))
        self.SavePlaceLabel.setText("")
        self.RefreshButton.setText(QCoreApplication.translate("DownloadWidget", u"\u5237\u65b0", None))
        self.DownloadButton.setText(QCoreApplication.translate("DownloadWidget", u"\u5f00\u59cb\u4e0b\u8f7d", None))
    # retranslateUi

