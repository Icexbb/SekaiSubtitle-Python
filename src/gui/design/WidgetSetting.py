# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WidgetSetting.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFontComboBox,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QSpinBox, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(418, 463)
        Form.setStyleSheet(u"QFrame#MainFrame{background-color: rgb(255, 255, 255);border-radius:10px;}\n"
"                QScrollArea{background-color: transparent;}\n"
"                QWidget#scrollAreaWidgetContents{background-color: transparent;}\n"
"                QLabel{ font: 10pt \"Microsoft YaHei UI\";}\n"
"            ")
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.MainFrame = QFrame(Form)
        self.MainFrame.setObjectName(u"MainFrame")
        self.MainFrame.setStyleSheet(u"")
        self.MainFrame.setFrameShape(QFrame.StyledPanel)
        self.MainFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.MainFrame)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea = QScrollArea(self.MainFrame)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(400, 0))
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QFrame.Plain)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 400, 396))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(2)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.SettingProxyTypeCombo = QComboBox(self.scrollAreaWidgetContents)
        self.SettingProxyTypeCombo.addItem("")
        self.SettingProxyTypeCombo.addItem("")
        self.SettingProxyTypeCombo.addItem("")
        self.SettingProxyTypeCombo.setObjectName(u"SettingProxyTypeCombo")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SettingProxyTypeCombo.sizePolicy().hasHeightForWidth())
        self.SettingProxyTypeCombo.setSizePolicy(sizePolicy)
        self.SettingProxyTypeCombo.setMinimumSize(QSize(75, 0))
        self.SettingProxyTypeCombo.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout_8.addWidget(self.SettingProxyTypeCombo)

        self.SettingProxyEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.SettingProxyEdit.setObjectName(u"SettingProxyEdit")

        self.horizontalLayout_8.addWidget(self.SettingProxyEdit)

        self.label_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_8.addWidget(self.label_6)

        self.SettingProxyHostSpin = QSpinBox(self.scrollAreaWidgetContents)
        self.SettingProxyHostSpin.setObjectName(u"SettingProxyHostSpin")
        self.SettingProxyHostSpin.setMinimumSize(QSize(60, 0))
        self.SettingProxyHostSpin.setMaximumSize(QSize(60, 16777215))
        self.SettingProxyHostSpin.setMinimum(1)
        self.SettingProxyHostSpin.setMaximum(65535)
        self.SettingProxyHostSpin.setValue(8080)

        self.horizontalLayout_8.addWidget(self.SettingProxyHostSpin)


        self.horizontalLayout_2.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 3)

        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(5, 5, 5, 5)
        self.label_9 = QLabel(self.scrollAreaWidgetContents)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_10.addWidget(self.label_9)

        self.SettingTimeoutSpin = QSpinBox(self.scrollAreaWidgetContents)
        self.SettingTimeoutSpin.setObjectName(u"SettingTimeoutSpin")
        self.SettingTimeoutSpin.setMaximum(60)
        self.SettingTimeoutSpin.setSingleStep(1)
        self.SettingTimeoutSpin.setValue(15)

        self.horizontalLayout_10.addWidget(self.SettingTimeoutSpin)

        self.horizontalLayout_10.setStretch(0, 1)
        self.horizontalLayout_10.setStretch(1, 3)

        self.verticalLayout_3.addLayout(self.horizontalLayout_10)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.SettingFontComboBox = QFontComboBox(self.scrollAreaWidgetContents)
        self.SettingFontComboBox.setObjectName(u"SettingFontComboBox")
        font = QFont()
        font.setFamilies([u"\u601d\u6e90\u9ed1\u4f53 CN Bold"])
        font.setPointSize(83)
        font.setBold(True)
        self.SettingFontComboBox.setCurrentFont(font)

        self.horizontalLayout.addWidget(self.SettingFontComboBox)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 3)

        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_5.addWidget(self.label_4)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.SettingChibiSelect = QComboBox(self.scrollAreaWidgetContents)
        self.SettingChibiSelect.setObjectName(u"SettingChibiSelect")

        self.horizontalLayout_6.addWidget(self.SettingChibiSelect)

        self.SettingAnimatedCheck = QCheckBox(self.scrollAreaWidgetContents)
        self.SettingAnimatedCheck.setObjectName(u"SettingAnimatedCheck")
        sizePolicy.setHeightForWidth(self.SettingAnimatedCheck.sizePolicy().hasHeightForWidth())
        self.SettingAnimatedCheck.setSizePolicy(sizePolicy)

        self.horizontalLayout_6.addWidget(self.SettingAnimatedCheck)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 3)

        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(5, 5, 5, 5)
        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_7.addWidget(self.label_5)

        self.SettingStartupUpdateCheck = QCheckBox(self.scrollAreaWidgetContents)
        self.SettingStartupUpdateCheck.setObjectName(u"SettingStartupUpdateCheck")
        sizePolicy.setHeightForWidth(self.SettingStartupUpdateCheck.sizePolicy().hasHeightForWidth())
        self.SettingStartupUpdateCheck.setSizePolicy(sizePolicy)
        self.SettingStartupUpdateCheck.setChecked(True)
        self.SettingStartupUpdateCheck.setAutoRepeat(False)

        self.horizontalLayout_7.addWidget(self.SettingStartupUpdateCheck)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.SettingStartImmediateCheck = QCheckBox(self.scrollAreaWidgetContents)
        self.SettingStartImmediateCheck.setObjectName(u"SettingStartImmediateCheck")
        sizePolicy.setHeightForWidth(self.SettingStartImmediateCheck.sizePolicy().hasHeightForWidth())
        self.SettingStartImmediateCheck.setSizePolicy(sizePolicy)
        self.SettingStartImmediateCheck.setAutoRepeat(False)

        self.horizontalLayout_4.addWidget(self.SettingStartImmediateCheck)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(5, 5, 5, 5)
        self.label_8 = QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_11.addWidget(self.label_8)

        self.SettingStartAdjustWindowCheck = QCheckBox(self.scrollAreaWidgetContents)
        self.SettingStartAdjustWindowCheck.setObjectName(u"SettingStartAdjustWindowCheck")
        sizePolicy.setHeightForWidth(self.SettingStartAdjustWindowCheck.sizePolicy().hasHeightForWidth())
        self.SettingStartAdjustWindowCheck.setSizePolicy(sizePolicy)
        self.SettingStartAdjustWindowCheck.setAutoRepeat(False)

        self.horizontalLayout_11.addWidget(self.SettingStartAdjustWindowCheck)


        self.verticalLayout_3.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(5, 5, 5, 5)
        self.label_7 = QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_9.addWidget(self.label_7)

        self.SettingTyperSpin = QSpinBox(self.scrollAreaWidgetContents)
        self.SettingTyperSpin.setObjectName(u"SettingTyperSpin")
        self.SettingTyperSpin.setMaximum(1000)
        self.SettingTyperSpin.setSingleStep(10)
        self.SettingTyperSpin.setValue(80)

        self.horizontalLayout_9.addWidget(self.SettingTyperSpin)

        self.horizontalLayout_9.setStretch(0, 1)
        self.horizontalLayout_9.setStretch(1, 3)

        self.verticalLayout_3.addLayout(self.horizontalLayout_9)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(self.MainFrame)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_3.addWidget(self.pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.gridLayout.addWidget(self.MainFrame, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u4e0b\u8f7d\u4ee3\u7406", None))
        self.SettingProxyTypeCombo.setItemText(0, QCoreApplication.translate("Form", u"\u65e0", None))
        self.SettingProxyTypeCombo.setItemText(1, QCoreApplication.translate("Form", u"http://", None))
        self.SettingProxyTypeCombo.setItemText(2, QCoreApplication.translate("Form", u"socks5://", None))

        self.label_6.setText(QCoreApplication.translate("Form", u":", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"\u4e0b\u8f7d\u8d85\u65f6(s)", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u81ea\u5b9a\u4e49\u5b57\u4f53", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u4e3b\u754c\u9762\u5c0f\u4eba", None))
        self.SettingAnimatedCheck.setText(QCoreApplication.translate("Form", u"\u4f7f\u7528\u52a8\u753b", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u81ea\u52a8\u68c0\u67e5\u66f4\u65b0", None))
        self.SettingStartupUpdateCheck.setText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"\u4efb\u52a1\u7acb\u5373\u5f00\u59cb", None))
        self.SettingStartImmediateCheck.setText("")
        self.label_8.setText(QCoreApplication.translate("Form", u"\u81ea\u52a8\u8c03\u6574\u7a97\u53e3", None))
        self.SettingStartAdjustWindowCheck.setText("")
        self.label_7.setText(QCoreApplication.translate("Form", u"\u6253\u5b57\u673a\u95f4\u9694", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u5e94\u7528", None))
    # retranslateUi

