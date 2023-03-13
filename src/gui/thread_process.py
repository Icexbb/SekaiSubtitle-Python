import os
from queue import Queue

from PySide6 import QtCore

from script.process import SekaiJsonVideoProcess


class VideoProcessThread(QtCore.QThread):
    signal_data = QtCore.Signal(dict)
    signal_stop = QtCore.Signal()

    def __init__(self, parent, video_file, json_file, translate_file=None, custom_font: str = None,
                 dryrun: bool = False, staff: list[dict] = None):
        super().__init__()
        self.started = 0
        self.dryrun = dryrun
        self.video_file = video_file
        self.json_file = json_file
        self.translate_file = translate_file
        self.custom_font = custom_font
        self.staff_data = staff

        self.bar = parent
        self.signal_stop.connect(self.stop_process)
        self.vp: SekaiJsonVideoProcess = None
        self.queue = Queue()

    def run(self):
        self.signal_data.emit({"type": int, "data": 1})
        output = os.path.realpath(os.path.splitext(self.video_file)[0] + ".ass")
        self.vp = SekaiJsonVideoProcess(
            self.video_file, self.json_file, self.translate_file,
            output, self.signal_data, True, self.queue, self.custom_font, self.dryrun, self.staff_data
        )
        self.vp.run()

    def stop_process(self):
        self.queue.put(True)
