# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WidgetSubtitleTaskAccept.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QSizePolicy, QWidget)

class Ui_AccWidget(object):
    def setupUi(self, AccWidget):
        if not AccWidget.objectName():
            AccWidget.setObjectName(u"AccWidget")
        AccWidget.resize(400, 75)
        AccWidget.setMinimumSize(QSize(0, 75))
        AccWidget.setMaximumSize(QSize(16777215, 75))
        AccWidget.setStyleSheet(u"QLabel#StatusLabel{ font: 500 12pt \"Microsoft YaHei UI\";}\n"
"QWidget#StatusWidget{ border: 3px dashed rgba(0, 157, 255, 50); border-radius:15px;}\n"
"            ")
        self.gridLayout = QGridLayout(AccWidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.StatusWidget = QWidget(AccWidget)
        self.StatusWidget.setObjectName(u"StatusWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StatusWidget.sizePolicy().hasHeightForWidth())
        self.StatusWidget.setSizePolicy(sizePolicy)
        self.StatusWidget.setMinimumSize(QSize(0, 75))
        self.StatusWidget.setMaximumSize(QSize(16777215, 75))
        self.horizontalLayout = QHBoxLayout(self.StatusWidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.StatusLabel = QLabel(self.StatusWidget)
        self.StatusLabel.setObjectName(u"StatusLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.StatusLabel.sizePolicy().hasHeightForWidth())
        self.StatusLabel.setSizePolicy(sizePolicy1)
        self.StatusLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.StatusLabel)


        self.gridLayout.addWidget(self.StatusWidget, 0, 0, 1, 1)


        self.retranslateUi(AccWidget)

        QMetaObject.connectSlotsByName(AccWidget)
    # setupUi

    def retranslateUi(self, AccWidget):
        AccWidget.setWindowTitle(QCoreApplication.translate("AccWidget", u"Form", None))
        self.StatusLabel.setText(QCoreApplication.translate("AccWidget", u"\u70b9\u51fb\u6216\u62d6\u52a8\u6587\u4ef6\u5230\u6b64\u5904\u6765\u521b\u5efa\u4efb\u52a1", None))
    # retranslateUi

