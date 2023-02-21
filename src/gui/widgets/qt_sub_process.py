# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WidgetSubtitleProcess.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QGridLayout,
    QHBoxLayout, QListWidget, QListWidgetItem, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_ProcessWidget(object):
    def setupUi(self, ProcessWidget):
        if not ProcessWidget.objectName():
            ProcessWidget.setObjectName(u"ProcessWidget")
        ProcessWidget.resize(448, 462)
        ProcessWidget.setStyleSheet(u"QListWidget#ProcessingListWidget{	background-color: rgba(255, 255, 255, 0);	border: none;outline:0px;}\n"
"QListWidget::item{background-color: rgba(255, 255, 255, 0);	border: none;outline:0px;}\n"
"QFrame{background-color:rgb(248, 248, 248);border-color: rgb(204, 204, 204);border-size: 2px;border-radius:20px;}\n"
"QFrame#MainFrame{background-color: rgb(255, 255, 255);}")
        self.gridLayout = QGridLayout(ProcessWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.MainFrame = QFrame(ProcessWidget)
        self.MainFrame.setObjectName(u"MainFrame")
        self.MainFrame.setFrameShape(QFrame.StyledPanel)
        self.MainFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.MainFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.StatusWidget = QWidget(self.MainFrame)
        self.StatusWidget.setObjectName(u"StatusWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StatusWidget.sizePolicy().hasHeightForWidth())
        self.StatusWidget.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.StatusWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.verticalLayout.addWidget(self.StatusWidget)

        self.ProcessingListWidget = QListWidget(self.MainFrame)
        self.ProcessingListWidget.setObjectName(u"ProcessingListWidget")
        self.ProcessingListWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ProcessingListWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ProcessingListWidget.setProperty("showDropIndicator", False)
        self.ProcessingListWidget.setSelectionMode(QAbstractItemView.NoSelection)

        self.verticalLayout.addWidget(self.ProcessingListWidget)


        self.gridLayout.addWidget(self.MainFrame, 0, 0, 1, 1)


        self.retranslateUi(ProcessWidget)

        QMetaObject.connectSlotsByName(ProcessWidget)
    # setupUi

    def retranslateUi(self, ProcessWidget):
        ProcessWidget.setWindowTitle(QCoreApplication.translate("ProcessWidget", u"Form", None))
    # retranslateUi

