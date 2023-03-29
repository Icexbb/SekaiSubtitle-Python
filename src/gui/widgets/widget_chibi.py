import os
import random
import threading
import socket
from PySide6 import QtCore
from PySide6.QtWebEngineWidgets import QWebEngineView
from http.server import SimpleHTTPRequestHandler
from http.server import ThreadingHTTPServer
from functools import partial
import contextlib
import sys

from PySide6.QtWidgets import QWidget

from script.data import get_asset_path, chara_en_name


class DualStackServer(ThreadingHTTPServer):
    def server_bind(self):
        # suppress exception when protocol is IPv4
        with contextlib.suppress(Exception):
            self.socket.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_V6ONLY, 0)
        return super().server_bind()


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass


class ChibiServer(threading.Thread):
    def __init__(self, port=9000, bind='127.0.0.1', directory='chibi_page') -> None:
        super().__init__()
        self.port = port
        self.bind = bind
        self.directory = get_asset_path(directory)
        self.asset_dir = os.path.join(self.directory, 'assets')
        self.handler_class = partial(
            QuietHandler, directory=self.directory)
        self.daemon = True

    def run(self):
        with DualStackServer((self.bind, self.port), self.handler_class) as httpd:
            httpd.serve_forever()


class WidgetChibi(QWebEngineView, QWidget):
    def __init__(self, chara_name: str = None):
        super().__init__()
        self.thread_http = ChibiServer()
        self.thread_http.start()
        self.chara_id = chara_en_name.index(chara_name.lower()) + 1 if chara_name else random.randint(1, 26)
        self.model_ls = [
            os.path.splitext(os.path.split(item)[-1])[0].lower()
            for item in os.listdir(self.thread_http.asset_dir)
            if item.endswith(".atlas") and item[:2].isdigit() and int(item[:2]) == self.chara_id
        ]
        model = random.choice(self.model_ls)
        ap = 'm_' if self.chara_id in [11, 12, 13, 16, 23, 26] else "w_"
        self.setFixedSize(QtCore.QSize(120, 120))
        self.load(QtCore.QUrl(f"http://127.0.0.1:9000/?an={model}&ap={ap}"))

    def setAnimation(self, animation):
        self.page().runJavaScript(f"changeAnimation({animation})")
