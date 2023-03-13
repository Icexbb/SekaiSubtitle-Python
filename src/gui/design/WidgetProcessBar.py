# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WidgetProcessBar.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QListWidget, QListWidgetItem,
    QProgressBar, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_ProgressBarWidget(object):
    def setupUi(self, ProgressBarWidget):
        if not ProgressBarWidget.objectName():
            ProgressBarWidget.setObjectName(u"ProgressBarWidget")
        ProgressBarWidget.resize(474, 200)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ProgressBarWidget.sizePolicy().hasHeightForWidth())
        ProgressBarWidget.setSizePolicy(sizePolicy)
        ProgressBarWidget.setMinimumSize(QSize(0, 100))
        ProgressBarWidget.setMaximumSize(QSize(16777215, 200))
        ProgressBarWidget.setStyleSheet(u"QProgressBar{height : 10px; border: 2px solid grey; border-radius: 5px;\n"
"                background-color: #FFFFFF;}\n"
"                QProgressBar::chunk { background-color: #007FFF; width: 10px;}\n"
"                QFrame#MainFrame{ background-color:rgb(248, 248, 248);border-color: rgb(204, 204, 204);border-size:\n"
"                2px;border-radius:20px;}\n"
"                QPushButton#StartButton{background-color:rgb(100,255,100);border: 2px solid grey; border-radius: 10px;}\n"
"                QPushButton#DeleteButton{background-color:rgb(255,100,100);border: 2px solid grey; border-radius: 10px;}\n"
"                QPushButton#LogShowButton{border: 2px solid grey; border-radius: 10px;}\n"
"                QListWidget#StatusLogList{ background-color: rgba(255, 255, 255, 0); border: none;outline:0px;}\n"
"                QListWidget::item{background-color: rgba(255, 255, 255, 0);border: none;outline:0px;}\n"
"            ")
        self.gridLayout = QGridLayout(ProgressBarWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.MainFrame = QFrame(ProgressBarWidget)
        self.MainFrame.setObjectName(u"MainFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.MainFrame.sizePolicy().hasHeightForWidth())
        self.MainFrame.setSizePolicy(sizePolicy1)
        self.MainFrame.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.MainFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.TaskStatus = QLabel(self.MainFrame)
        self.TaskStatus.setObjectName(u"TaskStatus")

        self.horizontalLayout.addWidget(self.TaskStatus)

        self.TaskName = QLabel(self.MainFrame)
        self.TaskName.setObjectName(u"TaskName")

        self.horizontalLayout.addWidget(self.TaskName)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.PercentLabel = QLabel(self.MainFrame)
        self.PercentLabel.setObjectName(u"PercentLabel")

        self.horizontalLayout.addWidget(self.PercentLabel)

        self.StartButton = QPushButton(self.MainFrame)
        self.StartButton.setObjectName(u"StartButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.StartButton.sizePolicy().hasHeightForWidth())
        self.StartButton.setSizePolicy(sizePolicy2)
        self.StartButton.setMinimumSize(QSize(20, 20))
        self.StartButton.setMaximumSize(QSize(20, 20))
        self.StartButton.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.StartButton)

        self.DeleteButton = QPushButton(self.MainFrame)
        self.DeleteButton.setObjectName(u"DeleteButton")
        sizePolicy2.setHeightForWidth(self.DeleteButton.sizePolicy().hasHeightForWidth())
        self.DeleteButton.setSizePolicy(sizePolicy2)
        self.DeleteButton.setMinimumSize(QSize(20, 20))
        self.DeleteButton.setMaximumSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.DeleteButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.ProgressBar = QProgressBar(self.MainFrame)
        self.ProgressBar.setObjectName(u"ProgressBar")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.ProgressBar.sizePolicy().hasHeightForWidth())
        self.ProgressBar.setSizePolicy(sizePolicy3)
        self.ProgressBar.setValue(24)
        self.ProgressBar.setTextVisible(False)

        self.verticalLayout.addWidget(self.ProgressBar)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.GraphLayoutWidget = QWidget(self.MainFrame)
        self.GraphLayoutWidget.setObjectName(u"GraphLayoutWidget")
        self.GraphLayoutWidget.setMaximumSize(QSize(200, 16777215))
        self.GraphLayout = QHBoxLayout(self.GraphLayoutWidget)
        self.GraphLayout.setObjectName(u"GraphLayout")

        self.horizontalLayout_2.addWidget(self.GraphLayoutWidget)

        self.StatusLogList = QListWidget(self.MainFrame)
        self.StatusLogList.setObjectName(u"StatusLogList")
        sizePolicy4 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.StatusLogList.sizePolicy().hasHeightForWidth())
        self.StatusLogList.setSizePolicy(sizePolicy4)
        self.StatusLogList.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.StatusLogList.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.StatusLogList.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.StatusLogList.setWordWrap(True)

        self.horizontalLayout_2.addWidget(self.StatusLogList)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.LogShowButton = QPushButton(self.MainFrame)
        self.LogShowButton.setObjectName(u"LogShowButton")
        sizePolicy5 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.LogShowButton.sizePolicy().hasHeightForWidth())
        self.LogShowButton.setSizePolicy(sizePolicy5)
        self.LogShowButton.setMinimumSize(QSize(20, 20))
        self.LogShowButton.setMaximumSize(QSize(20, 20))

        self.verticalLayout_2.addWidget(self.LogShowButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.gridLayout.addWidget(self.MainFrame, 0, 0, 1, 1)


        self.retranslateUi(ProgressBarWidget)

        QMetaObject.connectSlotsByName(ProgressBarWidget)
    # setupUi

    def retranslateUi(self, ProgressBarWidget):
        ProgressBarWidget.setWindowTitle(QCoreApplication.translate("ProgressBarWidget", u"Form", None))
        self.TaskStatus.setText(QCoreApplication.translate("ProgressBarWidget", u"\u672a\u5f00\u59cb", None))
        self.TaskName.setText(QCoreApplication.translate("ProgressBarWidget", u"TaskName", None))
        self.PercentLabel.setText("")
        self.StartButton.setText("")
        self.DeleteButton.setText("")
        self.LogShowButton.setText(QCoreApplication.translate("ProgressBarWidget", u"<", None))
    # retranslateUi

