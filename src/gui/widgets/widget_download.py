import json
import os
import urllib.parse
from urllib import parse

from PySide6 import QtNetwork, QtCore, QtWidgets
from PySide6.QtCore import SIGNAL

from gui.design.WidgetDataDownload import Ui_DownloadWidget
from lib.data import chara_name, areaDict, characterDict
from script.tools import save_json, read_json


class NetworkAccessManager(QtNetwork.QNetworkAccessManager):
    def __init__(self, proxy_addr):
        super().__init__()
        self.proxy_addr = proxy_addr
        if self.proxy_addr:
            proxy_parse = parse.urlparse(self.proxy_addr)

            if proxy_parse.scheme == "http":
                proxy_type = QtNetwork.QNetworkProxy.ProxyType.HttpProxy
            else:
                proxy_type = QtNetwork.QNetworkProxy.ProxyType.Socks5Proxy
            proxy = QtNetwork.QNetworkProxy(proxy_type, proxy_parse.hostname, proxy_parse.port)
            self.setProxy(proxy)


class DownloadWidget(Ui_DownloadWidget, QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__()
        self.receive_data = None
        self.downloadState = None
        self.setupUi(self)
        self.parent = parent
        self.root = os.getcwd()
        self.download_url = None
        self.DownloadButton.clicked.connect(self.download_data)
        self.RefreshButton.clicked.connect(self.load_data_list)

        self.DataSourceBox.currentTextChanged.connect(self.change_source)
        self.DataTypeBox.currentTextChanged.connect(self.change_type)
        self.DataPeriodBox.currentTextChanged.connect(self.change_period)
        self.DataEpisodeBox.currentTextChanged.connect(self.change_episode)

        self.msgbox = QtWidgets.QMessageBox(self)
        self.msgbox.setWindowTitle("消息")
        self.msgbox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        self.change_source()
        self.tree_updater = QtNetwork.QNetworkAccessManager()
        self.connect(self.tree_updater, SIGNAL("finished(QNetworkReply*)"), self.received_list_part)
        self.downloader = QtNetwork.QNetworkAccessManager()
        self.connect(self.downloader, SIGNAL("finished(QNetworkReply*)"), self.received_acquired_data)
        source = self.DataSourceBox.currentIndex()
        self.update_tree("pjsekai" if source else "best")

    @property
    def proxy(self) -> str:
        return self.parent.proxy

    @property
    def nam_proxy(self) -> None | QtNetwork.QNetworkProxy:
        if self.proxy:
            proxy_parse = parse.urlparse(self.proxy)

            if proxy_parse.scheme == "http":
                proxy_type = QtNetwork.QNetworkProxy.ProxyType.HttpProxy
            else:
                proxy_type = QtNetwork.QNetworkProxy.ProxyType.Socks5Proxy
            proxy = QtNetwork.QNetworkProxy(proxy_type, proxy_parse.hostname, proxy_parse.port)
            return proxy

    def load_data_list(self):

        def update_source_ai():
            root = "https://api.pjsek.ai/database/master/"
            events_url = root + "events?$limit=1000"
            cards_url = root + "cards?$limit=1000"
            character2ds_url = root + "character2ds?$limit=1000"
            unitStories_url = root + "unitStories?$limit=1000"
            eventStories_url = root + "eventStories?$limit=1000"
            cardEpisodes_url = root + "cardEpisodes?$limit=2000"
            actionSets_url = root + "actionSets?$limit=3000"
            specialStories_url = root + "specialStories?$limit=1000"

            urls = [events_url, cards_url, character2ds_url, unitStories_url, eventStories_url, cardEpisodes_url,
                    actionSets_url, specialStories_url]
            for url in urls:
                do_request(url)

        def update_source_best():
            root = "https://sekai-world.github.io/sekai-master-db-diff/"
            events_url = root + "events.json"
            cards_url = root + "cards.json"
            character2ds_url = root + "character2ds.json"
            unitStories_url = root + "unitStories.json"
            eventStories_url = root + "eventStories.json"
            cardEpisodes_url = root + "cardEpisodes.json"
            actionSets_url = root + "actionSets.json"
            specialStories_url = root + "specialStories.json"
            urls = [events_url, cards_url, character2ds_url, unitStories_url, eventStories_url, cardEpisodes_url,
                    actionSets_url, specialStories_url]
            for url in urls:
                do_request(url)

        def do_request(url):
            if p := self.nam_proxy:
                self.tree_updater.setProxy(p)
            else:
                self.tree_updater.setProxy()
            self.tree_updater.get(QtNetwork.QNetworkRequest(QtCore.QUrl(url)))

        self.SavePlaceLabel.setText("获取中")
        self.RefreshButton.setEnabled(False)
        source = self.DataSourceBox.currentIndex()
        if source == 0:
            update_source_best()
        else:
            update_source_ai()

    def received_list_part(self, reply: QtNetwork.QNetworkReply):
        url = reply.url().url()
        parse = urllib.parse.urlparse(url)
        if parse.netloc.__contains__("pjsek.ai"):
            source_type = "pjsekai"
        else:
            source_type = "best"
        file: str = os.path.split(parse.path)[-1]
        if not file.endswith("json"):
            file = file + ".json"
        filepath = os.path.join(self.root, "data", source_type, "tree", file)
        if not os.path.exists(os.path.split(filepath)[0]):
            os.makedirs(os.path.split(filepath)[0])
        er = reply.error()
        try:
            if er == QtNetwork.QNetworkReply.NetworkError.NoError:
                bytes_string = reply.readAll()
                data_string = str(bytes_string, 'utf-8')
                data = json.loads(data_string)
                if "data" in data:
                    data = data['data']
                save_json(filepath, data)
                self.SavePlaceLabel.setText(f"Data List Part Saved\n{filepath}")
                self.update_tree(source_type)
            else:
                self.SavePlaceLabel.setText(f"Error occured When Acquiring {file}: {er} \n{reply.errorString()}")
        except json.decoder.JSONDecodeError:
            pass
        finally:
            self.DownloadButton.setEnabled(True)
            self.RefreshButton.setEnabled(True)

    def received_acquired_data(self, reply: QtNetwork.QNetworkReply):
        url = reply.url().url()
        parse = urllib.parse.urlparse(url)
        if parse.netloc.__contains__("pjsek.ai"):
            source_type = "pjsekai"
        else:
            source_type = "best"
        file: str = os.path.split(parse.path)[-1]
        if file.endswith(".asset"):
            file = file.removesuffix(".asset") + ".json"

        filepath = os.path.join(self.root, "data", source_type, "source", file)

        if not os.path.exists(os.path.split(filepath)[0]):
            os.makedirs(os.path.split(filepath)[0])
        try:
            er = reply.error()
            if er == QtNetwork.QNetworkReply.NetworkError.NoError:
                bytes_string = reply.readAll()
                data_string = str(bytes_string, 'utf-8')
                data = json.loads(data_string)
                if "data" in data:
                    data = data['data']
                save_json(filepath, data)
                self.SavePlaceLabel.setText(f"Data Saved\nPath: {filepath}")
            else:
                self.SavePlaceLabel.setText(f"Error occured When Acquiring {file}: {er} \n{reply.errorString()}")
        except json.decoder.JSONDecodeError:
            pass
        finally:
            self.DownloadButton.setEnabled(True)
            self.RefreshButton.setEnabled(True)

    def update_tree(self, source):
        root = os.path.join(self.root, "data", source, "tree")

        if os.path.exists(os.path.join(root, "character2ds.json")):
            character2ds = read_json(os.path.join(root, "character2ds.json"))
        else:
            return
        if os.path.exists(os.path.join(root, "events.json")):
            events = read_json(os.path.join(root, "events.json"))
        else:
            return
        if os.path.exists(os.path.join(root, "cards.json")):
            cards = read_json(os.path.join(root, "cards.json"))
        else:
            return

        if os.path.exists(os.path.join(root, "tree.json")):
            tree = read_json(os.path.join(root, "tree.json"))
        else:
            tree = {}

        if os.path.exists(os.path.join(root, "cardEpisodes.json")):
            data = read_json(os.path.join(root, "cardEpisodes.json"))
            tree['卡牌剧情'] = {}
            for ep in data:
                if "scenarioId" not in ep:
                    continue
                card_id = ep['cardId']
                card = [card for card in cards if card['id'] == card_id][0]
                chara = chara_name[str(card['characterId'])]
                rarity = f"★{card['cardRarityType'][7:]}" if card['cardRarityType'][7:].isdigit() else "BD"
                prefix = card['prefix']
                section = "前篇" if ep['cardEpisodePartType'] == "first_part" else "后篇"
                if source == "pjsekai":
                    url = f"https://assets.pjsek.ai/file/pjsekai-assets/startapp/character/member/" \
                          f"{ep['assetbundleName']}/{ep['scenarioId']}.json"
                else:
                    url = f"https://storage.sekai.best/sekai-assets/character/member/" \
                          f"{ep['assetbundleName']}_rip/{ep['scenarioId']}.asset"
                if chara in tree['卡牌剧情']:
                    d = tree['卡牌剧情'][chara]
                else:
                    d = {}
                d[f"{rarity} {prefix} {section}"] = url
                tree['卡牌剧情'][chara] = d

        if os.path.exists(os.path.join(root, "eventStories.json")):
            data = read_json(os.path.join(root, "eventStories.json"))
            tree['活动剧情'] = {}
            for item in data:
                try:
                    ev_name = f"{item['eventId']}:{events[item['eventId']]['name']}"
                except IndexError:
                    ev_name = f"Event{item['eventId']}"
                ev_ep = {}
                for ep in item["eventStoryEpisodes"]:
                    if source == "best":
                        url = f"https://storage.sekai.best/sekai-assets/event_story/" \
                              f"{item['assetbundleName']}/scenario_rip/{ep['scenarioId']}.asset"
                    else:
                        url = f"https://assets.pjsek.ai/file/pjsekai-assets/ondemand/event_story/" + \
                              f"{item['assetbundleName']}/scenario/{ep['scenarioId']}.json"
                    ev_ep[f"{ep['episodeNo']}: {ep['title']}"] = url
                tree['活动剧情'][ev_name] = ev_ep

        if os.path.exists(os.path.join(root, "unitStories.json")):
            data = read_json(os.path.join(root, "unitStories.json"))
            tree['主线剧情'] = {}
            for unit in data:
                for chapters in unit['chapters']:
                    eps = {}
                    for episodes in chapters["episodes"]:
                        key = f"{episodes['episodeNoLabel']}: {episodes['title']}"
                        if source == "pjsekai":
                            url = "https://assets.pjsek.ai/file/pjsekai-assets/startapp/scenario/unitstory/" + \
                                  f"{chapters['assetbundleName']}/{episodes['scenarioId']}.json"
                        else:
                            url = "https://storage.sekai.best/sekai-assets/scenario/unitstory/" \
                                  f"{chapters['assetbundleName']}_rip/{episodes['scenarioId']}.asset"
                        eps[key] = url
                    tree['主线剧情'][chapters['title']] = eps

        if os.path.exists(os.path.join(root, "actionSets.json")):
            data = read_json(os.path.join(root, "actionSets.json"))
            tree['区域对话'] = {}
            for ep in data:
                if "scenarioId" not in ep.keys():
                    continue
                area = areaDict[ep['areaId']]
                group = int(ep["id"] / 100)
                scenario_id = ep['scenarioId']
                chara_string = []
                for cid in ep['characterIds']:
                    for gc in character2ds:
                        if cid == gc['id']:
                            chara_string.append(characterDict[gc['characterId'] - 1]["name_j"])
                            break
                chara = ",".join(chara_string)
                if area in tree['区域对话']:
                    d = tree['区域对话'][area]
                else:
                    d = {}
                as_id = f"{ep['id']} - {chara}"
                if source == "pjsekai":
                    url = f"https://assets.pjsek.ai/file/pjsekai-assets/startapp/scenario/actionset/" \
                          f"group{group}/{scenario_id}.json"
                else:
                    url = f"https://storage.sekai.best/sekai-assets/scenario/actionset/" \
                          f"group{group}_rip/{scenario_id}.asset"
                d[as_id] = url
                tree['区域对话'][area] = d

        if os.path.exists(os.path.join(root, "specialStories.json")):
            data = read_json(os.path.join(root, "specialStories.json"))
            tree['特殊剧情'] = {}
            for period in data:
                title = period["title"]
                title_d = {}
                for ep in period['episodes']:
                    ep_title = ep['title']
                    if source == "best":
                        url = f"https://storage.sekai.best/sekai-assets/scenario/special/" \
                              f"{ep['assetbundleName']}_rip/{ep['scenarioId']}.asset"
                    else:
                        url = f"https://assets.pjsek.ai/file/pjsekai-assets/startapp/scenario/special/" \
                              f"{ep['assetbundleName']}/{ep['scenarioId']}.json"
                    title_d[ep_title] = url
                tree['特殊剧情'][title] = title_d

        if len(tree.keys()) == 5:
            self.SavePlaceLabel.clear()
        self.change_source()
        save_json(os.path.join(root, "tree.json"), tree)

    def download_data(self):
        self.DownloadButton.setEnabled(False)
        self.SavePlaceLabel.setText("下载中")

        self.change_episode()
        url = self.download_url
        if not url:
            self.msgbox.setText("未选择剧情 请先刷新列表")
            self.msgbox.exec_()
            self.msgbox.close()
            return

        self.SavePlaceLabel.setText("下载中")
        self.DownloadButton.setEnabled(False)

        def do_request(req_url):
            if p := self.nam_proxy:
                self.downloader.setProxy(p)
            else:
                self.downloader.setProxy()
            self.downloader.get(QtNetwork.QNetworkRequest(QtCore.QUrl(req_url)))

        do_request(url)

    def load_tree_data(self):
        source = self.DataSourceBox.currentIndex()

        if source == 1:  # pjsekai
            p = os.path.join(self.root, "data/pjsekai/tree/tree.json")
        else:
            p = os.path.join(self.root, "data/best/tree/tree.json")
        data = read_json(p)
        return data

    def change_source(self) -> None:
        data = self.load_tree_data()
        self.DataTypeBox.clear()
        self.DataPeriodBox.clear()
        self.DataEpisodeBox.clear()
        if data:
            self.DataTypeBox.clear()
            for key in data:
                self.DataTypeBox.addItem(key)
            self.DataTypeBox.repaint()

    def change_type(self):
        data = self.load_tree_data()
        if data:
            type_key = self.DataTypeBox.currentText()
            if type_key:
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
            if type_key and period_key:
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
