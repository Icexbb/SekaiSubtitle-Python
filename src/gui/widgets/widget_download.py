import json
import os
import time

from PySide6 import QtWidgets

from gui.thread_download import DownloadThread
from gui.widgets.qt_downloadWidget import Ui_DownloadWidget
from lib.data import chara_name
from script.tools import save_json, read_json


class DownloadWidget(Ui_DownloadWidget, QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__()
        self.receive_data = None
        self.downloadState = None
        self.setupUi(self)
        self.parent = parent
        self.root = os.getcwd()
        self.download_url = None
        self.RefreshButton.clicked.connect(self.load_data_list)
        self.DataSourceBox.currentTextChanged.connect(self.change_source)
        self.DataTypeBox.currentTextChanged.connect(self.change_type)
        self.DataPeriodBox.currentTextChanged.connect(self.change_period)
        self.DataEpisodeBox.currentTextChanged.connect(self.change_episode)
        self.msgbox = QtWidgets.QMessageBox(self)
        self.msgbox.setWindowTitle("消息")
        self.msgbox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)

    @property
    def proxy(self) -> str:
        return self.parent.proxy

    def load_data_list(self):
        source = self.DataSourceBox.currentIndex()

        def update_ai_data(type_name: str, json_url: str):
            ai_root = os.path.join(self.root, "data/pjsekai/tree")
            os.makedirs(ai_root, exist_ok=True)
            json_path = os.path.join(ai_root, f"{type_name}.json")
            json_data = read_json(json_path)
            skip = len(json_data.get("data")) if json_data.get("data") else 0
            json_url = f"{json_url}&$skip={skip}"
            if self.download_json(json_url):
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
            if self.download_json(json_url):
                json_data += self.receive_data
                save_json(json_path, json_data)
                return json_data
            else:
                assert False, f"Get {type_name} Info Error"

        def update_source_ai():
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
                "eventStories",
                "https://api.pjsek.ai/database/master/eventStories?$limit=20&&$sort[eventId]=-1"
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

        def update_source_best():
            events = update_best_data(
                "events", "https://sekai-world.github.io/sekai-master-db-diff/events.json"
            )
            cards = update_best_data(
                "cards", "https://sekai-world.github.io/sekai-master-db-diff/cards.json"
            )

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

        self.RefreshButton.setText("获取中")
        self.RefreshButton.setEnabled(False)
        try:
            update_source_best()
            update_source_ai()
        except Exception as e:
            self.RefreshButton.setText("获取失败")
            print(e, e.args)
        else:
            self.RefreshButton.setText("获取成功")
        finally:
            time.sleep(1)
            self.RefreshButton.setEnabled(True)

    def download_check(self, status):
        if status:
            self.downloadState = 1
        else:
            self.msgbox.setText("下载失败，请检查代理设置")
            self.msgbox.exec()
            self.downloadState = 2

    def download_json(self, json_url):
        download = DownloadThread(json_url, self.proxy)
        download.trigger.connect(self.download_check)
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

    def load_tree_data(self):
        source = self.DataSourceBox.currentIndex()
        if source == 1:  # pjsekai
            p = os.path.join(self.root, "data/pjsekai/tree/tree.json")
            data = read_json(p)
            if data and "data" in data:
                data = data["data"]
        else:
            p = os.path.join(self.root, "data/best/tree/tree.json")
            data = read_json(p)
        return data

    def change_source(self) -> None:
        data = self.load_tree_data()
        if data:
            self.DataTypeBox.clear()
            for key in data:
                self.DataTypeBox.addItem(key)
            self.DataTypeBox.repaint()

    def change_type(self):
        data = self.load_tree_data()
        if data:
            type_key = self.DataTypeBox.currentText()
            self.DataPeriodBox.clear()
            for key in data[type_key]:
                self.DataPeriodBox.addItem(key)
            self.DataPeriodBox.repaint()
        else:
            self.DataTypeBox.clear()

    def change_period(self):
        data = self.load_tree_data()
        if data:
            type_key = self.DataTypeBox.currentText()
            period_key = self.DataPeriodBox.currentText()

            self.DataEpisodeBox.clear()
            for key in data[type_key][period_key]:
                self.DataEpisodeBox.addItem(key)
            self.DataEpisodeBox.repaint()
        else:
            self.DataPeriodBox.clear()

    def change_episode(self):
        data = self.load_tree_data()
        if data:
            type_key = self.DataTypeBox.currentText()
            period_key = self.DataPeriodBox.currentText()
            episode_key = self.DataEpisodeBox.currentText()
            if type_key and period_key and episode_key:
                self.download_url = data[type_key][period_key][episode_key]
        else:
            self.download_url = None