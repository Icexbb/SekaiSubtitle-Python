# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WidgetTranslateItem.ui'
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
    QLabel, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_WidgetTranslateItem(object):
    def setupUi(self, WidgetTranslateItem):
        if not WidgetTranslateItem.objectName():
            WidgetTranslateItem.setObjectName(u"WidgetTranslateItem")
        WidgetTranslateItem.resize(393, 62)
        WidgetTranslateItem.setMinimumSize(QSize(0, 62))
        WidgetTranslateItem.setStyleSheet(u"QFrame#MainFrame{background-color:rgb(250, 250, 250);border:1px solid rgba(0,0,0,128);border-radius:5px;}\n"
"                QListWidget{background-color: rgba(255, 255, 255, 0); border: none;outline:0px;}\n"
"                QListWidget::item{background-color: rgba(255, 255, 255, 0); border: none;outline:0px;}\n"
"            ")
        self.gridLayout = QGridLayout(WidgetTranslateItem)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.MainFrame = QFrame(WidgetTranslateItem)
        self.MainFrame.setObjectName(u"MainFrame")
        self.MainFrame.setFrameShape(QFrame.NoFrame)
        self.MainFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.MainFrame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.FrameInfo = QFrame(self.MainFrame)
        self.FrameInfo.setObjectName(u"FrameInfo")
        self.FrameInfo.setMinimumSize(QSize(50, 0))
        self.FrameInfo.setMaximumSize(QSize(50, 16777215))
        self.FrameInfo.setFrameShape(QFrame.StyledPanel)
        self.FrameInfo.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.FrameInfo)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.LabelNumber = QLabel(self.FrameInfo)
        self.LabelNumber.setObjectName(u"LabelNumber")
        self.LabelNumber.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.LabelNumber)

        self.LabelType = QLabel(self.FrameInfo)
        self.LabelType.setObjectName(u"LabelType")
        self.LabelType.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.LabelType)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addWidget(self.FrameInfo)

        self.FrameChara = QFrame(self.MainFrame)
        self.FrameChara.setObjectName(u"FrameChara")
        self.FrameChara.setMinimumSize(QSize(120, 0))
        self.FrameChara.setMaximumSize(QSize(120, 16777215))
        self.FrameChara.setFrameShape(QFrame.StyledPanel)
        self.FrameChara.setFrameShadow(QFrame.Raised)
        self.FrameCharaLayout = QGridLayout(self.FrameChara)
        self.FrameCharaLayout.setSpacing(0)
        self.FrameCharaLayout.setObjectName(u"FrameCharaLayout")
        self.FrameCharaLayout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout.addWidget(self.FrameChara)

        self.WidgetLines = QWidget(self.MainFrame)
        self.WidgetLines.setObjectName(u"WidgetLines")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.WidgetLines.sizePolicy().hasHeightForWidth())
        self.WidgetLines.setSizePolicy(sizePolicy)
        self.WidgetLinesLayout = QVBoxLayout(self.WidgetLines)
        self.WidgetLinesLayout.setSpacing(0)
        self.WidgetLinesLayout.setObjectName(u"WidgetLinesLayout")
        self.WidgetLinesLayout.setContentsMargins(0, 0, 0, 2)

        self.horizontalLayout.addWidget(self.WidgetLines)


        self.gridLayout.addWidget(self.MainFrame, 0, 0, 1, 1)


        self.retranslateUi(WidgetTranslateItem)

        QMetaObject.connectSlotsByName(WidgetTranslateItem)
    # setupUi

    def retranslateUi(self, WidgetTranslateItem):
        WidgetTranslateItem.setWindowTitle(QCoreApplication.translate("WidgetTranslateItem", u"Form", None))
        self.LabelNumber.setText(QCoreApplication.translate("WidgetTranslateItem", u"Num", None))
        self.LabelType.setText(QCoreApplication.translate("WidgetTranslateItem", u"Type", None))
    # retranslateUi

