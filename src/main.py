import json
import logging
import os
import sys
import time

from PySide6 import QtWidgets, QtCore
from PySide6.QtGui import QCloseEvent

from gui.mainGUI import Ui_Sekai_Subtitle
from lib.data import chara_name
from progress import VideoProcessThread, ProgressBar
from threads import DownloadThread


def read_json(path, alt=None):
    if alt is None:
        alt = {}
    if os.path.exists(path):
        return json.load(open(path, 'r', encoding="utf8"))
    else:
        return alt


def save_json(path, data):
    return json.dump(data, open(path, 'w', encoding="utf8"), ensure_ascii=False, indent=4)


class SekaiSubtitleMain(QtWidgets.QMainWindow, Ui_Sekai_Subtitle):

    def __init__(self):
        super().__init__()

        self.subtitle_fitting_file_selected = None
        self.setupUi(self)
        self.setting = None
        self.root = os.path.realpath(os.path.join(os.path.split(os.path.abspath(sys.argv[0]))[0], "../"))
        self.setting_file = os.path.join(self.root, "data/setting.json")
        os.makedirs(os.path.join(self.root, "data"), exist_ok=True)
        self.setting_load(True)

        # subtitle
        # subtitle video select
        self.subtitle_video_selected = None
        self.subtitle_button_video_select.clicked.connect(self.subtitle_open_video)
        self.subtitle_button_video_select_dir.clicked.connect(self.subtitle_open_video_dir)
        # subtitle json select
        self.subtitle_json_data = None
        self.subtitle_json_selected = None
        self.subtitle_button_json_load.clicked.connect(self.subtitle_open_json)
        # subtitle start
        self.subtitle_buttom_insert.clicked.connect(self.subtitle_task_insert)
        self.subtitle_button_start.clicked.connect(self.subtitle_task_start)
        self.subtitle_button_flush_list.clicked.connect(self.network_update_tree)
        self.subtitle_button_clear_list.clicked.connect(self.subtitle_list_clear)
        self.subtitle_button_video_clear.clicked.connect(self.subtitle_clear_video)
        self.subtitle_button_json_clear.clicked.connect(self.subtitle_clear_json)
        self.subtitle_button_json_clear_online.clicked.connect(self.subtitle_clear_json)
        self.subtitle_button_json_load_online.clicked.connect(self.subtitle_load_json_online)
        self.subtitle_list_tasks.clicked.connect(self.subtitle_show_info)
        self.subtitle_button_fitting_select.clicked.connect(self.subtitle_open_fitting)
        self.subtitle_button_fitting_clear.clicked.connect(self.subtitle_clear_fitting)
        self.subtitle_text_count = None
        self.subtitle_processing = None
        self.subtitle_progress.setValue(0)
        self.subtitle_task_list: list[VideoProcessThread] = []
        self.subtitle_task_wait: list[VideoProcessThread] = []
        self.subtitle_task_processing: list[VideoProcessThread] = []
        self.subtitle_task_finished: list[VideoProcessThread] = []
        self.subtitle_process_item: ProgressBar | None = None
        self.subtitle_json_selected_network = None
        self.receive_data = None

        # setting
        self.setting_button_save.clicked.connect(self.setting_save)
        # self.update_thread.start()
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_content)
        self.timer.start()
        self.msgbox = QtWidgets.QMessageBox(self)
        self.msgbox.setWindowTitle("消息")
        self.msgbox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        self.downloadState = None

    def subtitle_show_info(self, i: QtCore.QModelIndex):
        self.subtitle_process_item = None
        self.subtitle_text_processing.clear()
        item = self.subtitle_list_tasks.item(i.row())
        processor_bar: ProgressBar = self.subtitle_list_tasks.itemWidget(item)
        self.subtitle_process_item = processor_bar

    def subtitle_insert_task(self, json_path, video_path, fitting_file):
        item = QtWidgets.QListWidgetItem()
        item.setSizeHint(QtCore.QSize(240, 60))
        processor = VideoProcessThread(video_path, json_path, fitting_file)
        self.subtitle_list_tasks.addItem(item)
        self.subtitle_list_tasks.setItemWidget(item, processor.bar)
        self.subtitle_task_list.append(processor)
        if self.subtitle_task_count == 1:
            self.subtitle_text_processing.clear()
            self.subtitle_process_item = processor.bar
            self.subtitle_text_count = 0

    def subtitle_task_insert(self):
        if self.subtitle_json_selected and self.subtitle_video_selected and \
                ((self.subtitle_fitting_box.isChecked() and self.subtitle_fitting_file_selected)
                 or not self.subtitle_fitting_box.isChecked()):
            self.subtitle_insert_task(self.subtitle_json_selected, self.subtitle_video_selected,
                                      self.subtitle_fitting_file_selected)
            self.subtitle_video_selected = None
            self.subtitle_json_selected = None
            self.subtitle_fitting_file_selected = None
        else:
            not_type = []
            if not self.subtitle_video_selected:
                not_type.append("视频文件")
            if not self.subtitle_json_selected:
                not_type.append("数据文件")
            if self.subtitle_fitting_box.isChecked() and not self.subtitle_fitting_file_selected:
                not_type.append("合意文件")
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

    def subtitle_list_clear(self):
        self.subtitle_list_tasks.clear()
        self.subtitle_task_list: list[VideoProcessThread] = []
        self.subtitle_task_wait: list[VideoProcessThread] = []
        self.subtitle_task_processing: list[VideoProcessThread] = []
        self.subtitle_task_finished: list[VideoProcessThread] = []
        self.subtitle_processing = False
        self.subtitle_text_processing.clear()
        self.subtitle_process_item = None
        for bar in self.subtitle_task_processing:
            bar.processing = False

    def subtitle_open_video_dir(self):
        dir_path = QtWidgets.QFileDialog.getExistingDirectory(self, "选取文件夹", dir=self.root)
        file_list = os.listdir(dir_path)
        count = 0
        for file in file_list:
            file_real_path = os.path.join(dir_path, file)
            if os.path.isfile(file_real_path) and os.path.splitext(file)[-1] in [".mp4", ".avi", ".wmv", ".mkv"]:
                video_file = file_real_path
                json_file = None
                default_json_file = os.path.join(dir_path, f"{os.path.splitext(file)[0]}.json")
                if os.path.exists(default_json_file):
                    json_file = default_json_file
                if json_file:
                    self.subtitle_insert_task(json_file, video_file, None)
                    count += 1
        if count:
            self.msgbox.setText(f"自动导入了文件夹中的{count}个视频任务")
        else:
            self.msgbox.setText(f"未找到视频任务<br>请确保json文件与视频文件同名")
        self.msgbox.show()

    def subtitle_clear_video(self):
        self.subtitle_video_selected = None

    def subtitle_clear_json(self):
        self.subtitle_json_selected = None

    def subtitle_clear_fitting(self):
        self.subtitle_fitting_file_selected = None

    def subtitle_open_fitting(self):
        file_name_choose, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, "选取文件", dir=self.root, filter="世界计划翻译文件 (*.txt);;全部文件 (*)"
        )
        self.subtitle_fitting_file_selected = file_name_choose if file_name_choose else None

    def subtitle_open_json(self):
        source = self.subtitle_combo_json_source.currentIndex()
        if not source:
            file_name_choose, _ = QtWidgets.QFileDialog.getOpenFileName(
                self, "选取文件", dir=self.root, filter="世界计划剧情文件 (*.json);;全部文件 (*)"
            )
            self.subtitle_json_selected = file_name_choose if file_name_choose else None

    def subtitle_load_json_online(self):
        self.subtitle_button_json_load_online.setEnabled(False)
        self.subtitle_button_json_load_online.setText("下载中")

        source = self.subtitle_combo_json_source.currentIndex()
        if source and self.subtitle_json_selected_network:
            from urllib.parse import urlsplit
            url = self.subtitle_json_selected_network
            name = os.path.split(urlsplit(url).path)[-1]
            s = "pjsekai" if source == 1 else "best"
            root = os.path.join(self.root, f"data/{s}/source/")
            os.makedirs(root, exist_ok=True)
            path = os.path.join(root, name)
            self.subtitle_button_json_load_online.setText("下载中")
            self.subtitle_button_json_load_online.setEnabled(False)
            if self.network_download_json(url):
                data = self.receive_data
                save_json(path, data)
                file_name_choose = path
                self.subtitle_json_selected = file_name_choose if file_name_choose else None
                self.subtitle_button_json_load_online.setText("成功！")
            else:
                self.subtitle_button_json_load_online.setText("失败！")
            time.sleep(1)
            self.subtitle_button_json_load_online.setText("载入")
            self.subtitle_button_json_load_online.setEnabled(True)

    def setting_load(self, initial=False):
        self.setting = read_json(self.setting_file) or {}
        if initial:
            self.setting_text_proxy.setText(
                self.setting["proxy"] if "proxy" in self.setting and self.setting["proxy"] else "")
            self.setting_text_thread.setText(
                str(self.setting['thread_limit']) if "thread_limit" in self.setting and self.setting[
                    'thread_limit'] else ""
            )

    def setting_get(self, key: str):
        self.setting_load()
        return self.setting.get(key)

    def setting_save(self):
        proxy = self.setting_text_proxy.text() or None
        thread_limit = int(self.setting_text_thread.text()) if self.setting_text_thread.text().isdigit() else 2
        self.setting['proxy'] = proxy if proxy else None
        self.setting['thread_limit'] = thread_limit if thread_limit else 4
        with open(self.setting_file, 'w', encoding='utf8') as fp:
            json.dump(self.setting, fp, indent=4, ensure_ascii=False)
        self.setting_load()

    def update_content(self) -> None:
        self.update_tree()
        self.update_bar()
        self.update_fitting()
        # subtitle text
        self.subtitle_text_processing.clear()
        self.subtitle_text_processing.verticalScrollBar().setHidden(True)
        if self.subtitle_process_item:
            for line in self.subtitle_process_item.strings:
                self.subtitle_text_processing.insertPlainText(line)
            self.subtitle_text_processing.verticalScrollBar().setValue(
                self.subtitle_text_processing.verticalScrollBar().maximum()
            )
        self.subtitle_text_processing.repaint()
        # subtitle video name
        if self.subtitle_video_selected:
            subtitle_video_name = os.path.split(self.subtitle_video_selected)[-1]
            self.subtitle_label_video_name.setText(subtitle_video_name)
        else:
            self.subtitle_label_video_name.setText("未选择")
        self.subtitle_label_video_name.repaint()
        # subtitle json name
        if self.subtitle_json_selected:
            subtitle_json_name = os.path.split(self.subtitle_json_selected)[-1]
            self.subtitle_label_json_name.setText(subtitle_json_name)
        else:
            self.subtitle_label_json_name.setText("未选择")
        self.subtitle_label_json_name.repaint()
        # subtitle tasks
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
        # subtitle task query
        while self.subtitle_task_processing:
            processor = self.subtitle_task_processing.pop()
            if processor.started == 2:
                self.subtitle_task_finished.append(processor)
            elif processor.started == 1:
                processing.append(processor)
        self.subtitle_task_processing = processing

    def update_fitting(self):
        if self.subtitle_fitting_box.isChecked():
            self.subtitle_fitting_widget.setHidden(False)
            if not self.subtitle_fitting_file_selected:
                self.subtitle_label_fitting.setText("未选择")
            else:
                subtitle_fitting_name = os.path.split(self.subtitle_fitting_file_selected)[-1]
                self.subtitle_label_fitting.setText(subtitle_fitting_name)

        else:
            self.subtitle_label_fitting.setText("不进行合意替换")
            self.subtitle_fitting_widget.setHidden(True)
        self.subtitle_label_fitting.repaint()

    def update_bar(self):
        count = 0
        value = 0
        for item in self.subtitle_task_processing + self.subtitle_task_wait + self.subtitle_task_finished:
            value += item.bar.bar_progress.value()
            count += item.bar.bar_progress.maximum()
        if not count:
            count = 1
        self.subtitle_progress.setValue(value)
        self.subtitle_progress.setMaximum(count)

    def update_tree(self) -> None:
        source = self.subtitle_combo_json_source.currentIndex()
        if source:
            self.subtitle_online_group.setHidden(False)
            self.subtitle_offline_group.setHidden(True)
            if source == 1:  # pjsekai
                p = os.path.join(self.root, "data/pjsekai/tree/tree.json")
                data = read_json(p) or {}
                if data and "data" in data:
                    data = data["data"]
            else:
                p = os.path.join(self.root, "data/best/tree/tree.json")
                data = read_json(p) or {}
            if data:
                all_type = [self.subtitle_combo_type.itemText(i) for i in range(self.subtitle_combo_type.count())]
                if all_type == list(data.keys()):
                    pass
                else:
                    self.subtitle_combo_type.clear()
                    for key in data:
                        self.subtitle_combo_type.addItem(key)
                type_key = self.subtitle_combo_type.currentText()
                if type_key and type_key in data:
                    all_source = [self.subtitle_combo_source.itemText(i) for i in
                                  range(self.subtitle_combo_source.count())]
                    if all_source == list(data[type_key].keys()):
                        pass
                    else:
                        self.subtitle_combo_source.clear()
                        for key in data[type_key]:
                            self.subtitle_combo_source.addItem(key)
                else:
                    self.subtitle_combo_source.clear()

                s_key = self.subtitle_combo_source.currentText()
                if s_key and s_key in data[type_key]:
                    all_eps = [self.subtitle_combo_episode.itemText(i) for i in
                               range(self.subtitle_combo_episode.count())]
                    if all_eps == list(data[type_key][s_key].keys()):
                        pass
                    else:
                        self.subtitle_combo_episode.clear()
                        for key in data[type_key][s_key]:
                            self.subtitle_combo_episode.addItem(key)
                else:
                    self.subtitle_combo_episode.clear()

                ep_key = self.subtitle_combo_episode.currentText()
                if ep_key and ep_key in data[type_key][s_key]:
                    self.subtitle_json_selected_network = data[type_key][s_key][ep_key]
                else:
                    self.subtitle_json_selected_network = None
            else:
                self.subtitle_combo_type.clear()
                self.subtitle_combo_source.clear()
                self.subtitle_combo_episode.clear()
        else:
            self.subtitle_online_group.setHidden(True)
            self.subtitle_offline_group.setHidden(False)
            self.subtitle_combo_type.clear()
            self.subtitle_combo_source.clear()
            self.subtitle_combo_episode.clear()
        self.subtitle_combo_type.repaint()
        self.subtitle_combo_source.repaint()
        self.subtitle_combo_episode.repaint()

    def network_update_tree(self):
        def update_ai_data(type_name: str, json_url: str):
            ai_root = os.path.join(self.root, "data/pjsekai/tree")
            os.makedirs(ai_root, exist_ok=True)
            json_path = os.path.join(ai_root, f"{type_name}.json")
            json_data = read_json(json_path)
            skip = len(json_data.get("data")) if json_data.get("data") else 0
            json_url = f"{json_url}&$skip={skip}"
            if self.network_download_json(json_url):
                receive = self.receive_data
                if json_data:
                    json_data['data'] += receive['data']
                else:
                    json_data = receive
                save_json(json_path, json_data)
                if json_data and "data" in json_data:
                    json_data = json_data["data"]
                return json_data
            else:
                assert False, f"Get {type_name} Info Error"

        def update_best_data(type_name: str, json_url: str):
            best_root = os.path.join(self.root, "data/best/tree")
            os.makedirs(best_root, exist_ok=True)
            json_path = os.path.join(best_root, f"{type_name}.json")
            json_data = read_json(json_path, [])
            if self.network_download_json(json_url):
                json_data += self.receive_data
                save_json(json_path, json_data)
                return json_data
            else:
                assert False, f"Get {type_name} Info Error"

        source = self.subtitle_combo_json_source.currentIndex()
        if source:
            self.subtitle_button_flush_list.setText("获取中")
            self.subtitle_button_flush_list.setEnabled(False)
            try:
                if source == 1:  # pjsekai
                    events = update_ai_data("events", "https://api.pjsek.ai/database/master/events?$limit=200")
                    cards = update_ai_data("cards", "https://api.pjsek.ai/database/master/cards?$limit=1000")

                    result = {}
                    data = update_ai_data(
                        "unitStories", "https://api.pjsek.ai/database/master/unitStories?$limit=20&$sort[seq]=1")
                    result['主线剧情'] = {}
                    for unit in data:
                        for chapters in unit['chapters']:
                            eps = {}
                            for episodes in chapters["episodes"]:
                                key = f"{episodes['episodeNoLabel']}: {episodes['title']}"
                                url = "https://assets.pjsek.ai/file/pjsekai-assets/startapp/scenario/unitstory/" + \
                                      f"{chapters['assetbundleName']}/{episodes['scenarioId']}.json"
                                eps[key] = url
                            result['主线剧情'][chapters['title']] = eps

                    data = update_ai_data(
                        "eventStories", "https://api.pjsek.ai/database/master/eventStories?$limit=20&&$sort[eventId]=-1"
                    )
                    result['活动剧情'] = {
                        f"{item['eventId']}:{events[item['eventId']]['name']}": {
                            f"{ep['episodeNo']}: {ep['title']}":
                                f"https://assets.pjsek.ai/file/pjsekai-assets/ondemand/event_story/" +
                                f"{item['assetbundleName']}/scenario/{ep['scenarioId']}.json"
                            for ep in item["eventStoryEpisodes"]
                        }
                        for item in data
                    }

                    data = update_ai_data(
                        "cardEpisodes",
                        "https://api.pjsek.ai/database/master/cardEpisodes?$limit=2000&$sort[cardId]=-1&$sort[seq]=1"
                    )
                    result['卡牌剧情'] = {}
                    for ep in data:
                        card_id = ep['cardId']
                        card = [card for card in cards if card['id'] == card_id][0]
                        chara = chara_name[str(card['characterId'])]
                        rarity = f"★{card['cardRarityType'][7:]}" if card['cardRarityType'][7:].isdigit() else "BD"
                        prefix = card['prefix']
                        section = "前篇" if ep['cardEpisodePartType'] == "first_part" else "后篇"
                        url = f"https://assets.pjsek.ai/file/pjsekai-assets/startapp/character/member/" \
                              f"{ep['assetbundleName']}/{ep['scenarioId']}.json"

                        if chara in result['卡牌剧情']:
                            d = result['卡牌剧情'][chara]
                        else:
                            d = {}
                        d[f"{rarity} {prefix} {section}"] = url
                        result['卡牌剧情'][chara] = d

                    path = os.path.join(os.path.join(self.root, "data/pjsekai/tree"), "tree.json")
                    json.dump(result, open(path, 'w', encoding='utf8'), ensure_ascii=False, indent=4)
                else:  # sekai.best
                    events = update_best_data("events",
                                              "https://sekai-world.github.io/sekai-master-db-diff/events.json")
                    cards = update_best_data("cards", "https://sekai-world.github.io/sekai-master-db-diff/cards.json")

                    result = {}
                    data = update_best_data("unitStories",
                                            "https://sekai-world.github.io/sekai-master-db-diff/unitStories.json")
                    result['主线剧情'] = {}
                    for unit in data:
                        for chapters in unit['chapters']:
                            eps = {}
                            for episodes in chapters["episodes"]:
                                key = f"{episodes['episodeNoLabel']}: {episodes['title']}"
                                url = "https://assets.pjsek.ai/file/pjsekai-assets/startapp/scenario/unitstory/" + \
                                      f"{chapters['assetbundleName']}/{episodes['scenarioId']}.json"
                                eps[key] = url
                            result['主线剧情'][chapters['title']] = eps

                    data = update_best_data("eventStories",
                                            "https://sekai-world.github.io/sekai-master-db-diff/eventStories.json")
                    result['活动剧情'] = {}
                    for event in data:
                        t = [ev for ev in events if ev["id"] == event['eventId']]
                        event_data = t[0] if len(t) else None
                        key = f"{event['eventId']}" + f": {event_data['name']}" if event_data else ""
                        value = {
                            f"{ep['episodeNo']}: {ep['title']}":
                                f"https://assets.pjsek.ai/file/pjsekai-assets/ondemand/event_story/" +
                                f"{event['assetbundleName']}/scenario/{ep['scenarioId']}.json"
                            for ep in event["eventStoryEpisodes"]
                        }
                        result["活动剧情"][key] = value

                    data = update_best_data("cardEpisodes",
                                            "https://sekai-world.github.io/sekai-master-db-diff/cardEpisodes.json")
                    result['卡牌剧情'] = {}
                    for ep in data:
                        card_id = ep['cardId']
                        card = [card for card in cards if card['id'] == card_id][0]
                        chara = chara_name[str(card['characterId'])]
                        rarity = "★" + card['cardRarityType'][7:] if card['cardRarityType'][7:].isdigit() else "BD"
                        prefix = card['prefix']
                        section = "前篇" if ep['cardEpisodePartType'] == "first_part" else "后篇"
                        url = f"https://assets.pjsek.ai/file/pjsekai-assets/startapp/character/member/" \
                              f"{ep['assetbundleName']}/{ep['scenarioId']}.json"

                        if chara in result['卡牌剧情']:
                            d = result['卡牌剧情'][chara]
                        else:
                            d = {}
                        d[f"{rarity} {prefix} {section}"] = url
                        result['卡牌剧情'][chara] = d

                    path = os.path.join(os.path.join(self.root, "data/best/tree"), "tree.json")
                    json.dump(result, open(path, 'w', encoding='utf8'), ensure_ascii=False, indent=4)
                self.msgbox.setText("更新完成")
                self.msgbox.close()
            except Exception as e:
                self.subtitle_button_flush_list.setText("获取失败")
                logging.exception(e)
            else:
                self.subtitle_button_flush_list.setText("获取成功")
            finally:
                time.sleep(1)
                self.subtitle_button_flush_list.setEnabled(True)

    def network_download_check(self, status):
        if status:
            self.downloadState = 1
        else:
            self.msgbox.setStandardButtons(QtWidgets.QMessageBox.Ok)
            self.msgbox.setText("下载失败，请检查代理设置")
            self.msgbox.close()
            self.msgbox.exec()
            self.downloadState = 2

    def network_download_json(self, json_url):
        download = DownloadThread(json_url, self.proxy)
        download.trigger.connect(self.network_download_check)
        download.data.connect(self.network_download_receive)

        self.downloadState = 0

        download.start()
        while not self.downloadState:
            time.sleep(0.1)
            QtWidgets.QApplication.processEvents()
        if self.downloadState == 2:
            return False
        return True

    def network_download_receive(self, data):
        self.receive_data = data['data']

    def network_download_failed(self):
        self.downloadState = 2

    @property
    def proxy(self):
        return self.setting_get("proxy")

    @property
    def thread_limit(self):
        return self.setting_get("thread_limit") or 1

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
    main_ui = SekaiSubtitleMain()
    main_ui.show()
    app.exec()


if __name__ == '__main__':
    main()
