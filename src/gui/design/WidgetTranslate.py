# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WidgetTranslate.ui'
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
    QLabel, QLineEdit, QListView, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(671, 374)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setStyleSheet(u"QListWidget{ background-color: rgba(255, 255, 255, 0); border: none;outline:0px;}\n"
"                QListWidget::item{background-color: rgba(255, 255, 255, 0); border: none;outline:0px;}\n"
"                QFrame#MainFrame{background-color: rgb(255, 255, 255);border-radius:20px;}\n"
"                QPushButton{max-width:50px}\n"
"            ")
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.MainFrame = QFrame(Form)
        self.MainFrame.setObjectName(u"MainFrame")
        self.MainFrame.setFrameShape(QFrame.StyledPanel)
        self.MainFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.MainFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(self.MainFrame)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(3, 3, 3, 3)
        self.ButtonLoad = QPushButton(self.frame)
        self.ButtonLoad.setObjectName(u"ButtonLoad")
        self.ButtonLoad.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout.addWidget(self.ButtonLoad)

        self.ButtonClear = QPushButton(self.frame)
        self.ButtonClear.setObjectName(u"ButtonClear")
        self.ButtonClear.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout.addWidget(self.ButtonClear)

        self.ButtonOpen = QPushButton(self.frame)
        self.ButtonOpen.setObjectName(u"ButtonOpen")
        self.ButtonOpen.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout.addWidget(self.ButtonOpen)

        self.ButtonSave = QPushButton(self.frame)
        self.ButtonSave.setObjectName(u"ButtonSave")
        self.ButtonSave.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout.addWidget(self.ButtonSave)


        self.horizontalLayout_3.addWidget(self.frame)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.LabeiTitle = QLabel(self.widget)
        self.LabeiTitle.setObjectName(u"LabeiTitle")

        self.horizontalLayout_3.addWidget(self.LabeiTitle)

        self.EditTitle = QLineEdit(self.widget)
        self.EditTitle.setObjectName(u"EditTitle")

        self.horizontalLayout_3.addWidget(self.EditTitle)


        self.verticalLayout.addWidget(self.widget)

        self.ListWidgetLine = QListWidget(self.MainFrame)
        self.ListWidgetLine.setObjectName(u"ListWidgetLine")
        self.ListWidgetLine.setMinimumSize(QSize(340, 0))
        self.ListWidgetLine.setLineWidth(0)
        self.ListWidgetLine.setResizeMode(QListView.Adjust)

        self.verticalLayout.addWidget(self.ListWidgetLine)


        self.gridLayout.addWidget(self.MainFrame, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.ButtonLoad.setText(QCoreApplication.translate("Form", u"\u8f7d\u5165", None))
        self.ButtonClear.setText(QCoreApplication.translate("Form", u"\u6e05\u9664", None))
        self.ButtonOpen.setText(QCoreApplication.translate("Form", u"\u6253\u5f00", None))
        self.ButtonSave.setText(QCoreApplication.translate("Form", u"\u4fdd\u5b58", None))
        self.LabeiTitle.setText(QCoreApplication.translate("Form", u"\u6807\u9898", None))
    # retranslateUi

