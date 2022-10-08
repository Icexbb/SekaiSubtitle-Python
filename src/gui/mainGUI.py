# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFormLayout,
    QHBoxLayout, QHeaderView, QLabel, QLayout,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QProgressBar, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QTabWidget, QTableView, QTextBrowser,
    QVBoxLayout, QWidget)

class Ui_Sekai_Subtitle(object):
    def setupUi(self, Sekai_Subtitle):
        if not Sekai_Subtitle.objectName():
            Sekai_Subtitle.setObjectName(u"Sekai_Subtitle")
        Sekai_Subtitle.resize(800, 425)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Sekai_Subtitle.sizePolicy().hasHeightForWidth())
        Sekai_Subtitle.setSizePolicy(sizePolicy)
        Sekai_Subtitle.setMinimumSize(QSize(800, 300))
        Sekai_Subtitle.setBaseSize(QSize(800, 300))
        self.widget_main = QWidget(Sekai_Subtitle)
        self.widget_main.setObjectName(u"widget_main")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_main.sizePolicy().hasHeightForWidth())
        self.widget_main.setSizePolicy(sizePolicy1)
        self.widget_main.setAutoFillBackground(True)
        self.Main = QFormLayout(self.widget_main)
        self.Main.setSpacing(5)
        self.Main.setContentsMargins(5, 5, 5, 5)
        self.Main.setObjectName(u"Main")
        self.Main.setHorizontalSpacing(0)
        self.Main.setVerticalSpacing(0)
        self.Main.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.widget_main)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(50, 0))
        self.subtitle_widget = QWidget()
        self.subtitle_widget.setObjectName(u"subtitle_widget")
        self.subtitle_widget.setEnabled(True)
        self.formLayout_3 = QFormLayout(self.subtitle_widget)
        self.formLayout_3.setSpacing(5)
        self.formLayout_3.setContentsMargins(5, 5, 5, 5)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setContentsMargins(6, 6, 6, 6)
        self.gridWidget = QWidget(self.subtitle_widget)
        self.gridWidget.setObjectName(u"gridWidget")
        self.verticalLayout_6 = QVBoxLayout(self.gridWidget)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setSizeConstraint(QLayout.SetMaximumSize)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.vbox_subtitle_setting = QHBoxLayout()
        self.vbox_subtitle_setting.setSpacing(5)
        self.vbox_subtitle_setting.setObjectName(u"vbox_subtitle_setting")
        self.vbox_subtitle_setting.setSizeConstraint(QLayout.SetMinimumSize)
        self.vbox_subtitle_setting.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetMinimumSize)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setSizeConstraint(QLayout.SetMinimumSize)
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(5)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setSizeConstraint(QLayout.SetMinimumSize)
        self.subtitle_label_video_video = QLabel(self.gridWidget)
        self.subtitle_label_video_video.setObjectName(u"subtitle_label_video_video")
        self.subtitle_label_video_video.setMinimumSize(QSize(75, 22))
        self.subtitle_label_video_video.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout_12.addWidget(self.subtitle_label_video_video)

        self.subtitle_label_video_name = QLabel(self.gridWidget)
        self.subtitle_label_video_name.setObjectName(u"subtitle_label_video_name")
        self.subtitle_label_video_name.setMinimumSize(QSize(0, 22))

        self.horizontalLayout_12.addWidget(self.subtitle_label_video_name)

        self.subtitle_button_video_select = QPushButton(self.gridWidget)
        self.subtitle_button_video_select.setObjectName(u"subtitle_button_video_select")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.subtitle_button_video_select.sizePolicy().hasHeightForWidth())
        self.subtitle_button_video_select.setSizePolicy(sizePolicy2)
        self.subtitle_button_video_select.setMinimumSize(QSize(75, 22))
        self.subtitle_button_video_select.setMaximumSize(QSize(75, 24))

        self.horizontalLayout_12.addWidget(self.subtitle_button_video_select)


        self.horizontalLayout_7.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setSpacing(5)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setSizeConstraint(QLayout.SetMinimumSize)
        self.subtitle_label_json_json = QLabel(self.gridWidget)
        self.subtitle_label_json_json.setObjectName(u"subtitle_label_json_json")
        self.subtitle_label_json_json.setMinimumSize(QSize(75, 22))
        self.subtitle_label_json_json.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout_13.addWidget(self.subtitle_label_json_json)

        self.subtitle_label_json_name = QLabel(self.gridWidget)
        self.subtitle_label_json_name.setObjectName(u"subtitle_label_json_name")
        self.subtitle_label_json_name.setMinimumSize(QSize(0, 22))

        self.horizontalLayout_13.addWidget(self.subtitle_label_json_name)

        self.subtitle_combo_json_source = QComboBox(self.gridWidget)
        self.subtitle_combo_json_source.addItem("")
        self.subtitle_combo_json_source.addItem("")
        self.subtitle_combo_json_source.addItem("")
        self.subtitle_combo_json_source.setObjectName(u"subtitle_combo_json_source")
        self.subtitle_combo_json_source.setMinimumSize(QSize(75, 22))
        self.subtitle_combo_json_source.setMaximumSize(QSize(75, 22))

        self.horizontalLayout_13.addWidget(self.subtitle_combo_json_source)

        self.subtitle_button_json_load = QPushButton(self.gridWidget)
        self.subtitle_button_json_load.setObjectName(u"subtitle_button_json_load")
        self.subtitle_button_json_load.setMinimumSize(QSize(75, 22))
        self.subtitle_button_json_load.setMaximumSize(QSize(75, 24))

        self.horizontalLayout_13.addWidget(self.subtitle_button_json_load)


        self.horizontalLayout_7.addLayout(self.horizontalLayout_13)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setSpacing(5)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setSizeConstraint(QLayout.SetMinimumSize)
        self.subtitle_combo_type = QComboBox(self.gridWidget)
        self.subtitle_combo_type.setObjectName(u"subtitle_combo_type")
        self.subtitle_combo_type.setEnabled(True)
        self.subtitle_combo_type.setMinimumSize(QSize(75, 22))
        self.subtitle_combo_type.setMaximumSize(QSize(75, 22))
        self.subtitle_combo_type.setFocusPolicy(Qt.WheelFocus)
        self.subtitle_combo_type.setAutoFillBackground(False)
        self.subtitle_combo_type.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.subtitle_combo_type.setFrame(True)

        self.horizontalLayout_14.addWidget(self.subtitle_combo_type)

        self.subtitle_combo_source = QComboBox(self.gridWidget)
        self.subtitle_combo_source.setObjectName(u"subtitle_combo_source")
        self.subtitle_combo_source.setMinimumSize(QSize(75, 22))
        self.subtitle_combo_source.setMaximumSize(QSize(300, 22))
        self.subtitle_combo_source.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.subtitle_combo_source.setFrame(True)

        self.horizontalLayout_14.addWidget(self.subtitle_combo_source)

        self.subtitle_combo_episode = QComboBox(self.gridWidget)
        self.subtitle_combo_episode.setObjectName(u"subtitle_combo_episode")
        self.subtitle_combo_episode.setMinimumSize(QSize(75, 22))
        self.subtitle_combo_episode.setMaximumSize(QSize(300, 22))
        self.subtitle_combo_episode.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.subtitle_combo_episode.setFrame(True)

        self.horizontalLayout_14.addWidget(self.subtitle_combo_episode)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_4)

        self.subtitle_button_flush_list = QPushButton(self.gridWidget)
        self.subtitle_button_flush_list.setObjectName(u"subtitle_button_flush_list")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.subtitle_button_flush_list.sizePolicy().hasHeightForWidth())
        self.subtitle_button_flush_list.setSizePolicy(sizePolicy3)
        self.subtitle_button_flush_list.setMinimumSize(QSize(75, 22))
        self.subtitle_button_flush_list.setMaximumSize(QSize(75, 22))

        self.horizontalLayout_14.addWidget(self.subtitle_button_flush_list)


        self.verticalLayout_3.addLayout(self.horizontalLayout_14)


        self.vbox_subtitle_setting.addLayout(self.verticalLayout_3)

        self.subtitle_buttom_insert = QPushButton(self.gridWidget)
        self.subtitle_buttom_insert.setObjectName(u"subtitle_buttom_insert")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.subtitle_buttom_insert.sizePolicy().hasHeightForWidth())
        self.subtitle_buttom_insert.setSizePolicy(sizePolicy4)
        self.subtitle_buttom_insert.setMinimumSize(QSize(25, 0))
        self.subtitle_buttom_insert.setMaximumSize(QSize(75, 45))

        self.vbox_subtitle_setting.addWidget(self.subtitle_buttom_insert)


        self.verticalLayout_6.addLayout(self.vbox_subtitle_setting)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setSpacing(5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.subtitle_list_tasks = QListWidget(self.gridWidget)
        self.subtitle_list_tasks.setObjectName(u"subtitle_list_tasks")
        self.subtitle_list_tasks.setEnabled(True)
        self.subtitle_list_tasks.setMinimumSize(QSize(250, 0))
        self.subtitle_list_tasks.setMaximumSize(QSize(250, 16777215))

        self.verticalLayout_11.addWidget(self.subtitle_list_tasks)

        self.subtitle_button_start = QPushButton(self.gridWidget)
        self.subtitle_button_start.setObjectName(u"subtitle_button_start")

        self.verticalLayout_11.addWidget(self.subtitle_button_start)


        self.horizontalLayout_4.addLayout(self.verticalLayout_11)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.subtitle_text_processing = QTextBrowser(self.gridWidget)
        self.subtitle_text_processing.setObjectName(u"subtitle_text_processing")
        self.subtitle_text_processing.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_7.addWidget(self.subtitle_text_processing)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(5)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label = QLabel(self.gridWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_9.addWidget(self.label)

        self.subtitle_progress = QProgressBar(self.gridWidget)
        self.subtitle_progress.setObjectName(u"subtitle_progress")
        self.subtitle_progress.setValue(0)

        self.horizontalLayout_9.addWidget(self.subtitle_progress)


        self.verticalLayout_7.addLayout(self.horizontalLayout_9)


        self.horizontalLayout_4.addLayout(self.verticalLayout_7)

        self.horizontalLayout_4.setStretch(0, 2)
        self.horizontalLayout_4.setStretch(1, 5)

        self.verticalLayout_6.addLayout(self.horizontalLayout_4)


        self.formLayout_3.setWidget(0, QFormLayout.SpanningRole, self.gridWidget)

        self.tabWidget.addTab(self.subtitle_widget, "")
        self.translate_widget = QWidget()
        self.translate_widget.setObjectName(u"translate_widget")
        self.formLayout_2 = QFormLayout(self.translate_widget)
        self.formLayout_2.setSpacing(5)
        self.formLayout_2.setContentsMargins(5, 5, 5, 5)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetMaximumSize)
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(5)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setSpacing(5)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setSizeConstraint(QLayout.SetMinimumSize)
        self.translate_combo_type = QComboBox(self.translate_widget)
        self.translate_combo_type.addItem("")
        self.translate_combo_type.addItem("")
        self.translate_combo_type.addItem("")
        self.translate_combo_type.addItem("")
        self.translate_combo_type.setObjectName(u"translate_combo_type")
        self.translate_combo_type.setEnabled(True)
        self.translate_combo_type.setMinimumSize(QSize(75, 22))
        self.translate_combo_type.setMaximumSize(QSize(75, 22))
        self.translate_combo_type.setFocusPolicy(Qt.WheelFocus)
        self.translate_combo_type.setAutoFillBackground(False)
        self.translate_combo_type.setFrame(True)

        self.horizontalLayout_15.addWidget(self.translate_combo_type)

        self.translate_combo_source = QComboBox(self.translate_widget)
        self.translate_combo_source.setObjectName(u"translate_combo_source")
        self.translate_combo_source.setMinimumSize(QSize(75, 22))
        self.translate_combo_source.setMaximumSize(QSize(100, 22))

        self.horizontalLayout_15.addWidget(self.translate_combo_source)

        self.translate_combo_episode = QComboBox(self.translate_widget)
        self.translate_combo_episode.setObjectName(u"translate_combo_episode")
        self.translate_combo_episode.setMinimumSize(QSize(75, 22))
        self.translate_combo_episode.setMaximumSize(QSize(150, 22))

        self.horizontalLayout_15.addWidget(self.translate_combo_episode)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer)

        self.translate_button_flush = QPushButton(self.translate_widget)
        self.translate_button_flush.setObjectName(u"translate_button_flush")
        sizePolicy3.setHeightForWidth(self.translate_button_flush.sizePolicy().hasHeightForWidth())
        self.translate_button_flush.setSizePolicy(sizePolicy3)
        self.translate_button_flush.setMinimumSize(QSize(75, 22))
        self.translate_button_flush.setMaximumSize(QSize(75, 22))

        self.horizontalLayout_15.addWidget(self.translate_button_flush)


        self.verticalLayout_2.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setSpacing(5)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setSizeConstraint(QLayout.SetMinimumSize)
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.translate_label_json = QLabel(self.translate_widget)
        self.translate_label_json.setObjectName(u"translate_label_json")
        self.translate_label_json.setMinimumSize(QSize(0, 22))
        self.translate_label_json.setMaximumSize(QSize(16777215, 22))

        self.horizontalLayout_16.addWidget(self.translate_label_json)

        self.translate_combo_json_source = QComboBox(self.translate_widget)
        self.translate_combo_json_source.addItem("")
        self.translate_combo_json_source.addItem("")
        self.translate_combo_json_source.addItem("")
        self.translate_combo_json_source.setObjectName(u"translate_combo_json_source")
        self.translate_combo_json_source.setMinimumSize(QSize(75, 22))
        self.translate_combo_json_source.setMaximumSize(QSize(75, 22))

        self.horizontalLayout_16.addWidget(self.translate_combo_json_source)

        self.translate_button_json_load = QPushButton(self.translate_widget)
        self.translate_button_json_load.setObjectName(u"translate_button_json_load")
        self.translate_button_json_load.setMinimumSize(QSize(40, 22))
        self.translate_button_json_load.setMaximumSize(QSize(50, 22))

        self.horizontalLayout_16.addWidget(self.translate_button_json_load)


        self.verticalLayout_2.addLayout(self.horizontalLayout_16)


        self.verticalLayout_9.addLayout(self.verticalLayout_2)

        self.translate_table_json = QTableView(self.translate_widget)
        self.translate_table_json.setObjectName(u"translate_table_json")

        self.verticalLayout_9.addWidget(self.translate_table_json)


        self.horizontalLayout_3.addLayout(self.verticalLayout_9)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.translate_radio_trans = QRadioButton(self.translate_widget)
        self.translate_radio_trans.setObjectName(u"translate_radio_trans")
        self.translate_radio_trans.setMinimumSize(QSize(0, 22))
        self.translate_radio_trans.setChecked(True)

        self.horizontalLayout_5.addWidget(self.translate_radio_trans)

        self.translate_radio_check = QRadioButton(self.translate_widget)
        self.translate_radio_check.setObjectName(u"translate_radio_check")
        self.translate_radio_check.setMinimumSize(QSize(0, 22))

        self.horizontalLayout_5.addWidget(self.translate_radio_check)

        self.translate_radio_mean = QRadioButton(self.translate_widget)
        self.translate_radio_mean.setObjectName(u"translate_radio_mean")
        self.translate_radio_mean.setMinimumSize(QSize(0, 22))

        self.horizontalLayout_5.addWidget(self.translate_radio_mean)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.translate_label_title = QLabel(self.translate_widget)
        self.translate_label_title.setObjectName(u"translate_label_title")

        self.horizontalLayout_6.addWidget(self.translate_label_title)

        self.translate_line_title = QLineEdit(self.translate_widget)
        self.translate_line_title.setObjectName(u"translate_line_title")
        self.translate_line_title.setMinimumSize(QSize(0, 22))

        self.horizontalLayout_6.addWidget(self.translate_line_title)

        self.translate_button_open = QPushButton(self.translate_widget)
        self.translate_button_open.setObjectName(u"translate_button_open")
        self.translate_button_open.setMinimumSize(QSize(40, 22))
        self.translate_button_open.setMaximumSize(QSize(50, 22))

        self.horizontalLayout_6.addWidget(self.translate_button_open)

        self.translate_button_save = QPushButton(self.translate_widget)
        self.translate_button_save.setObjectName(u"translate_button_save")
        self.translate_button_save.setMinimumSize(QSize(40, 22))
        self.translate_button_save.setMaximumSize(QSize(50, 22))

        self.horizontalLayout_6.addWidget(self.translate_button_save)

        self.translate_button_clear = QPushButton(self.translate_widget)
        self.translate_button_clear.setObjectName(u"translate_button_clear")
        self.translate_button_clear.setMinimumSize(QSize(40, 22))
        self.translate_button_clear.setMaximumSize(QSize(50, 22))

        self.horizontalLayout_6.addWidget(self.translate_button_clear)

        self.translate_button_check = QPushButton(self.translate_widget)
        self.translate_button_check.setObjectName(u"translate_button_check")
        self.translate_button_check.setMinimumSize(QSize(40, 22))
        self.translate_button_check.setMaximumSize(QSize(50, 22))

        self.horizontalLayout_6.addWidget(self.translate_button_check)


        self.verticalLayout_5.addLayout(self.horizontalLayout_6)


        self.horizontalLayout_8.addLayout(self.verticalLayout_5)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.translate_check_fore = QCheckBox(self.translate_widget)
        self.translate_check_fore.setObjectName(u"translate_check_fore")

        self.verticalLayout_4.addWidget(self.translate_check_fore)

        self.translate_check_enter = QCheckBox(self.translate_widget)
        self.translate_check_enter.setObjectName(u"translate_check_enter")
        self.translate_check_enter.setChecked(True)

        self.verticalLayout_4.addWidget(self.translate_check_enter)


        self.horizontalLayout_8.addLayout(self.verticalLayout_4)


        self.verticalLayout_8.addLayout(self.horizontalLayout_8)

        self.translate_table_text = QTableView(self.translate_widget)
        self.translate_table_text.setObjectName(u"translate_table_text")

        self.verticalLayout_8.addWidget(self.translate_table_text)


        self.horizontalLayout_3.addLayout(self.verticalLayout_8)

        self.horizontalLayout_3.setStretch(0, 2)
        self.horizontalLayout_3.setStretch(1, 3)

        self.formLayout_2.setLayout(0, QFormLayout.SpanningRole, self.horizontalLayout_3)

        self.tabWidget.addTab(self.translate_widget, "")
        self.setting_widget = QWidget()
        self.setting_widget.setObjectName(u"setting_widget")
        self.formLayout = QFormLayout(self.setting_widget)
        self.formLayout.setSpacing(5)
        self.formLayout.setContentsMargins(5, 5, 5, 5)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.setting_label_proxy = QLabel(self.setting_widget)
        self.setting_label_proxy.setObjectName(u"setting_label_proxy")

        self.horizontalLayout.addWidget(self.setting_label_proxy)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.setting_text_proxy = QLineEdit(self.setting_widget)
        self.setting_text_proxy.setObjectName(u"setting_text_proxy")

        self.horizontalLayout.addWidget(self.setting_text_proxy)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(5)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(5, 5, 5, 5)
        self.setting_label_thread = QLabel(self.setting_widget)
        self.setting_label_thread.setObjectName(u"setting_label_thread")

        self.horizontalLayout_10.addWidget(self.setting_label_thread)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_5)

        self.setting_text_thread = QLineEdit(self.setting_widget)
        self.setting_text_thread.setObjectName(u"setting_text_thread")

        self.horizontalLayout_10.addWidget(self.setting_text_thread)


        self.verticalLayout.addLayout(self.horizontalLayout_10)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.setting_button_default = QPushButton(self.setting_widget)
        self.setting_button_default.setObjectName(u"setting_button_default")

        self.horizontalLayout_2.addWidget(self.setting_button_default)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.setting_button_save = QPushButton(self.setting_widget)
        self.setting_button_save.setObjectName(u"setting_button_save")

        self.horizontalLayout_2.addWidget(self.setting_button_save)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.formLayout.setLayout(0, QFormLayout.SpanningRole, self.verticalLayout)

        self.tabWidget.addTab(self.setting_widget, "")

        self.Main.setWidget(0, QFormLayout.SpanningRole, self.tabWidget)

        Sekai_Subtitle.setCentralWidget(self.widget_main)

        self.retranslateUi(Sekai_Subtitle)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Sekai_Subtitle)
    # setupUi

    def retranslateUi(self, Sekai_Subtitle):
        Sekai_Subtitle.setWindowTitle(QCoreApplication.translate("Sekai_Subtitle", u"Sekai \u8f74\u59ec", None))
        self.subtitle_label_video_video.setText(QCoreApplication.translate("Sekai_Subtitle", u"\u89c6\u9891\u6587\u4ef6\uff1a", None))
        self.subtitle_label_video_name.setText(QCoreApplication.translate("Sekai_Subtitle", u"\u672a\u9009\u62e9", None))
        self.subtitle_button_video_select.setText(QCoreApplication.translate("Sekai_Subtitle", u"\u9009\u62e9", None))
        self.subtitle_label_json_json.setText(QCoreApplication.translate("Sekai_Subtitle", u"\u6570\u636e\u6587\u4ef6\uff1a", None))
        self.subtitle_label_json_name.setText(QCoreApplication.translate("Sekai_Subtitle", u"\u672a\u9009\u62e9", None))
        self.subtitle_combo_json_source.setItemText(0, QCoreApplication.translate("Sekai_Subtitle", u"\u672c\u5730\u8f7d\u5165", None))
        self.subtitle_combo_json_source.setItemText(1, QCoreApplication.translate("Sekai_Subtitle", u"Ai\u7ad9", None))
        self.subtitle_combo_json_source.setItemText(2, QCoreApplication.translate("Sekai_Subtitle", u"Best\u7ad9", None))

        self.subtitle_button_json_load.setText(QCoreApplication.translate("Sekai_Subtitle", u"\u8f7d\u5165", None))
        self.subtitle_button_flush_list.setText(QCoreApplication.translate("Sekai_Subtitle", u"\u5237\u65b0", None))
        self.subtitle_buttom_insert.setText(QCoreApplication.translate("Sekai_Subtitle", u"\u52a0\u5165\u961f\u5217", None))
        self.subtitle_button_start.setText(QCoreApplication.translate("Sekai_Subtitle", u"\u5f00\u59cb\u5904\u7406", None))
        self.label.setText(QCoreApplication.translate("Sekai_Subtitle", u"\u603b\u8fdb\u5ea6", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.subtitle_widget), QCoreApplication.translate("Sekai_Subtitle", u"\u8f74\u673a", None))
        self.translate_combo_type.setItemText(0, QCoreApplication.translate("Sekai_Subtitle", u"\u4e3b\u7ebf\u5267\u60c5", None))
        self.translate_combo_type.setItemText(1, QCoreApplication.translate("Sekai_Subtitle", u"\u6d3b\u52a8\u5267\u60c5", None))
        self.translate_combo_type.setItemText(2, QCoreApplication.translate("Sekai_Subtitle", u"\u7279\u6b8a\u5267\u60c5", None))
        self.translate_combo_type.setItemText(3, QCoreApplication.translate("Sekai_Subtitle", u"\u5361\u9762\u5267\u60c5", None))

        self.translate_button_flush.setText(QCoreApplication.translate("Sekai_Subtitle", u"\u5237\u65b0", None))
        self.translate_label_json.setText(QCoreApplication.translate("Sekai_Subtitle", u"\u6570\u636e\u6587\u4ef6\uff1a", None))
        self.translate_combo_json_source.setItemText(0, QCoreApplication.translate("Sekai_Subtitle", u"\u672c\u5730\u8f7d\u5165", None))
        self.translate_combo_json_source.setItemText(1, QCoreApplication.translate("Sekai_Subtitle", u"\u81ea\u52a8\u83b7\u53d6\uff1apjsek.ai", None))
        self.translate_combo_json_source.setItemText(2, QCoreApplication.translate("Sekai_Subtitle", u"\u81ea\u52a8\u83b7\u53d6\uff1asekai.best", None))

        self.translate_button_json_load.setText(QCoreApplication.translate("Sekai_Subtitle", u"\u8f7d\u5165", None))
        self.translate_radio_trans.setText(QCoreApplication.translate("Sekai_Subtitle", u"\u7ffb\u8bd1", None))
        self.translate_radio_check.setText(QCoreApplication.translate("Sekai_Subtitle", u"\u6821\u5bf9", None))
        self.translate_radio_mean.setText(QCoreApplication.translate("Sekai_Subtitle", u"\u5408\u610f", None))
        self.translate_label_title.setText(QCoreApplication.translate("Sekai_Subtitle", u"\u6807\u9898\uff1a", None))
        self.translate_button_open.setText(QCoreApplication.translate("Sekai_Subtitle", u"\u6253\u5f00", None))
        self.translate_button_save.setText(QCoreApplication.translate("Sekai_Subtitle", u"\u4fdd\u5b58", None))
        self.translate_button_clear.setText(QCoreApplication.translate("Sekai_Subtitle", u"\u6e05\u7a7a", None))
        self.translate_button_check.setText(QCoreApplication.translate("Sekai_Subtitle", u"\u68c0\u67e5", None))
        self.translate_check_fore.setText(QCoreApplication.translate("Sekai_Subtitle", u"\u663e\u793a\u4fee\u6539\u524d\u5185\u5bb9", None))
        self.translate_check_enter.setText(QCoreApplication.translate("Sekai_Subtitle", u"\u4fdd\u5b58\u6362\u884c\u7b26", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.translate_widget), QCoreApplication.translate("Sekai_Subtitle", u"\u7ffb\u8bd1", None))
        self.setting_label_proxy.setText(QCoreApplication.translate("Sekai_Subtitle", u"\u4ee3\u7406", None))
        self.setting_label_thread.setText(QCoreApplication.translate("Sekai_Subtitle", u"\u7ebf\u7a0b", None))
        self.setting_button_default.setText(QCoreApplication.translate("Sekai_Subtitle", u"\u6062\u590d\u9ed8\u8ba4", None))
        self.setting_button_save.setText(QCoreApplication.translate("Sekai_Subtitle", u"\u4fdd\u5b58", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.setting_widget), QCoreApplication.translate("Sekai_Subtitle", u"\u8bbe\u7f6e", None))
    # retranslateUi

