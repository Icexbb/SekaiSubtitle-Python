import json
import os
import sys

from PySide6 import QtWidgets, QtCore
from PySide6.QtGui import QCloseEvent

from gui.mainGUI import Ui_Sekai_Subtitle
from progress import VideoProcessThread, ProgressBar


class SekaiSubtitleMain(QtWidgets.QMainWindow, Ui_Sekai_Subtitle):

    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.setting = None
        self.root = os.path.realpath(os.path.join(os.path.split(os.path.abspath(sys.argv[0]))[0], "../"))
        self.setting_file = os.path.join(self.root, "data/setting.json")
        os.makedirs(os.path.join(self.root, "data"), exist_ok=True)
        self.setting_load()

        # subtitle
        # subtitle video select
        self.subtitle_video_selected = None
        self.subtitle_button_video_select.clicked.connect(self.subtitle_open_video)
        # subtitle json select
        self.subtitle_json_data = None
        self.subtitle_json_selected = None
        self.subtitle_button_json_load.clicked.connect(self.subtitle_open_json)
        # subtitle start
        self.subtitle_buttom_insert.clicked.connect(self.subtitle_task_insert)
        self.subtitle_button_start.clicked.connect(self.subtitle_task_start)
        self.subtitle_text_count = None
        self.subtitle_processing = None
        self.subtitle_progress.setValue(0)
        self.subtitle_task_list: list[VideoProcessThread] = []
        self.subtitle_task_wait: list[VideoProcessThread] = []
        self.subtitle_task_processing: list[VideoProcessThread] = []
        self.subtitle_task_finished: list[VideoProcessThread] = []
        self.subtitle_list_tasks.clicked.connect(self.subtitle_show_info)
        self.subtitle_process_item: ProgressBar | None = None
        # setting
        self.setting_button_save.clicked.connect(self.setting_save)
        # thread
        # self.update_thread.start()
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_label)
        self.timer.start()

    def subtitle_show_info(self, i: QtCore.QModelIndex):
        self.subtitle_process_item = None
        self.subtitle_text_processing.clear()
        item = self.subtitle_list_tasks.item(i.row())
        processor_bar: ProgressBar = self.subtitle_list_tasks.itemWidget(item)
        self.subtitle_process_item = processor_bar

    def subtitle_task_insert(self):
        self.subtitle_text_processing.clear()
        if self.subtitle_json_selected and self.subtitle_video_selected:
            item = QtWidgets.QListWidgetItem()
            item.setSizeHint(QtCore.QSize(240, 60))
            processor = VideoProcessThread(
                self.subtitle_video_selected, self.subtitle_json_selected)
            self.subtitle_video_selected = None
            self.subtitle_json_selected = None
            self.subtitle_list_tasks.addItem(item)
            self.subtitle_list_tasks.setItemWidget(item, processor.bar)
            self.subtitle_task_list.append(processor)
            if self.subtitle_task_count == 1:
                self.subtitle_process_item = processor.bar
                self.subtitle_text_count = 0

        else:
            not_type = []
            if not self.subtitle_video_selected:
                not_type.append("视频文件")
            if not self.subtitle_json_selected:
                not_type.append("数据文件")
            QtWidgets.QMessageBox.warning(
                self, "错误", "、".join(not_type) + "未选择",
                QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.Yes)

    def subtitle_task_start(self):
        while self.subtitle_task_list:
            processor = self.subtitle_task_list.pop()
            if len(self.subtitle_task_processing) < self.thread_limit:
                processor.start()
                processor.started = 1
                self.subtitle_task_processing.append(processor)
            else:
                processor.signal_data.emit({'type': int, "data": 3})
                self.subtitle_task_wait.append(processor)

    def update_label(self) -> None:
        self.subtitle_text_processing.clear()
        self.subtitle_text_processing.verticalScrollBar().setHidden(True)
        if self.subtitle_process_item:
            for line in self.subtitle_process_item.strings:
                self.subtitle_text_processing.insertPlainText(f"{line}\n")
            self.subtitle_text_processing.verticalScrollBar().setValue(
                self.subtitle_text_processing.verticalScrollBar().maximum()
            )

        self.subtitle_text_processing.repaint()
        if self.subtitle_video_selected:
            subtitle_video_name = os.path.split(self.subtitle_video_selected)[-1]
            self.subtitle_label_video_name.setText(subtitle_video_name)
        else:
            self.subtitle_label_video_name.setText("未选择")
        self.subtitle_label_video_name.repaint()
        if self.subtitle_json_selected:
            subtitle_json_name = os.path.split(self.subtitle_json_selected)[-1]
            self.subtitle_label_json_name.setText(subtitle_json_name)
        else:
            self.subtitle_label_json_name.setText("未选择")
        self.subtitle_label_json_name.repaint()
        if self.subtitle_task_processing:
            self.subtitle_processing = True
        while len(self.subtitle_task_processing) < self.thread_limit:
            if self.subtitle_task_wait:
                processor = self.subtitle_task_wait.pop()
                processor.start()
                processor.started = 1
                self.subtitle_task_processing.append(processor)
            else:
                break
        processing = []
        while self.subtitle_task_processing:
            processor = self.subtitle_task_processing.pop()
            if processor.started == 2:
                self.subtitle_task_finished.append(processor)
            elif processor.started == 1:
                processing.append(processor)
        self.subtitle_task_processing = processing

    def subtitle_open_video(self):
        file_name_choose, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, "选取文件", dir=self.root, filter="视频文件 (*.mp4 *.avi *.wmv *.mkv);;全部文件 (*)"
        )
        self.subtitle_video_selected = file_name_choose if file_name_choose else None
        if self.subtitle_video_selected:
            video_dir, video_file = os.path.split(self.subtitle_video_selected)
            default_json_file = os.path.join(video_dir, f"{os.path.splitext(video_file)[0]}.json")
            if os.path.exists(default_json_file):
                self.subtitle_json_selected = default_json_file

    def subtitle_open_json(self):
        if self.subtitle_combo_json_source.currentIndex() == 0:
            file_name_choose, _ = QtWidgets.QFileDialog.getOpenFileName(
                self, "选取文件", dir=self.root, filter="世界计划剧情文件 (*.json);;全部文件 (*)"
            )
            self.subtitle_json_selected = file_name_choose if file_name_choose else None
            self.subtitle_json_data = json.load(open(self.subtitle_json_selected, 'r', encoding='utf8')) \
                if file_name_choose else None

    def setting_load(self):
        if os.path.exists(self.setting_file):
            with open(self.setting_file, 'r', encoding='utf8') as fp:
                self.setting = json.load(fp)
        else:
            self.setting = {}
        self.setting_text_proxy.setText(
            self.setting["proxy"] if "proxy" in self.setting and self.setting["proxy"] else "")
        self.setting_text_thread.setText(
            str(self.setting['thread_limit']) if "thread_limit" in self.setting and self.setting['thread_limit'] else ""
        )

    def setting_get(self, key: str):
        self.setting_load()
        return self.setting.get(key)

    def setting_save(self):
        proxy = self.setting_text_proxy.text()
        thread_limit = int(self.setting_text_thread.text())
        self.setting['proxy'] = proxy if proxy else None
        self.setting['thread_limit'] = thread_limit if thread_limit else 4
        with open(self.setting_file, 'w', encoding='utf8') as fp:
            json.dump(self.setting, fp, indent=4, ensure_ascii=False)
        self.setting_load()

    @property
    def proxy(self):
        return self.setting_get("proxy")

    @property
    def thread_limit(self):
        return self.setting_get("thread_limit") or 4

    @property
    def subtitle_task_count(self):
        return len(self.subtitle_task_processing + self.subtitle_task_wait +
                   self.subtitle_task_list + self.subtitle_task_finished)

    def closeEvent(self, event: QCloseEvent) -> None:
        self.subtitle_processing = False
        for bar in self.subtitle_task_processing:
            bar.processing = False


def main():
    app = QtWidgets.QApplication(sys.argv)
    main = SekaiSubtitleMain()
    main.show()
    app.exec()


if __name__ == '__main__':
    main()
