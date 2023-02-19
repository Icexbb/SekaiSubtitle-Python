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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QProgressBar, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_ProgressBarWidget(object):
    def setupUi(self, ProgressBarWidget):
        if not ProgressBarWidget.objectName():
            ProgressBarWidget.setObjectName(u"ProgressBarWidget")
        ProgressBarWidget.resize(393, 100)
        ProgressBarWidget.setMinimumSize(QSize(0, 100))
        ProgressBarWidget.setMaximumSize(QSize(16777215, 100))
        ProgressBarWidget.setStyleSheet(u"QProgressBar{height : 10px; border: 2px solid grey; border-radius: 5px; background-color: #FFFFFF;}\n"
"QProgressBar::chunk { background-color: #007FFF; width: 10px;}\n"
"\n"
"QFrame#MainFrame{background-color: rgb(255, 255, 255);border-color: rgb(204, 204, 204);border-size: 2px;border-radius:20px;}\n"
"QPushButton#StartButton{background-color:rgb(100,255,100);border: 2px solid grey; border-radius: 10px;}\n"
"QPushButton#DeleteButton{background-color:rgb(255,100,100);border: 2px solid grey; border-radius: 10px;}")
        self.gridLayout = QGridLayout(ProgressBarWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.MainFrame = QFrame(ProgressBarWidget)
        self.MainFrame.setObjectName(u"MainFrame")
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

        self.StartButton = QPushButton(self.MainFrame)
        self.StartButton.setObjectName(u"StartButton")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StartButton.sizePolicy().hasHeightForWidth())
        self.StartButton.setSizePolicy(sizePolicy)
        self.StartButton.setMinimumSize(QSize(20, 20))
        self.StartButton.setMaximumSize(QSize(20, 20))
        self.StartButton.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.StartButton)

        self.DeleteButton = QPushButton(self.MainFrame)
        self.DeleteButton.setObjectName(u"DeleteButton")
        sizePolicy.setHeightForWidth(self.DeleteButton.sizePolicy().hasHeightForWidth())
        self.DeleteButton.setSizePolicy(sizePolicy)
        self.DeleteButton.setMinimumSize(QSize(20, 20))
        self.DeleteButton.setMaximumSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.DeleteButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.ProgressBar = QProgressBar(self.MainFrame)
        self.ProgressBar.setObjectName(u"ProgressBar")
        self.ProgressBar.setValue(24)
        self.ProgressBar.setTextVisible(False)

        self.verticalLayout.addWidget(self.ProgressBar)

        self.StatusLog = QLabel(self.MainFrame)
        self.StatusLog.setObjectName(u"StatusLog")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.StatusLog.sizePolicy().hasHeightForWidth())
        self.StatusLog.setSizePolicy(sizePolicy1)
        self.StatusLog.setScaledContents(False)
        self.StatusLog.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.StatusLog)


        self.gridLayout.addWidget(self.MainFrame, 0, 0, 1, 1)


        self.retranslateUi(ProgressBarWidget)

        QMetaObject.connectSlotsByName(ProgressBarWidget)
    # setupUi

    def retranslateUi(self, ProgressBarWidget):
        ProgressBarWidget.setWindowTitle(QCoreApplication.translate("ProgressBarWidget", u"Form", None))
        self.TaskStatus.setText(QCoreApplication.translate("ProgressBarWidget", u"\u672a\u5f00\u59cb", None))
        self.TaskName.setText(QCoreApplication.translate("ProgressBarWidget", u"TaskName", None))
        self.StartButton.setText("")
        self.DeleteButton.setText("")
        self.StatusLog.setText("")
    # retranslateUi

