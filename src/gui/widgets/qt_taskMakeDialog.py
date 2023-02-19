# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WindowDialogNewSubTask.ui'
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
    QHBoxLayout, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_NewSubProcessDialog(object):
    def setupUi(self, NewSubProcessDialog):
        if not NewSubProcessDialog.objectName():
            NewSubProcessDialog.setObjectName(u"NewSubProcessDialog")
        NewSubProcessDialog.resize(500, 300)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(NewSubProcessDialog.sizePolicy().hasHeightForWidth())
        NewSubProcessDialog.setSizePolicy(sizePolicy)
        NewSubProcessDialog.setMinimumSize(QSize(500, 300))
        NewSubProcessDialog.setMaximumSize(QSize(500, 300))
        self.gridLayout = QGridLayout(NewSubProcessDialog)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.MainFrame = QFrame(NewSubProcessDialog)
        self.MainFrame.setObjectName(u"MainFrame")
        self.MainFrame.setEnabled(True)
        self.MainFrame.setStyleSheet(u"QFrame#MainFrame{background-color: rgb(255, 255, 255);border-color: rgb(204, 204, 204);border-size: 2px;border-radius:20px;}\n"
"QLabel{font: 12pt \"Microsoft YaHei UI\";}\n"
"QGroupBox{background-color: rgba(204, 204, 204,50);border-color: rgb(204, 204, 204);border-size: 1px;border-radius:20px;}")
        self.verticalLayout = QVBoxLayout(self.MainFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 35, -1, -1)
        self.SelectBox = QFrame(self.MainFrame)
        self.SelectBox.setObjectName(u"SelectBox")
        self.SelectBoxLayout = QVBoxLayout(self.SelectBox)
        self.SelectBoxLayout.setObjectName(u"SelectBoxLayout")

        self.verticalLayout.addWidget(self.SelectBox)

        self.EmitFrame = QFrame(self.MainFrame)
        self.EmitFrame.setObjectName(u"EmitFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.EmitFrame.sizePolicy().hasHeightForWidth())
        self.EmitFrame.setSizePolicy(sizePolicy1)
        self.EmitFrame.setFrameShape(QFrame.StyledPanel)
        self.EmitFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.EmitFrame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.EmitButton = QPushButton(self.EmitFrame)
        self.EmitButton.setObjectName(u"EmitButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.EmitButton.sizePolicy().hasHeightForWidth())
        self.EmitButton.setSizePolicy(sizePolicy2)

        self.horizontalLayout_4.addWidget(self.EmitButton)


        self.verticalLayout.addWidget(self.EmitFrame)

        self.verticalLayout.setStretch(1, 1)

        self.gridLayout.addWidget(self.MainFrame, 0, 0, 1, 1)


        self.retranslateUi(NewSubProcessDialog)

        QMetaObject.connectSlotsByName(NewSubProcessDialog)
    # setupUi

    def retranslateUi(self, NewSubProcessDialog):
        NewSubProcessDialog.setWindowTitle(QCoreApplication.translate("NewSubProcessDialog", u"Dialog", None))
        self.EmitButton.setText(QCoreApplication.translate("NewSubProcessDialog", u"\u5f00\u59cb\uff01", None))
    # retranslateUi

