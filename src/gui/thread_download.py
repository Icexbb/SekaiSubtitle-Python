# -*- coding: utf-8 -*-
import logging

import requests
from PySide6 import QtCore


class DownloadThread(QtCore.QThread):
    trigger = QtCore.Signal(bool)
    data = QtCore.Signal(dict)

    def __init__(self, jsonurl, proxy):
        super(DownloadThread, self).__init__()
        self.url = jsonurl
        self.proxy = proxy

    def run(self):
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                              'AppleWebKit/537.36 (KHTML, like Gecko) '
                              'Chrome/106.0.0.0 Safari/537.36'
            }
            r = requests.get(self.url, headers=headers, stream=True, proxies={"http": self.proxy, "https": self.proxy})
            json_data = r.json()
            if r.status_code != 200:
                logging.info("Download Failed")
                self.trigger.emit(False)
            else:
                self.data.emit({"data": json_data})
                logging.info("Download Succeeded.")
                self.trigger.emit(True)
        except BaseException as e:
            logging.error("Fail to Download Json File.")
            logging.exception(e)
            self.trigger.emit(False)
