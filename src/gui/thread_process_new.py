import os

from PySide6 import QtCore


class VideoProcessThread(QtCore.QThread):
    signal_data = QtCore.Signal(dict)

    def __init__(self, parent, video_file, json_file, translate_file=None):
        super().__init__()
        self.started = 0
        self.video_file = video_file
        self.json_file = json_file
        self.translate_file = translate_file
        self.bar = parent

    def run(self):
        from lib.process import SekaiJsonVideoProcess
        self.started = 1
        self.signal_data.emit({"type": int, "data": 1})
        output = os.path.realpath(os.path.splitext(self.video_file)[0] + ".ass")
        vp = SekaiJsonVideoProcess(self.video_file, self.json_file, self.translate_file, output, self.signal_data, True)
        vp.run()
