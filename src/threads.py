import json
import logging

import httpx
from PySide6 import QtCore


class DownloadThread(QtCore.QThread):
    trigger = QtCore.Signal(bool)

    def __init__(self, jsonpath, jsonurl, proxy, headers):
        super(DownloadThread, self).__init__()
        self.path = jsonpath
        self.url = jsonurl
        self.proxy = proxy
        self.headers = headers

    def run(self):
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                              'AppleWebKit/537.36 (KHTML, like Gecko) '
                              'Chrome/94.0.4606.81 Safari/537.36'
            }
            with httpx.stream("GET", self.url, headers=headers) as r:
                r.encoding = "utf-8"
                json_data = json.loads(r.text)

            with open(self.path, 'w', encoding='utf-8') as f:
                json.dump(json_data, f, indent=2, ensure_ascii=False)
            logging.info("Json File Saved: " + self.path)

            if "code" in json_data and json_data["code"] == "not_found":
                logging.info("Download Failed, Json File not Exist.")
                self.trigger.emit(False)
            else:
                logging.info("Download Succeeded.")
                self.trigger.emit(True)
        except BaseException:
            logging.error("Fail to Download Json File.")
            self.trigger.emit(False)


