# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'video_progress.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QHBoxLayout, QLabel,
    QProgressBar, QSizePolicy, QSpacerItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(240, 60)
        Form.setMinimumSize(QSize(200, 60))
        Form.setMaximumSize(QSize(240, 60))
        self.formLayout = QFormLayout(Form)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(3)
        self.formLayout.setVerticalSpacing(3)
        self.formLayout.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_process_status = QLabel(Form)
        self.label_process_status.setObjectName(u"label_process_status")

        self.horizontalLayout_3.addWidget(self.label_process_status)

        self.horizontalSpacer_2 = QSpacerItem(5, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.label_video_name = QLabel(Form)
        self.label_video_name.setObjectName(u"label_video_name")
        self.label_video_name.setMinimumSize(QSize(30, 20))
        self.label_video_name.setMaximumSize(QSize(160, 20))
        self.label_video_name.setScaledContents(False)

        self.horizontalLayout_3.addWidget(self.label_video_name)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout_3.addWidget(self.label)

        self.label_process_fps = QLabel(Form)
        self.label_process_fps.setObjectName(u"label_process_fps")
        self.label_process_fps.setMinimumSize(QSize(40, 0))
        self.label_process_fps.setMaximumSize(QSize(40, 20))
        self.label_process_fps.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_process_fps)


        self.horizontalLayout_2.addLayout(self.horizontalLayout_3)


        self.formLayout.setLayout(0, QFormLayout.FieldRole, self.horizontalLayout_2)

        self.bar_progress = QProgressBar(Form)
        self.bar_progress.setObjectName(u"bar_progress")
        self.bar_progress.setEnabled(True)
        self.bar_progress.setMinimumSize(QSize(0, 20))
        self.bar_progress.setValue(0)
        self.bar_progress.setTextVisible(True)
        self.bar_progress.setInvertedAppearance(False)
        self.bar_progress.setTextDirection(QProgressBar.TopToBottom)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.bar_progress)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_process_status.setText(QCoreApplication.translate("Form", u"\u672a\u5f00\u59cb", None))
        self.label_video_name.setText(QCoreApplication.translate("Form", u"\u6587\u4ef6\u540d", None))
        self.label.setText(QCoreApplication.translate("Form", u"FPS:", None))
        self.label_process_fps.setText(QCoreApplication.translate("Form", u"0", None))
        self.bar_progress.setFormat(QCoreApplication.translate("Form", u"%p%", None))
    # retranslateUi

