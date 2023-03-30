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
    QHBoxLayout, QListView, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_ProcessWidget(object):
    def setupUi(self, ProcessWidget):
        if not ProcessWidget.objectName():
            ProcessWidget.setObjectName(u"ProcessWidget")
        ProcessWidget.resize(448, 462)
        ProcessWidget.setStyleSheet(u"QListWidget#ProcessingListWidget{ background-color: rgba(255, 255, 255, 0); border:none;outline:0px;}\n"
"QListWidget::item{background-color: rgba(255, 255, 255, 0); border: none;outline:0px;}\n"
"QFrame#MainFrame{background-color: rgb(255, 255, 255);border-radius:10px;}\n"
"            ")
        self.gridLayout = QGridLayout(ProcessWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
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
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ProcessingListWidget.sizePolicy().hasHeightForWidth())
        self.ProcessingListWidget.setSizePolicy(sizePolicy1)
        self.ProcessingListWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ProcessingListWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ProcessingListWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ProcessingListWidget.setSelectionMode(QAbstractItemView.NoSelection)
        self.ProcessingListWidget.setResizeMode(QListView.Adjust)
        self.ProcessingListWidget.setLayoutMode(QListView.SinglePass)

        self.verticalLayout.addWidget(self.ProcessingListWidget)

        self.frame = QFrame(self.MainFrame)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.StartAllButton = QPushButton(self.frame)
        self.StartAllButton.setObjectName(u"StartAllButton")

        self.horizontalLayout_3.addWidget(self.StartAllButton)

        self.StopAllButton = QPushButton(self.frame)
        self.StopAllButton.setObjectName(u"StopAllButton")

        self.horizontalLayout_3.addWidget(self.StopAllButton)

        self.ClearAllButton = QPushButton(self.frame)
        self.ClearAllButton.setObjectName(u"ClearAllButton")

        self.horizontalLayout_3.addWidget(self.ClearAllButton)


        self.verticalLayout.addWidget(self.frame)


        self.gridLayout.addWidget(self.MainFrame, 0, 0, 1, 1)


        self.retranslateUi(ProcessWidget)

        QMetaObject.connectSlotsByName(ProcessWidget)
    # setupUi

    def retranslateUi(self, ProcessWidget):
        ProcessWidget.setWindowTitle(QCoreApplication.translate("ProcessWidget", u"Form", None))
        self.StartAllButton.setText(QCoreApplication.translate("ProcessWidget", u"\u5f00\u59cb\u6240\u6709\u4efb\u52a1", None))
        self.StopAllButton.setText(QCoreApplication.translate("ProcessWidget", u"\u505c\u6b62\u6240\u6709\u4efb\u52a1", None))
        self.ClearAllButton.setText(QCoreApplication.translate("ProcessWidget", u"\u6e05\u7a7a\u4efb\u52a1\u5217\u8868", None))
    # retranslateUi

