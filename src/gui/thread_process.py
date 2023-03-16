from queue import Queue

from PySide6 import QtCore

from script.process import SekaiJsonVideoProcess


class VideoProcessThread(QtCore.QThread):
    signal_data = QtCore.Signal(dict)
    signal_stop = QtCore.Signal()

    def __init__(self, parent, data):
        super().__init__()
        self.started = 0
        self.bar = parent
        self.signal_stop.connect(self.stop_process)
        self.vp: SekaiJsonVideoProcess = None
        self.queue = Queue()
        self.process_data = data

    def run(self):
        self.signal_data.emit({"type": int, "data": 1})
        self.vp = SekaiJsonVideoProcess(self.process_data, self.signal_data, self.queue)
        self.vp.run()

    def stop_process(self):
        self.queue.put(True)
