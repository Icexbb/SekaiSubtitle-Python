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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QGridLayout, QHBoxLayout,
    QListWidget, QListWidgetItem, QSizePolicy, QWidget)

class Ui_ProcessWidget(object):
    def setupUi(self, ProcessWidget):
        if not ProcessWidget.objectName():
            ProcessWidget.setObjectName(u"ProcessWidget")
        ProcessWidget.resize(295, 293)
        ProcessWidget.setStyleSheet(u"QListWidget#ProcessingListWidget{	background-color: rgba(255, 255, 255, 0);	border: none;outline:0px;}\n"
"QListWidget::item{background-color: rgba(255, 255, 255, 0);	border: none;outline:0px;}")
        self.gridLayout = QGridLayout(ProcessWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.StatusWidget = QWidget(ProcessWidget)
        self.StatusWidget.setObjectName(u"StatusWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StatusWidget.sizePolicy().hasHeightForWidth())
        self.StatusWidget.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.StatusWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.gridLayout.addWidget(self.StatusWidget, 0, 0, 1, 1)

        self.ProcessingListWidget = QListWidget(ProcessWidget)
        self.ProcessingListWidget.setObjectName(u"ProcessingListWidget")
        self.ProcessingListWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ProcessingListWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ProcessingListWidget.setProperty("showDropIndicator", False)
        self.ProcessingListWidget.setSelectionMode(QAbstractItemView.NoSelection)

        self.gridLayout.addWidget(self.ProcessingListWidget, 2, 0, 1, 1)

        self.gridLayout.setRowStretch(0, 1)

        self.retranslateUi(ProcessWidget)

        QMetaObject.connectSlotsByName(ProcessWidget)
    # setupUi

    def retranslateUi(self, ProcessWidget):
        ProcessWidget.setWindowTitle(QCoreApplication.translate("ProcessWidget", u"Form", None))
    # retranslateUi

