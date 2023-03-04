# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WidgetTranslateIcon.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(120, 62)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(120, 62))
        Form.setMaximumSize(QSize(120, 16777215))
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.LabelIcon = QLabel(Form)
        self.LabelIcon.setObjectName(u"LabelIcon")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.LabelIcon.sizePolicy().hasHeightForWidth())
        self.LabelIcon.setSizePolicy(sizePolicy1)
        self.LabelIcon.setMinimumSize(QSize(55, 55))
        self.LabelIcon.setMaximumSize(QSize(55, 55))
        self.LabelIcon.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.LabelIcon)

        self.LabelName = QLabel(Form)
        self.LabelName.setObjectName(u"LabelName")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.LabelName.sizePolicy().hasHeightForWidth())
        self.LabelName.setSizePolicy(sizePolicy2)
        self.LabelName.setAlignment(Qt.AlignCenter)
        self.LabelName.setWordWrap(True)

        self.horizontalLayout.addWidget(self.LabelName)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.LabelIcon.setText(QCoreApplication.translate("Form", u"Icon", None))
        self.LabelName.setText(QCoreApplication.translate("Form", u"Name", None))
    # retranslateUi

