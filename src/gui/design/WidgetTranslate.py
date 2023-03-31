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
    QListWidgetItem, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(404, 295)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setStyleSheet(u"QListWidget{ background-color: rgba(255, 255, 255, 0); border: none;outline:0px;}\n"
"QListWidget::item{background-color: rgba(255, 255, 255, 0); border: none;outline:0px;}\n"
"QFrame#MainFrame{background-color: rgb(255, 255, 255);border-radius:10px;}\n"
"QPushButton{max-width:50px}\n"
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
        self.ButtonFrame = QFrame(self.widget)
        self.ButtonFrame.setObjectName(u"ButtonFrame")
        self.ButtonFrame.setMinimumSize(QSize(0, 60))
        self.ButtonFrame.setMaximumSize(QSize(16777215, 60))
        self.ButtonFrame.setFrameShape(QFrame.StyledPanel)
        self.ButtonFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.ButtonFrame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(3, 3, 3, 3)
        self.widget_3 = QWidget(self.ButtonFrame)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.ButtonLoad = QPushButton(self.widget_3)
        self.ButtonLoad.setObjectName(u"ButtonLoad")
        self.ButtonLoad.setMaximumSize(QSize(52, 16777215))

        self.horizontalLayout_4.addWidget(self.ButtonLoad)

        self.ButtonClear = QPushButton(self.widget_3)
        self.ButtonClear.setObjectName(u"ButtonClear")
        self.ButtonClear.setMaximumSize(QSize(52, 16777215))

        self.horizontalLayout_4.addWidget(self.ButtonClear)


        self.verticalLayout_3.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.ButtonFrame)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.ButtonOpen = QPushButton(self.widget_4)
        self.ButtonOpen.setObjectName(u"ButtonOpen")
        self.ButtonOpen.setMaximumSize(QSize(52, 16777215))

        self.horizontalLayout_5.addWidget(self.ButtonOpen)

        self.ButtonSave = QPushButton(self.widget_4)
        self.ButtonSave.setObjectName(u"ButtonSave")
        self.ButtonSave.setMaximumSize(QSize(52, 16777215))

        self.horizontalLayout_5.addWidget(self.ButtonSave)


        self.verticalLayout_3.addWidget(self.widget_4)


        self.horizontalLayout_3.addWidget(self.ButtonFrame)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.AutoSaveLabel = QLabel(self.widget)
        self.AutoSaveLabel.setObjectName(u"AutoSaveLabel")

        self.horizontalLayout_3.addWidget(self.AutoSaveLabel)

        self.gridWidget = QWidget(self.widget)
        self.gridWidget.setObjectName(u"gridWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(60)
        sizePolicy1.setHeightForWidth(self.gridWidget.sizePolicy().hasHeightForWidth())
        self.gridWidget.setSizePolicy(sizePolicy1)
        self.gridWidget.setMinimumSize(QSize(200, 60))
        self.gridWidget.setMaximumSize(QSize(200, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.gridWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_2 = QWidget(self.gridWidget)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy2)
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.RadioTrans = QRadioButton(self.widget_2)
        self.RadioTrans.setObjectName(u"RadioTrans")
        self.RadioTrans.setMinimumSize(QSize(0, 15))
        self.RadioTrans.setMaximumSize(QSize(16777215, 15))

        self.horizontalLayout.addWidget(self.RadioTrans)

        self.RadioProof = QRadioButton(self.widget_2)
        self.RadioProof.setObjectName(u"RadioProof")
        self.RadioProof.setMinimumSize(QSize(0, 15))
        self.RadioProof.setMaximumSize(QSize(16777215, 15))

        self.horizontalLayout.addWidget(self.RadioProof)

        self.RadioCheck = QRadioButton(self.widget_2)
        self.RadioCheck.setObjectName(u"RadioCheck")
        self.RadioCheck.setMinimumSize(QSize(0, 15))
        self.RadioCheck.setMaximumSize(QSize(16777215, 15))

        self.horizontalLayout.addWidget(self.RadioCheck)


        self.verticalLayout_2.addWidget(self.widget_2)

        self.horizontalWidget = QWidget(self.gridWidget)
        self.horizontalWidget.setObjectName(u"horizontalWidget")
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.LabeiTitle = QLabel(self.horizontalWidget)
        self.LabeiTitle.setObjectName(u"LabeiTitle")

        self.horizontalLayout_2.addWidget(self.LabeiTitle)

        self.EditTitle = QLineEdit(self.horizontalWidget)
        self.EditTitle.setObjectName(u"EditTitle")

        self.horizontalLayout_2.addWidget(self.EditTitle)


        self.verticalLayout_2.addWidget(self.horizontalWidget)


        self.horizontalLayout_3.addWidget(self.gridWidget)


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
        self.AutoSaveLabel.setText("")
        self.RadioTrans.setText(QCoreApplication.translate("Form", u"\u7ffb\u8bd1", None))
        self.RadioProof.setText(QCoreApplication.translate("Form", u"\u6821\u5bf9", None))
        self.RadioCheck.setText(QCoreApplication.translate("Form", u"\u5408\u610f", None))
        self.LabeiTitle.setText(QCoreApplication.translate("Form", u"\u6807\u9898", None))
    # retranslateUi

