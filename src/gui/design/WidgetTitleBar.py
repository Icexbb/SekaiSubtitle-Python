# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WidgetTitleBar.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QWidget)

class Ui_TitleBar(object):
    def setupUi(self, TitleBar):
        if not TitleBar.objectName():
            TitleBar.setObjectName(u"TitleBar")
        TitleBar.resize(752, 39)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TitleBar.sizePolicy().hasHeightForWidth())
        TitleBar.setSizePolicy(sizePolicy)
        TitleBar.setStyleSheet(u"QPushButton{border-radius:10px;border:2px solid gray;}\n"
"QPushButton#WindowCloseButton{	background-color: rgb(255,100,100);}\n"
"QPushButton#WindowMaxButton{background-color: rgb(100, 255, 100);}\n"
"QPushButton#WindowMinButton{background-color: rgb(255, 255, 100);}\n"
"QLabel#TitleLabel{font: 500 12pt \"Microsoft YaHei UI\";}\n"
"")
        self.horizontalLayout = QHBoxLayout(TitleBar)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(15, -1, 15, -1)
        self.TitleLabel = QLabel(TitleBar)
        self.TitleLabel.setObjectName(u"TitleLabel")

        self.horizontalLayout.addWidget(self.TitleLabel)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.WindowMinButton = QPushButton(TitleBar)
        self.WindowMinButton.setObjectName(u"WindowMinButton")
        self.WindowMinButton.setMinimumSize(QSize(20, 20))
        self.WindowMinButton.setMaximumSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.WindowMinButton)

        self.WindowMaxButton = QPushButton(TitleBar)
        self.WindowMaxButton.setObjectName(u"WindowMaxButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.WindowMaxButton.sizePolicy().hasHeightForWidth())
        self.WindowMaxButton.setSizePolicy(sizePolicy1)
        self.WindowMaxButton.setMinimumSize(QSize(20, 20))
        self.WindowMaxButton.setMaximumSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.WindowMaxButton)

        self.WindowCloseButton = QPushButton(TitleBar)
        self.WindowCloseButton.setObjectName(u"WindowCloseButton")
        sizePolicy1.setHeightForWidth(self.WindowCloseButton.sizePolicy().hasHeightForWidth())
        self.WindowCloseButton.setSizePolicy(sizePolicy1)
        self.WindowCloseButton.setMinimumSize(QSize(20, 20))
        self.WindowCloseButton.setMaximumSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.WindowCloseButton)


        self.retranslateUi(TitleBar)

        QMetaObject.connectSlotsByName(TitleBar)
    # setupUi

    def retranslateUi(self, TitleBar):
        TitleBar.setWindowTitle(QCoreApplication.translate("TitleBar", u"Form", None))
        self.TitleLabel.setText("")
        self.WindowMinButton.setText("")
        self.WindowMaxButton.setText("")
        self.WindowCloseButton.setText("")
    # retranslateUi

