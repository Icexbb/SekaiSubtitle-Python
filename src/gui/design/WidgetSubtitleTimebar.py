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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QGridLayout, QHBoxLayout,
    QLabel, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(464, 43)
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
        self.MW = QWidget(Form)
        self.MW.setObjectName(u"MW")
        self.horizontalLayout_2 = QHBoxLayout(self.MW)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.LeftSpin = QDoubleSpinBox(self.MW)
        self.LeftSpin.setObjectName(u"LeftSpin")
        self.LeftSpin.setMinimumSize(QSize(100, 0))
        self.LeftSpin.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_2.addWidget(self.LeftSpin)

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
        self.VLeft.setMinimumSize(QSize(5, 25))
        self.VLeft.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout.addWidget(self.VLeft)

        self.VCurrent = QWidget(self.widget)
        self.VCurrent.setObjectName(u"VCurrent")
        self.VCurrent.setEnabled(False)
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.VCurrent.sizePolicy().hasHeightForWidth())
        self.VCurrent.setSizePolicy(sizePolicy2)
        self.VCurrent.setMinimumSize(QSize(0, 25))
        self.VCurrent.setMaximumSize(QSize(16777215, 25))
        self.horizontalLayout_3 = QHBoxLayout(self.VCurrent)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.TimeLabel = QLabel(self.VCurrent)
        self.TimeLabel.setObjectName(u"TimeLabel")
        sizePolicy3 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.TimeLabel.sizePolicy().hasHeightForWidth())
        self.TimeLabel.setSizePolicy(sizePolicy3)
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.TimeLabel.setFont(font)
        self.TimeLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.TimeLabel)


        self.horizontalLayout.addWidget(self.VCurrent)

        self.VRight = QWidget(self.widget)
        self.VRight.setObjectName(u"VRight")
        self.VRight.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.VRight.sizePolicy().hasHeightForWidth())
        self.VRight.setSizePolicy(sizePolicy1)
        self.VRight.setMinimumSize(QSize(5, 25))
        self.VRight.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout.addWidget(self.VRight)


        self.horizontalLayout_2.addWidget(self.widget)

        self.RightSpin = QDoubleSpinBox(self.MW)
        self.RightSpin.setObjectName(u"RightSpin")
        self.RightSpin.setMinimumSize(QSize(100, 0))
        self.RightSpin.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_2.addWidget(self.RightSpin)


        self.gridLayout.addWidget(self.MW, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.TimeLabel.setText(QCoreApplication.translate("Form", u"TextLabel", None))
    # retranslateUi

