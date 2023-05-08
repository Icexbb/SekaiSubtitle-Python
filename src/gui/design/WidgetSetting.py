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
from PySide6.QtWidgets import (QApplication, QFontComboBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

from qfluentwidgets import (CheckBox, ComboBox, LineEdit, PushButton,
    ScrollArea, SpinBox)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(562, 626)
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
        self.scrollArea = ScrollArea(self.MainFrame)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(400, 0))
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QFrame.Plain)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 527, 770))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.GB1 = QGroupBox(self.scrollAreaWidgetContents)
        self.GB1.setObjectName(u"GB1")
        self.verticalLayout_2 = QVBoxLayout(self.GB1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.HW1 = QWidget(self.GB1)
        self.HW1.setObjectName(u"HW1")
        self.HW1.setMinimumSize(QSize(0, 60))
        self.HL1 = QHBoxLayout(self.HW1)
        self.HL1.setSpacing(5)
        self.HL1.setObjectName(u"HL1")
        self.HL1.setContentsMargins(5, 5, 5, 5)
        self.label_5 = QLabel(self.HW1)
        self.label_5.setObjectName(u"label_5")

        self.HL1.addWidget(self.label_5)

        self.widget = QWidget(self.HW1)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.SettingStartupUpdateCheck = CheckBox(self.widget)
        self.SettingStartupUpdateCheck.setObjectName(u"SettingStartupUpdateCheck")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SettingStartupUpdateCheck.sizePolicy().hasHeightForWidth())
        self.SettingStartupUpdateCheck.setSizePolicy(sizePolicy)
        self.SettingStartupUpdateCheck.setChecked(True)
        self.SettingStartupUpdateCheck.setAutoRepeat(False)

        self.horizontalLayout.addWidget(self.SettingStartupUpdateCheck)


        self.HL1.addWidget(self.widget)

        self.HL1.setStretch(0, 2)
        self.HL1.setStretch(1, 5)

        self.verticalLayout_2.addWidget(self.HW1)

        self.HW2 = QWidget(self.GB1)
        self.HW2.setObjectName(u"HW2")
        self.HW2.setMinimumSize(QSize(0, 60))
        self.HL2 = QHBoxLayout(self.HW2)
        self.HL2.setSpacing(5)
        self.HL2.setObjectName(u"HL2")
        self.HL2.setContentsMargins(5, 5, 5, 5)
        self.label_8 = QLabel(self.HW2)
        self.label_8.setObjectName(u"label_8")

        self.HL2.addWidget(self.label_8)

        self.widget_2 = QWidget(self.HW2)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_3 = QSpacerItem(240, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.SettingStartAdjustWindowCheck = CheckBox(self.widget_2)
        self.SettingStartAdjustWindowCheck.setObjectName(u"SettingStartAdjustWindowCheck")
        sizePolicy.setHeightForWidth(self.SettingStartAdjustWindowCheck.sizePolicy().hasHeightForWidth())
        self.SettingStartAdjustWindowCheck.setSizePolicy(sizePolicy)
        self.SettingStartAdjustWindowCheck.setAutoRepeat(False)

        self.horizontalLayout_2.addWidget(self.SettingStartAdjustWindowCheck)


        self.HL2.addWidget(self.widget_2)

        self.HL2.setStretch(0, 2)
        self.HL2.setStretch(1, 5)

        self.verticalLayout_2.addWidget(self.HW2)

        self.HW3 = QWidget(self.GB1)
        self.HW3.setObjectName(u"HW3")
        self.HW3.setMinimumSize(QSize(0, 60))
        self.HL3 = QHBoxLayout(self.HW3)
        self.HL3.setSpacing(5)
        self.HL3.setObjectName(u"HL3")
        self.HL3.setContentsMargins(5, 5, 5, 5)
        self.label_4 = QLabel(self.HW3)
        self.label_4.setObjectName(u"label_4")

        self.HL3.addWidget(self.label_4)

        self.HWW1 = QWidget(self.HW3)
        self.HWW1.setObjectName(u"HWW1")
        self.horizontalLayout_6 = QHBoxLayout(self.HWW1)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_9)

        self.SettingChibiSelect = ComboBox(self.HWW1)
        self.SettingChibiSelect.setObjectName(u"SettingChibiSelect")
        self.SettingChibiSelect.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_6.addWidget(self.SettingChibiSelect)

        self.SettingAnimatedCheck = CheckBox(self.HWW1)
        self.SettingAnimatedCheck.setObjectName(u"SettingAnimatedCheck")
        sizePolicy.setHeightForWidth(self.SettingAnimatedCheck.sizePolicy().hasHeightForWidth())
        self.SettingAnimatedCheck.setSizePolicy(sizePolicy)

        self.horizontalLayout_6.addWidget(self.SettingAnimatedCheck)


        self.HL3.addWidget(self.HWW1)

        self.HL3.setStretch(0, 2)
        self.HL3.setStretch(1, 5)

        self.verticalLayout_2.addWidget(self.HW3)


        self.verticalLayout_3.addWidget(self.GB1)

        self.GB2 = QGroupBox(self.scrollAreaWidgetContents)
        self.GB2.setObjectName(u"GB2")
        self.verticalLayout_5 = QVBoxLayout(self.GB2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(3, 3, 3, 3)
        self.HW4 = QWidget(self.GB2)
        self.HW4.setObjectName(u"HW4")
        self.HW4.setMinimumSize(QSize(0, 60))
        self.HL4 = QHBoxLayout(self.HW4)
        self.HL4.setSpacing(5)
        self.HL4.setObjectName(u"HL4")
        self.HL4.setContentsMargins(5, 5, 5, 5)
        self.label_3 = QLabel(self.HW4)
        self.label_3.setObjectName(u"label_3")

        self.HL4.addWidget(self.label_3)

        self.widget_3 = QWidget(self.HW4)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_4 = QSpacerItem(240, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.SettingStartImmediateCheck = CheckBox(self.widget_3)
        self.SettingStartImmediateCheck.setObjectName(u"SettingStartImmediateCheck")
        sizePolicy.setHeightForWidth(self.SettingStartImmediateCheck.sizePolicy().hasHeightForWidth())
        self.SettingStartImmediateCheck.setSizePolicy(sizePolicy)
        self.SettingStartImmediateCheck.setAutoRepeat(False)

        self.horizontalLayout_4.addWidget(self.SettingStartImmediateCheck)


        self.HL4.addWidget(self.widget_3)

        self.HL4.setStretch(0, 2)
        self.HL4.setStretch(1, 5)

        self.verticalLayout_5.addWidget(self.HW4)

        self.HW5 = QWidget(self.GB2)
        self.HW5.setObjectName(u"HW5")
        self.HW5.setMinimumSize(QSize(0, 60))
        self.HL5 = QHBoxLayout(self.HW5)
        self.HL5.setSpacing(5)
        self.HL5.setObjectName(u"HL5")
        self.HL5.setContentsMargins(5, 5, 5, 5)
        self.label = QLabel(self.HW5)
        self.label.setObjectName(u"label")

        self.HL5.addWidget(self.label)

        self.widget_4 = QWidget(self.HW5)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(20, 0))
        self.horizontalLayout_5 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)

        self.SettingFontComboBox = QFontComboBox(self.widget_4)
        self.SettingFontComboBox.setObjectName(u"SettingFontComboBox")
        font = QFont()
        font.setFamilies([u"\u601d\u6e90\u9ed1\u4f53 CN Bold"])
        font.setPointSize(83)
        font.setBold(True)
        self.SettingFontComboBox.setCurrentFont(font)

        self.horizontalLayout_5.addWidget(self.SettingFontComboBox)


        self.HL5.addWidget(self.widget_4)

        self.HL5.setStretch(0, 2)
        self.HL5.setStretch(1, 5)

        self.verticalLayout_5.addWidget(self.HW5)

        self.HW6 = QWidget(self.GB2)
        self.HW6.setObjectName(u"HW6")
        self.HW6.setMinimumSize(QSize(0, 60))
        self.HL6 = QHBoxLayout(self.HW6)
        self.HL6.setSpacing(5)
        self.HL6.setObjectName(u"HL6")
        self.HL6.setContentsMargins(5, 5, 5, 5)
        self.label_7 = QLabel(self.HW6)
        self.label_7.setObjectName(u"label_7")

        self.HL6.addWidget(self.label_7)

        self.widget_5 = QWidget(self.HW6)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMinimumSize(QSize(20, 0))
        self.horizontalLayout_7 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.HS = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.HS)

        self.SettingTyperIntervalSpin = SpinBox(self.widget_5)
        self.SettingTyperIntervalSpin.setObjectName(u"SettingTyperIntervalSpin")
        self.SettingTyperIntervalSpin.setMinimumSize(QSize(47, 0))
        self.SettingTyperIntervalSpin.setMaximum(1000)
        self.SettingTyperIntervalSpin.setSingleStep(10)
        self.SettingTyperIntervalSpin.setValue(80)

        self.horizontalLayout_7.addWidget(self.SettingTyperIntervalSpin)

        self.label_22 = QLabel(self.widget_5)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_7.addWidget(self.label_22)


        self.HL6.addWidget(self.widget_5)

        self.HL6.setStretch(0, 2)
        self.HL6.setStretch(1, 5)

        self.verticalLayout_5.addWidget(self.HW6)

        self.HW7 = QWidget(self.GB2)
        self.HW7.setObjectName(u"HW7")
        self.HW7.setMinimumSize(QSize(0, 60))
        self.HL6_2 = QHBoxLayout(self.HW7)
        self.HL6_2.setSpacing(5)
        self.HL6_2.setObjectName(u"HL6_2")
        self.HL6_2.setContentsMargins(5, 5, 5, 5)
        self.label_10 = QLabel(self.HW7)
        self.label_10.setObjectName(u"label_10")

        self.HL6_2.addWidget(self.label_10)

        self.widget_8 = QWidget(self.HW7)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setMinimumSize(QSize(20, 0))
        self.horizontalLayout_11 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.HS_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.HS_2)

        self.SettingTyperFadeSpin = SpinBox(self.widget_8)
        self.SettingTyperFadeSpin.setObjectName(u"SettingTyperFadeSpin")
        self.SettingTyperFadeSpin.setMinimumSize(QSize(47, 0))
        self.SettingTyperFadeSpin.setMaximum(1000)
        self.SettingTyperFadeSpin.setSingleStep(10)
        self.SettingTyperFadeSpin.setValue(50)

        self.horizontalLayout_11.addWidget(self.SettingTyperFadeSpin)

        self.label_23 = QLabel(self.widget_8)
        self.label_23.setObjectName(u"label_23")

        self.horizontalLayout_11.addWidget(self.label_23)


        self.HL6_2.addWidget(self.widget_8)

        self.HL6_2.setStretch(0, 2)
        self.HL6_2.setStretch(1, 5)

        self.verticalLayout_5.addWidget(self.HW7)


        self.verticalLayout_3.addWidget(self.GB2)

        self.GB3 = QGroupBox(self.scrollAreaWidgetContents)
        self.GB3.setObjectName(u"GB3")
        self.verticalLayout_6 = QVBoxLayout(self.GB3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(3, 3, 3, 3)
        self.HW8 = QWidget(self.GB3)
        self.HW8.setObjectName(u"HW8")
        self.HW8.setMinimumSize(QSize(0, 60))
        self.HL7 = QHBoxLayout(self.HW8)
        self.HL7.setSpacing(5)
        self.HL7.setObjectName(u"HL7")
        self.HL7.setContentsMargins(5, 5, 5, 5)
        self.label_2 = QLabel(self.HW8)
        self.label_2.setObjectName(u"label_2")

        self.HL7.addWidget(self.label_2)

        self.qw = QWidget(self.HW8)
        self.qw.setObjectName(u"qw")
        self.horizontalLayout_8 = QHBoxLayout(self.qw)
        self.horizontalLayout_8.setSpacing(2)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_6)

        self.SettingProxyTypeCombo = ComboBox(self.qw)
        self.SettingProxyTypeCombo.addItem("")
        self.SettingProxyTypeCombo.addItem("")
        self.SettingProxyTypeCombo.addItem("")
        self.SettingProxyTypeCombo.setObjectName(u"SettingProxyTypeCombo")
        sizePolicy.setHeightForWidth(self.SettingProxyTypeCombo.sizePolicy().hasHeightForWidth())
        self.SettingProxyTypeCombo.setSizePolicy(sizePolicy)
        self.SettingProxyTypeCombo.setMinimumSize(QSize(100, 0))
        self.SettingProxyTypeCombo.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_8.addWidget(self.SettingProxyTypeCombo)

        self.SettingProxyEdit = LineEdit(self.qw)
        self.SettingProxyEdit.setObjectName(u"SettingProxyEdit")

        self.horizontalLayout_8.addWidget(self.SettingProxyEdit)

        self.SettingProxyLabel = QLabel(self.qw)
        self.SettingProxyLabel.setObjectName(u"SettingProxyLabel")

        self.horizontalLayout_8.addWidget(self.SettingProxyLabel)

        self.SettingProxyHostSpin = SpinBox(self.qw)
        self.SettingProxyHostSpin.setObjectName(u"SettingProxyHostSpin")
        self.SettingProxyHostSpin.setMinimumSize(QSize(120, 0))
        self.SettingProxyHostSpin.setMaximumSize(QSize(120, 16777215))
        self.SettingProxyHostSpin.setMinimum(1)
        self.SettingProxyHostSpin.setMaximum(65535)
        self.SettingProxyHostSpin.setValue(8080)

        self.horizontalLayout_8.addWidget(self.SettingProxyHostSpin)


        self.HL7.addWidget(self.qw)

        self.HL7.setStretch(0, 2)
        self.HL7.setStretch(1, 5)

        self.verticalLayout_6.addWidget(self.HW8)

        self.HW9 = QWidget(self.GB3)
        self.HW9.setObjectName(u"HW9")
        self.HW9.setMinimumSize(QSize(0, 60))
        self.HL8 = QHBoxLayout(self.HW9)
        self.HL8.setSpacing(5)
        self.HL8.setObjectName(u"HL8")
        self.HL8.setContentsMargins(5, 5, 5, 5)
        self.label_9 = QLabel(self.HW9)
        self.label_9.setObjectName(u"label_9")

        self.HL8.addWidget(self.label_9)

        self.widget_6 = QWidget(self.HW9)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMinimumSize(QSize(20, 0))
        self.horizontalLayout_9 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_7)

        self.SettingTimeoutSpin = SpinBox(self.widget_6)
        self.SettingTimeoutSpin.setObjectName(u"SettingTimeoutSpin")
        self.SettingTimeoutSpin.setMinimumSize(QSize(60, 0))
        self.SettingTimeoutSpin.setMaximum(60)
        self.SettingTimeoutSpin.setSingleStep(1)
        self.SettingTimeoutSpin.setValue(15)

        self.horizontalLayout_9.addWidget(self.SettingTimeoutSpin)

        self.label_21 = QLabel(self.widget_6)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_9.addWidget(self.label_21)


        self.HL8.addWidget(self.widget_6)

        self.HL8.setStretch(0, 2)
        self.HL8.setStretch(1, 5)

        self.verticalLayout_6.addWidget(self.HW9)


        self.verticalLayout_3.addWidget(self.GB3)

        self.GB4 = QGroupBox(self.scrollAreaWidgetContents)
        self.GB4.setObjectName(u"GB4")
        self.verticalLayout_7 = QVBoxLayout(self.GB4)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(3, 3, 3, 3)
        self.HW10 = QWidget(self.GB4)
        self.HW10.setObjectName(u"HW10")
        self.HW10.setMinimumSize(QSize(0, 60))
        self.HL9 = QHBoxLayout(self.HW10)
        self.HL9.setSpacing(5)
        self.HL9.setObjectName(u"HL9")
        self.HL9.setContentsMargins(5, 5, 5, 5)
        self.label_19 = QLabel(self.HW10)
        self.label_19.setObjectName(u"label_19")

        self.HL9.addWidget(self.label_19)

        self.widget_7 = QWidget(self.HW10)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_10 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_8)

        self.SettingSaveSpin = SpinBox(self.widget_7)
        self.SettingSaveSpin.setObjectName(u"SettingSaveSpin")
        self.SettingSaveSpin.setMinimumSize(QSize(60, 0))
        self.SettingSaveSpin.setMaximum(1000)
        self.SettingSaveSpin.setSingleStep(10)
        self.SettingSaveSpin.setValue(80)

        self.horizontalLayout_10.addWidget(self.SettingSaveSpin)

        self.label_6 = QLabel(self.widget_7)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_10.addWidget(self.label_6)


        self.HL9.addWidget(self.widget_7)

        self.HL9.setStretch(0, 2)
        self.HL9.setStretch(1, 5)

        self.verticalLayout_7.addWidget(self.HW10)


        self.verticalLayout_3.addWidget(self.GB4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.widget1 = QWidget(self.MainFrame)
        self.widget1.setObjectName(u"widget1")
        self.horizontalLayout_3 = QHBoxLayout(self.widget1)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.pushButton = PushButton(self.widget1)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_3.addWidget(self.pushButton)


        self.verticalLayout.addWidget(self.widget1)


        self.gridLayout.addWidget(self.MainFrame, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.GB1.setTitle(QCoreApplication.translate("Form", u"\u4e00\u822c\u8bbe\u7f6e", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u81ea\u52a8\u68c0\u67e5\u66f4\u65b0", None))
        self.SettingStartupUpdateCheck.setText("")
        self.label_8.setText(QCoreApplication.translate("Form", u"\u81ea\u52a8\u8c03\u6574\u7a97\u53e3", None))
        self.SettingStartAdjustWindowCheck.setText("")
        self.label_4.setText(QCoreApplication.translate("Form", u"\u4e3b\u754c\u9762\u5c0f\u4eba", None))
        self.SettingAnimatedCheck.setText(QCoreApplication.translate("Form", u"\u52a8\u753b", None))
        self.GB2.setTitle(QCoreApplication.translate("Form", u"\u5b57\u5e55\u751f\u6210", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u4efb\u52a1\u7acb\u5373\u5f00\u59cb", None))
        self.SettingStartImmediateCheck.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"\u81ea\u5b9a\u4e49\u5b57\u4f53", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u6253\u5b57\u673a\u6587\u5b57\u95f4\u9694", None))
        self.label_22.setText(QCoreApplication.translate("Form", u"\u6beb\u79d2", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"\u6253\u5b57\u673a\u6e10\u53d8\u65f6\u957f", None))
        self.label_23.setText(QCoreApplication.translate("Form", u"\u6beb\u79d2", None))
        self.GB3.setTitle(QCoreApplication.translate("Form", u"\u6570\u636e\u4e0b\u8f7d", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u4e0b\u8f7d\u4ee3\u7406", None))
        self.SettingProxyTypeCombo.setItemText(0, QCoreApplication.translate("Form", u"\u65e0", None))
        self.SettingProxyTypeCombo.setItemText(1, QCoreApplication.translate("Form", u"http://", None))
        self.SettingProxyTypeCombo.setItemText(2, QCoreApplication.translate("Form", u"socks5://", None))

        self.SettingProxyLabel.setText(QCoreApplication.translate("Form", u":", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"\u4e0b\u8f7d\u8d85\u65f6", None))
        self.label_21.setText(QCoreApplication.translate("Form", u"\u79d2", None))
        self.GB4.setTitle(QCoreApplication.translate("Form", u"\u6587\u672c\u7ffb\u8bd1", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"\u81ea\u52a8\u4fdd\u5b58\u95f4\u9694", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u5206", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u5e94\u7528", None))
    # retranslateUi

