# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WindowDialogStaff.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPlainTextEdit,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_NewStaffDialog(object):
    def setupUi(self, NewStaffDialog):
        if not NewStaffDialog.objectName():
            NewStaffDialog.setObjectName(u"NewStaffDialog")
        NewStaffDialog.resize(500, 350)
        NewStaffDialog.setMinimumSize(QSize(500, 350))
        NewStaffDialog.setMaximumSize(QSize(500, 350))
        NewStaffDialog.setStyleSheet(u"QFrame#MainFrame{background-color: rgb(255, 255, 255);border-radius:20px;}\n"
"QLabel{	font: 10pt \"Microsoft YaHei UI\";}")
        self.gridLayout = QGridLayout(NewStaffDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.MainFrame = QFrame(NewStaffDialog)
        self.MainFrame.setObjectName(u"MainFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MainFrame.sizePolicy().hasHeightForWidth())
        self.MainFrame.setSizePolicy(sizePolicy)
        self.MainFrame.setFrameShape(QFrame.StyledPanel)
        self.MainFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.MainFrame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 35, -1, -1)
        self.widget_7 = QWidget(self.MainFrame)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.frame = QFrame(self.widget_7)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_5 = QWidget(self.frame)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_5 = QLabel(self.widget_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 20))
        self.label_5.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout_6.addWidget(self.label_5)

        self.EditRecord = QLineEdit(self.widget_5)
        self.EditRecord.setObjectName(u"EditRecord")
        self.EditRecord.setMinimumSize(QSize(0, 20))
        self.EditRecord.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout_6.addWidget(self.EditRecord)

        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 1)

        self.verticalLayout.addWidget(self.widget_5)

        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 20))
        self.label.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout.addWidget(self.label)

        self.EditTranslator = QLineEdit(self.widget)
        self.EditTranslator.setObjectName(u"EditTranslator")
        self.EditTranslator.setMinimumSize(QSize(0, 20))
        self.EditTranslator.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout.addWidget(self.EditTranslator)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(self.frame)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 20))
        self.label_2.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout_2.addWidget(self.label_2)

        self.EditTranslateProof = QLineEdit(self.widget_2)
        self.EditTranslateProof.setObjectName(u"EditTranslateProof")
        self.EditTranslateProof.setMinimumSize(QSize(0, 20))
        self.EditTranslateProof.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout_2.addWidget(self.EditTranslateProof)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)

        self.verticalLayout.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.frame)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.widget_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 20))
        self.label_3.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout_4.addWidget(self.label_3)

        self.EditSubMaker = QLineEdit(self.widget_3)
        self.EditSubMaker.setObjectName(u"EditSubMaker")
        self.EditSubMaker.setMinimumSize(QSize(0, 20))
        self.EditSubMaker.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout_4.addWidget(self.EditSubMaker)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 1)

        self.verticalLayout.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.frame)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(self.widget_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 20))
        self.label_4.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout_5.addWidget(self.label_4)

        self.EditSubProof = QLineEdit(self.widget_4)
        self.EditSubProof.setObjectName(u"EditSubProof")
        self.EditSubProof.setMinimumSize(QSize(0, 20))
        self.EditSubProof.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout_5.addWidget(self.EditSubProof)

        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 1)

        self.verticalLayout.addWidget(self.widget_4)


        self.horizontalLayout_8.addWidget(self.frame)

        self.frame_2 = QFrame(self.widget_7)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_2.addWidget(self.label_7)

        self.EditPrefix = QPlainTextEdit(self.frame_2)
        self.EditPrefix.setObjectName(u"EditPrefix")

        self.verticalLayout_2.addWidget(self.EditPrefix)

        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.label_6)

        self.EditSubfix = QPlainTextEdit(self.frame_2)
        self.EditSubfix.setObjectName(u"EditSubfix")

        self.verticalLayout_2.addWidget(self.EditSubfix)

        self.widget_6 = QWidget(self.frame_2)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_8 = QLabel(self.widget_6)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_7.addWidget(self.label_8)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.RadioPos9 = QRadioButton(self.widget_6)
        self.RadioPos9.setObjectName(u"RadioPos9")

        self.gridLayout_2.addWidget(self.RadioPos9, 0, 1, 1, 1)

        self.RadioPos7 = QRadioButton(self.widget_6)
        self.RadioPos7.setObjectName(u"RadioPos7")
        self.RadioPos7.setCheckable(True)
        self.RadioPos7.setChecked(True)

        self.gridLayout_2.addWidget(self.RadioPos7, 0, 0, 1, 1)

        self.RadioPos1 = QRadioButton(self.widget_6)
        self.RadioPos1.setObjectName(u"RadioPos1")

        self.gridLayout_2.addWidget(self.RadioPos1, 1, 0, 1, 1)

        self.RadioPos3 = QRadioButton(self.widget_6)
        self.RadioPos3.setObjectName(u"RadioPos3")

        self.gridLayout_2.addWidget(self.RadioPos3, 1, 1, 1, 1)


        self.horizontalLayout_7.addLayout(self.gridLayout_2)


        self.verticalLayout_2.addWidget(self.widget_6)


        self.horizontalLayout_8.addWidget(self.frame_2)

        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(1, 1)

        self.verticalLayout_3.addWidget(self.widget_7)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.widget_8 = QWidget(self.MainFrame)
        self.widget_8.setObjectName(u"widget_8")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_8.sizePolicy().hasHeightForWidth())
        self.widget_8.setSizePolicy(sizePolicy1)
        self.horizontalLayout_9 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.widget_8)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_9.addWidget(self.label_9)

        self.EditDuration = QLineEdit(self.widget_8)
        self.EditDuration.setObjectName(u"EditDuration")
        self.EditDuration.setMinimumSize(QSize(50, 0))
        self.EditDuration.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_9.addWidget(self.EditDuration)


        self.horizontalLayout_3.addWidget(self.widget_8)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.ButtonImport = QPushButton(self.MainFrame)
        self.ButtonImport.setObjectName(u"ButtonImport")

        self.horizontalLayout_3.addWidget(self.ButtonImport)

        self.ButtonExport = QPushButton(self.MainFrame)
        self.ButtonExport.setObjectName(u"ButtonExport")

        self.horizontalLayout_3.addWidget(self.ButtonExport)

        self.ButtonSubmit = QPushButton(self.MainFrame)
        self.ButtonSubmit.setObjectName(u"ButtonSubmit")

        self.horizontalLayout_3.addWidget(self.ButtonSubmit)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.gridLayout.addWidget(self.MainFrame, 0, 0, 1, 1)


        self.retranslateUi(NewStaffDialog)

        QMetaObject.connectSlotsByName(NewStaffDialog)
    # setupUi

    def retranslateUi(self, NewStaffDialog):
        NewStaffDialog.setWindowTitle(QCoreApplication.translate("NewStaffDialog", u"Dialog", None))
        self.label_5.setText(QCoreApplication.translate("NewStaffDialog", u"\u5f55\u5236", None))
        self.label.setText(QCoreApplication.translate("NewStaffDialog", u"\u7ffb\u8bd1", None))
        self.label_2.setText(QCoreApplication.translate("NewStaffDialog", u"\u6821\u5bf9", None))
        self.label_3.setText(QCoreApplication.translate("NewStaffDialog", u"\u65f6\u8f74", None))
        self.EditSubMaker.setText(QCoreApplication.translate("NewStaffDialog", u"SekaiSubtitle", None))
        self.label_4.setText(QCoreApplication.translate("NewStaffDialog", u"\u8f74\u6821/\u538b\u5236", None))
        self.label_7.setText(QCoreApplication.translate("NewStaffDialog", u"\u524d\u7f00\u5185\u5bb9", None))
        self.EditPrefix.setPlainText(QCoreApplication.translate("NewStaffDialog", u"\u5b57\u5e55\u5236\u4f5c by PJS\u5b57\u5e55\u7ec4", None))
        self.label_6.setText(QCoreApplication.translate("NewStaffDialog", u"\u540e\u7f00\u5185\u5bb9", None))
        self.label_8.setText(QCoreApplication.translate("NewStaffDialog", u"\u4f4d\u7f6e", None))
        self.RadioPos9.setText(QCoreApplication.translate("NewStaffDialog", u"\u53f3\u4e0a", None))
        self.RadioPos7.setText(QCoreApplication.translate("NewStaffDialog", u"\u5de6\u4e0a", None))
        self.RadioPos1.setText(QCoreApplication.translate("NewStaffDialog", u"\u5de6\u4e0b", None))
        self.RadioPos3.setText(QCoreApplication.translate("NewStaffDialog", u"\u53f3\u4e0b", None))
        self.label_9.setText(QCoreApplication.translate("NewStaffDialog", u"\u65f6\u95f4\u6301\u7eed(s)", None))
        self.EditDuration.setText(QCoreApplication.translate("NewStaffDialog", u"5", None))
        self.ButtonImport.setText(QCoreApplication.translate("NewStaffDialog", u"\u5bfc\u5165", None))
        self.ButtonExport.setText(QCoreApplication.translate("NewStaffDialog", u"\u5bfc\u51fa", None))
        self.ButtonSubmit.setText(QCoreApplication.translate("NewStaffDialog", u"\u5e94\u7528", None))
    # retranslateUi

