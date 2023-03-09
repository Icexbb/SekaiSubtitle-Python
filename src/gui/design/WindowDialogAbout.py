# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WindowDialogAbout.ui'
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
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(576, 329)
        Dialog.setStyleSheet(u"QLabel#IconLabel{font: 700 12pt \"Microsoft YaHei UI\";}\n"
"                QLabel#GroupLabel{font: 700 12pt \"Microsoft YaHei UI\";}\n"
"                QDialog{background-color:rgb(255, 255, 255)}\n"
"            ")
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.MainFrame = QFrame(Dialog)
        self.MainFrame.setObjectName(u"MainFrame")
        self.MainFrame.setFrameShape(QFrame.StyledPanel)
        self.MainFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.MainFrame)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.IconLabel = QLabel(self.MainFrame)
        self.IconLabel.setObjectName(u"IconLabel")
        self.IconLabel.setMinimumSize(QSize(198, 198))
        self.IconLabel.setMaximumSize(QSize(198, 198))
        self.IconLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.IconLabel)

        self.GroupLabel = QLabel(self.MainFrame)
        self.GroupLabel.setObjectName(u"GroupLabel")
        self.GroupLabel.setMinimumSize(QSize(198, 60))
        self.GroupLabel.setMaximumSize(QSize(198, 60))
        self.GroupLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.GroupLabel)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(20)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.label_2 = QLabel(self.MainFrame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 50))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_2.setFont(font)

        self.verticalLayout_2.addWidget(self.label_2)

        self.line = QFrame(self.MainFrame)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(self.MainFrame)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.LabelVersion = QLabel(self.MainFrame)
        self.LabelVersion.setObjectName(u"LabelVersion")

        self.horizontalLayout.addWidget(self.LabelVersion)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 6)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_7 = QLabel(self.MainFrame)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_3.addWidget(self.label_7)

        self.LabelAuthor = QLabel(self.MainFrame)
        self.LabelAuthor.setObjectName(u"LabelAuthor")

        self.horizontalLayout_3.addWidget(self.LabelAuthor)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 6)

        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_9 = QLabel(self.MainFrame)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_4.addWidget(self.label_9)

        self.LabelPage = QLabel(self.MainFrame)
        self.LabelPage.setObjectName(u"LabelPage")

        self.horizontalLayout_4.addWidget(self.LabelPage)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 6)

        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.UpdateButton = QPushButton(self.MainFrame)
        self.UpdateButton.setObjectName(u"UpdateButton")

        self.horizontalLayout_5.addWidget(self.UpdateButton)

        self.PageButton = QPushButton(self.MainFrame)
        self.PageButton.setObjectName(u"PageButton")

        self.horizontalLayout_5.addWidget(self.PageButton)

        self.CloseButton = QPushButton(self.MainFrame)
        self.CloseButton.setObjectName(u"CloseButton")

        self.horizontalLayout_5.addWidget(self.CloseButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)


        self.gridLayout.addWidget(self.MainFrame, 0, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.IconLabel.setText(QCoreApplication.translate("Dialog", u"Sekai Subtitle", None))
        self.GroupLabel.setText(QCoreApplication.translate("Dialog", u"PJS\u5b57\u5e55\u7ec4", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u5173\u4e8e Sekai Subtitle", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Version", None))
        self.LabelVersion.setText(QCoreApplication.translate("Dialog", u"0.3.0-beta", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Author", None))
        self.LabelAuthor.setText(QCoreApplication.translate("Dialog", u"XBB@PJS\u5b57\u5e55\u7ec4", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"Github", None))
        self.LabelPage.setText(QCoreApplication.translate("Dialog", u"https://github.com/Icexbb/SekaiSubtitle-Python\n"
"                                                            ", None))
        self.UpdateButton.setText(QCoreApplication.translate("Dialog", u"\u68c0\u67e5\u66f4\u65b0", None))
        self.PageButton.setText(QCoreApplication.translate("Dialog", u"\u9879\u76ee\u9996\u9875", None))
        self.CloseButton.setText(QCoreApplication.translate("Dialog", u"\u5173\u95ed", None))
    # retranslateUi

