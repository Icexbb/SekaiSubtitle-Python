import json
import os
import urllib.parse
from urllib import parse

from PySide6 import QtNetwork, QtCore, QtWidgets
from PySide6.QtCore import SIGNAL, Signal

from gui.design.WidgetDataDownload import Ui_DownloadWidget
from script.data import chara_name, areaDict, characterDict, unit_dict
from script.tools import save_json, read_json


class DownloadWidget(Ui_DownloadWidget, QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__()
        self.receive_data = None
        self.downloadState = None
        self.setupUi(self)
        from gui.gui_main import MainUi
        self.parent: MainUi = parent
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
        self.tree_updater.setTransferTimeout(self.parent.download_timeout * 1000)
        self.connect(self.tree_updater, SIGNAL("finished(QNetworkReply*)"), self.received_list_part)
        # self.connect(self.tree_updater, SIGNAL("NetworkError(QNetworkReply*)"), self.error_handle)
        self.downloader = QtNetwork.QNetworkAccessManager()
        self.downloader.setTransferTimeout(self.parent.download_timeout * 1000)
        self.connect(self.downloader, SIGNAL("finished(QNetworkReply*)"), self.received_acquired_data)

        source = self.DataSourceBox.currentIndex()
        self.update_tree("pjsekai" if source else "best")
        if self.nam_proxy:
            self.tree_updater.setProxy(self.nam_proxy)
            self.downloader.setProxy(self.nam_proxy)

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
        parsed_url = urllib.parse.urlparse(url)
        if parsed_url.netloc.__contains__("pjsek.ai"):
            source_type = "pjsekai"
        else:
            source_type = "best"
        file: str = os.path.split(parsed_url.path)[-1]
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
                self.SavePlaceLabel.setText(f"列表信息已保存\n路径：{filepath}")
                self.update_tree(source_type)
            else:
                self.SavePlaceLabel.setText(
                    f"在下载{file}时发生了错误: {er} \n{reply.errorString()} 请尝试修改代理或超时时间")
        except json.decoder.JSONDecodeError:
            pass
        finally:
            self.DownloadButton.setEnabled(True)
            self.RefreshButton.setEnabled(True)

    def received_acquired_data(self, reply: QtNetwork.QNetworkReply):
        url = reply.url().url()
        parsed_url = urllib.parse.urlparse(url)
        if parsed_url.netloc.__contains__("pjsek.ai"):
            source_type = "pjsekai"
        else:
            source_type = "best"
        file: str = os.path.split(parsed_url.path)[-1]
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
                self.SavePlaceLabel.setText(f"文件已保存\n路径: {filepath}")
            else:
                self.SavePlaceLabel.setText(
                    f"在下载{file}时发生了错误: {er} \n{reply.errorString()} 请尝试修改代理或超时时间")
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
            character2ds = {}
        if os.path.exists(os.path.join(root, "events.json")):
            events = read_json(os.path.join(root, "events.json"))
        else:
            events = {}

        if os.path.exists(os.path.join(root, "cards.json")):
            cards = read_json(os.path.join(root, "cards.json"))
        else:
            cards = {}

        if os.path.exists(os.path.join(root, "tree.json")):
            tree = read_json(os.path.join(root, "tree.json"))
        else:
            tree = {}

        if os.path.exists(os.path.join(root, "cardEpisodes.json")) and cards:
            data = read_json(os.path.join(root, "cardEpisodes.json"))
            tree['卡牌剧情'] = {}
            for ep in data:
                if "scenarioId" not in ep:
                    continue
                card_id = ep['cardId']
                card = None
                for enu_card in cards:
                    if enu_card['id'] == card_id:
                        card = enu_card
                        break
                if not card:
                    continue
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
                d[f"{card_id} - {rarity} {prefix} {section}"] = url
                tree['卡牌剧情'][chara] = d

        if os.path.exists(os.path.join(root, "eventStories.json")) and events:
            data = read_json(os.path.join(root, "eventStories.json"))
            tree['活动剧情'] = {}
            for item in data:
                try:
                    ev_name = f"{item['eventId']}:{events[item['eventId'] - 1]['name']}"
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

        if os.path.exists(os.path.join(root, "actionSets.json")) and character2ds and events:
            data: list[dict] = read_json(os.path.join(root, "actionSets.json"))
            tree['地图对话 - 地点筛选'] = {}
            tree['地图对话 - 人物筛选'] = {}
            tree['地图对话 - 活动追加'] = {}
            tree['地图对话 - 月度追加'] = {}
            as_count = 0
            as_count_sp = 0
            for ep in data:
                if (not ep.get("scenarioId")) or (not ep.get("actionSetType")):
                    continue
                area: str = areaDict[ep['areaId']]
                group: int = int(ep["id"] / 100)
                scenario_id: str = ep['scenarioId']
                chara_string: list[str] = []
                for cid in ep['characterIds']:
                    for gc in character2ds:
                        if cid == gc['id']:
                            chara_string.append(characterDict[gc['characterId'] - 1])
                            break
                chara: str = ",".join(chara_string)

                if ep.get("actionSetType") == "normal":
                    as_count += 1
                    as_id = f"{as_count:04d} - {chara} - id{ep['id']}"
                else:
                    as_count_sp += 1
                    as_id = f"S{as_count_sp:03d} - {chara} - id{ep['id']}"

                if source == "pjsekai":
                    url = f"https://assets.pjsek.ai/file/pjsekai-assets/startapp/scenario/actionset/" \
                          f"group{group}/{scenario_id}.json"
                else:
                    url = f"https://storage.sekai.best/sekai-assets/scenario/actionset/" \
                          f"group{group}_rip/{scenario_id}.asset"

                if "monthly" in scenario_id:
                    year = scenario_id.split("_")[1].removeprefix("monthly")[:2]
                    month = scenario_id.split("_")[1].removeprefix("monthly")[2:]
                    key = f"{year}年{month}月"
                    d = tree['地图对话 - 月度追加'].get(key) or {}
                    d[as_id] = url
                    tree['地图对话 - 月度追加'][key] = d

                if "ev" in scenario_id:
                    release_event_id = ep['releaseConditionId']
                    if release_event_id > 100000:
                        release_event_id = int((release_event_id % 10000) / 100) + 1
                    unit = unit_dict[scenario_id.split("_")[2]]
                    key = f"{release_event_id}: {events[release_event_id - 1]['name']} - {unit}" \
                        if release_event_id < len(events) else f"{release_event_id}: 未知活动 - {unit}"
                    d = tree['地图对话 - 活动追加'].get(key) or {}
                    d[as_id] = url
                    tree['地图对话 - 活动追加'][key] = d

                d = tree['地图对话 - 地点筛选'].get(area) or {}
                d[as_id] = url
                tree['地图对话 - 地点筛选'][area] = d

                for chara in chara_string:
                    d = tree['地图对话 - 人物筛选'].get(chara) or {}
                    d[as_id] = url
                    tree['地图对话 - 人物筛选'][chara] = d

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
        save_json(os.path.join(root, "tree.json"), tree)
        self.change_source()

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
            keys = sorted(list(data.keys()))
            for key in keys:
                self.DataTypeBox.addItem(key)
            self.DataTypeBox.repaint()

    def change_type(self):
        data = self.load_tree_data()
        if data:
            type_key = self.DataTypeBox.currentText()
            if type_key:
                self.DataPeriodBox.clear()
                ls = data[type_key]
                if type_key == "活动剧情":
                    ls = reversed(ls)
                if type_key == "地图对话 - 人物筛选":
                    ls = sorted(ls, key=lambda x: characterDict.index(x))
                for key in ls:
                    self.DataPeriodBox.addItem(key)
                self.DataPeriodBox.repaint()
                if type_key == "地图对话 - 地点筛选":
                    self.L2.setText("区域类别")
                    self.L3.setText("对话序号")
                elif type_key == "地图对话 - 月度追加":
                    self.L2.setText("追加时间")
                    self.L3.setText("对话序号")
                elif type_key == "地图对话 - 活动追加":
                    self.L2.setText("追加活动")
                    self.L3.setText("对话序号")
                elif type_key == "地图对话 - 人物筛选":
                    self.L2.setText("角色名称")
                    self.L3.setText("对话序号")
                    self.DataPeriodBox.insertSeparator(4)
                    self.DataPeriodBox.insertSeparator(9)
                    self.DataPeriodBox.insertSeparator(14)
                    self.DataPeriodBox.insertSeparator(19)
                    self.DataPeriodBox.insertSeparator(24)
                elif type_key == "活动剧情":
                    self.L2.setText("活动期数")
                    self.L3.setText("剧情话数")
                elif type_key == "特殊剧情":
                    self.L2.setText("剧情类别")
                    self.L3.setText("剧情话数")
                elif type_key == "主线剧情":
                    self.L2.setText("乐队章节")
                    self.L3.setText("剧情话数")
                elif type_key == "卡牌剧情":
                    self.L2.setText("所属角色")
                    self.L3.setText("角色卡牌")
        else:
            self.DataTypeBox.clear()

    def change_period(self):
        data = self.load_tree_data()
        if data:
            type_key = self.DataTypeBox.currentText()
            period_key = self.DataPeriodBox.currentText()
            if type_key and period_key:
                self.DataEpisodeBox.clear()
                ls = data[type_key][period_key]
                if type_key == "地图对话":
                    ls = sorted(ls)
                for key in ls:
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
