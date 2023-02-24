# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WindowDialogStartup.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QLabel,
    QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(218, 218)
        Dialog.setMinimumSize(QSize(218, 218))
        Dialog.setMaximumSize(QSize(218, 218))
        Dialog.setStyleSheet(u"QDialog{background-color: rgb(255, 255, 255);}\n"
"")
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.IconLabel = QLabel(Dialog)
        self.IconLabel.setObjectName(u"IconLabel")
        self.IconLabel.setMinimumSize(QSize(200, 200))
        self.IconLabel.setMaximumSize(QSize(200, 200))
        self.IconLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.IconLabel, 0, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.IconLabel.setText(QCoreApplication.translate("Dialog", u"Sekai Subtitle", None))
    # retranslateUi

