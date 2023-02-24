# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WidgetNewTaskSelector.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)

class Ui_SelectWidget(object):
    def setupUi(self, SelectWidget):
        if not SelectWidget.objectName():
            SelectWidget.setObjectName(u"SelectWidget")
        SelectWidget.resize(690, 159)
        self.gridLayout = QGridLayout(SelectWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.SelectGroupBox = QGroupBox(SelectWidget)
        self.SelectGroupBox.setObjectName(u"SelectGroupBox")
        self.SelectGroupBox.setStyleSheet(u"QLineEdit{background-color:\"transparent\";border:None;font: 12pt \"Microsoft YaHei UI\";}")
        self.horizontalLayout = QHBoxLayout(self.SelectGroupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.HintLabel = QLabel(self.SelectGroupBox)
        self.HintLabel.setObjectName(u"HintLabel")

        self.horizontalLayout.addWidget(self.HintLabel)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.FileLabel = QLineEdit(self.SelectGroupBox)
        self.FileLabel.setObjectName(u"FileLabel")
        self.FileLabel.setMouseTracking(False)
        self.FileLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.FileLabel.setReadOnly(True)

        self.horizontalLayout.addWidget(self.FileLabel)

        self.SelectButton = QPushButton(self.SelectGroupBox)
        self.SelectButton.setObjectName(u"SelectButton")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SelectButton.sizePolicy().hasHeightForWidth())
        self.SelectButton.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.SelectButton)


        self.gridLayout.addWidget(self.SelectGroupBox, 0, 0, 1, 1)


        self.retranslateUi(SelectWidget)

        QMetaObject.connectSlotsByName(SelectWidget)
    # setupUi

    def retranslateUi(self, SelectWidget):
        SelectWidget.setWindowTitle(QCoreApplication.translate("SelectWidget", u"Form", None))
        self.HintLabel.setText(QCoreApplication.translate("SelectWidget", u"\u6587\u4ef6", None))
        self.SelectButton.setText(QCoreApplication.translate("SelectWidget", u"\u9009\u62e9", None))
    # retranslateUi

