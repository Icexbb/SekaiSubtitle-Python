# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WidgetTranslateLines.ui'
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
    QLabel, QLineEdit, QSizePolicy, QToolButton,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(394, 94)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(0, 64))
        Form.setMaximumSize(QSize(16777215, 94))
        Form.setStyleSheet(u"#WidgetUp{background-color: rgba(150, 255, 150,50);}\n"
"#WidgetDown{background-color: rgba(255, 255, 150, 50);}\n"
"#WidgetMiddle{background-color: rgba(150, 255, 255, 50);}\n"
"QLineEdit{margin:2px;background-color:rgba(0,0,0,0);}\n"
"QToolButton#ClearButton{border:0px;background-color: rgba(255, 150, 150, 50);}\n"
"#LineFrame{border:0.5px solid rgba(0,0,0,64);border-radius:5px;}")
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.LineFrame = QFrame(Form)
        self.LineFrame.setObjectName(u"LineFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.LineFrame.sizePolicy().hasHeightForWidth())
        self.LineFrame.setSizePolicy(sizePolicy1)
        self.LineFrame.setFrameShape(QFrame.StyledPanel)
        self.LineFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.LineFrame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.WidgetUp = QWidget(self.LineFrame)
        self.WidgetUp.setObjectName(u"WidgetUp")
        self.WidgetUp.setMinimumSize(QSize(0, 30))
        self.WidgetUp.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_2 = QHBoxLayout(self.WidgetUp)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.TextBrowserOrigin = QLineEdit(self.WidgetUp)
        self.TextBrowserOrigin.setObjectName(u"TextBrowserOrigin")
        self.TextBrowserOrigin.setMinimumSize(QSize(0, 30))
        self.TextBrowserOrigin.setMaximumSize(QSize(16777215, 30))
        self.TextBrowserOrigin.setMouseTracking(False)
        self.TextBrowserOrigin.setFocusPolicy(Qt.NoFocus)
        self.TextBrowserOrigin.setFrame(False)
        self.TextBrowserOrigin.setReadOnly(True)
        self.TextBrowserOrigin.setClearButtonEnabled(False)

        self.horizontalLayout_2.addWidget(self.TextBrowserOrigin)


        self.verticalLayout.addWidget(self.WidgetUp)

        self.WidgetMiddle = QWidget(self.LineFrame)
        self.WidgetMiddle.setObjectName(u"WidgetMiddle")
        self.WidgetMiddle.setMinimumSize(QSize(0, 0))
        self.WidgetMiddle.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout = QHBoxLayout(self.WidgetMiddle)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.TextBrowserTranslated = QLineEdit(self.WidgetMiddle)
        self.TextBrowserTranslated.setObjectName(u"TextBrowserTranslated")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.TextBrowserTranslated.sizePolicy().hasHeightForWidth())
        self.TextBrowserTranslated.setSizePolicy(sizePolicy2)
        self.TextBrowserTranslated.setMinimumSize(QSize(0, 30))
        self.TextBrowserTranslated.setMaximumSize(QSize(16777215, 30))
        self.TextBrowserTranslated.setMouseTracking(False)
        self.TextBrowserTranslated.setFocusPolicy(Qt.NoFocus)
        self.TextBrowserTranslated.setFrame(False)
        self.TextBrowserTranslated.setReadOnly(True)
        self.TextBrowserTranslated.setClearButtonEnabled(False)

        self.horizontalLayout.addWidget(self.TextBrowserTranslated)


        self.verticalLayout.addWidget(self.WidgetMiddle)

        self.WidgetDown = QWidget(self.LineFrame)
        self.WidgetDown.setObjectName(u"WidgetDown")
        self.WidgetDown.setMinimumSize(QSize(0, 30))
        self.WidgetDown.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_3 = QHBoxLayout(self.WidgetDown)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.TextEditTranslate = QLineEdit(self.WidgetDown)
        self.TextEditTranslate.setObjectName(u"TextEditTranslate")
        self.TextEditTranslate.setMinimumSize(QSize(0, 30))
        self.TextEditTranslate.setMaximumSize(QSize(16777215, 30))
        self.TextEditTranslate.setTabletTracking(True)
        self.TextEditTranslate.setFocusPolicy(Qt.StrongFocus)
        self.TextEditTranslate.setAutoFillBackground(False)
        self.TextEditTranslate.setFrame(False)

        self.horizontalLayout_3.addWidget(self.TextEditTranslate)

        self.WarningLabel = QLabel(self.WidgetDown)
        self.WarningLabel.setObjectName(u"WarningLabel")
        self.WarningLabel.setToolTipDuration(0)

        self.horizontalLayout_3.addWidget(self.WarningLabel)

        self.TextLengthLabel = QLabel(self.WidgetDown)
        self.TextLengthLabel.setObjectName(u"TextLengthLabel")

        self.horizontalLayout_3.addWidget(self.TextLengthLabel)

        self.ClearButton = QToolButton(self.WidgetDown)
        self.ClearButton.setObjectName(u"ClearButton")
        self.ClearButton.setMinimumSize(QSize(15, 30))
        self.ClearButton.setMaximumSize(QSize(15, 30))

        self.horizontalLayout_3.addWidget(self.ClearButton)


        self.verticalLayout.addWidget(self.WidgetDown)


        self.gridLayout.addWidget(self.LineFrame, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.WarningLabel.setText("")
        self.TextLengthLabel.setText("")
        self.ClearButton.setText(QCoreApplication.translate("Form", u"x", None))
    # retranslateUi

