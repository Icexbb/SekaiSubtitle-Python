# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WidgetSubtitleTimebar.ui'
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
    QSizePolicy, QSpacerItem, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(464, 47)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setStyleSheet(u"QWidget#Form{background-color: rgb(255, 255, 255); border:5px;}\n"
"QWidget#VCurrent{background-color: rgb(107, 146, 255);border:2px solid gray;}\n"
"QWidget#VRight{background-color: rgb(230, 230, 255);border:2px solid gray;border-left:none; border-top-right-radius:5px;border-bottom-right-radius:5px;}\n"
"QWidget#VLeft{background-color: rgb(230, 230, 255);border:2px solid gray;border-right:none; border-top-left-radius:5px;border-bottom-left-radius:5px;}\n"
"QLabel#TimeLabel{color: rgb(0, 0, 0);}\n"
"\n"
"")
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(9, 3, -1, 3)
        self.MW = QWidget(Form)
        self.MW.setObjectName(u"MW")
        self.horizontalLayout_2 = QHBoxLayout(self.MW)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.LeftSpin = QSpinBox(self.MW)
        self.LeftSpin.setObjectName(u"LeftSpin")
        self.LeftSpin.setMinimumSize(QSize(70, 0))
        self.LeftSpin.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_2.addWidget(self.LeftSpin)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.LLabel = QLabel(self.MW)
        self.LLabel.setObjectName(u"LLabel")
        font = QFont()
        font.setPointSize(8)
        self.LLabel.setFont(font)

        self.horizontalLayout_4.addWidget(self.LLabel)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.CLabel = QLabel(self.MW)
        self.CLabel.setObjectName(u"CLabel")
        self.CLabel.setFont(font)

        self.horizontalLayout_4.addWidget(self.CLabel)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.RLabel = QLabel(self.MW)
        self.RLabel.setObjectName(u"RLabel")
        self.RLabel.setFont(font)

        self.horizontalLayout_4.addWidget(self.RLabel)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.widget = QWidget(self.MW)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.VLeft = QWidget(self.widget)
        self.VLeft.setObjectName(u"VLeft")
        self.VLeft.setEnabled(False)
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.VLeft.sizePolicy().hasHeightForWidth())
        self.VLeft.setSizePolicy(sizePolicy1)
        self.VLeft.setMinimumSize(QSize(5, 10))
        self.VLeft.setMaximumSize(QSize(16777215, 10))

        self.horizontalLayout.addWidget(self.VLeft)

        self.VCurrent = QWidget(self.widget)
        self.VCurrent.setObjectName(u"VCurrent")
        self.VCurrent.setEnabled(False)
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.VCurrent.sizePolicy().hasHeightForWidth())
        self.VCurrent.setSizePolicy(sizePolicy2)
        self.VCurrent.setMinimumSize(QSize(0, 10))
        self.VCurrent.setMaximumSize(QSize(16777215, 10))
        self.horizontalLayout_3 = QHBoxLayout(self.VCurrent)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout.addWidget(self.VCurrent)

        self.VRight = QWidget(self.widget)
        self.VRight.setObjectName(u"VRight")
        self.VRight.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.VRight.sizePolicy().hasHeightForWidth())
        self.VRight.setSizePolicy(sizePolicy1)
        self.VRight.setMinimumSize(QSize(5, 10))
        self.VRight.setMaximumSize(QSize(16777215, 10))

        self.horizontalLayout.addWidget(self.VRight)


        self.verticalLayout.addWidget(self.widget)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.RightSpin = QSpinBox(self.MW)
        self.RightSpin.setObjectName(u"RightSpin")
        self.RightSpin.setMinimumSize(QSize(70, 0))
        self.RightSpin.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_2.addWidget(self.RightSpin)


        self.gridLayout.addWidget(self.MW, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.LLabel.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.CLabel.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.RLabel.setText(QCoreApplication.translate("Form", u"TextLabel", None))
    # retranslateUi

