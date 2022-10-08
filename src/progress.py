import os
import os.path
import time

from PySide6 import QtWidgets, QtCore

from gui.mainGUI import Ui_Sekai_Subtitle
from gui.progress import Ui_Form as Bar


class VideoProcessThread(QtCore.QThread):
    signal_data = QtCore.Signal(dict)

    def __init__(self, video_file, json_file,):
        super().__init__()
        self.started = 0
        self.video_file = video_file
        self.json_file = json_file
        self.bar = ProgressBar(self.video_file)
        self.signal_data.connect(self.bar.subtitle_output_processing)

    def run(self):
        from lib.subtitle.json_process import Episode
        from lib.subtitle.reference import get_point_center
        from lib.subtitle.video_process import VideoProcessor
        self.started = 1
        self.signal_data.emit({"type": int, "data": 1})
        output = os.path.realpath(os.path.splitext(self.video_file)[0] + ".ass")
        # ===== Analyze Video =====
        v = VideoProcessor(self.video_file, self.signal_data)
        v.initial()
        self.signal_data.emit(
            {"type": str, "data": f"[Video] Total frame: {v.frame_count} Video length:{v.second_count}s"}
        )
        t1 = time.time()
        frames = v.process()
        t2 = time.time()
        self.signal_data.emit(
            {"type": str, "data": f"[Finish] Use Time: {t2 - t1:.2f}s Process Rate:{v.second_count / (t2 - t1):.2f}"})
        screen_data = get_point_center((v.frame_width, v.frame_height), v.constant_point_center)
        # ===== Generate Subtitle =====
        episode = Episode(
            self.video_file, self.json_file, output,
            frames, screen_data, v.constant_point_center, v.pointer_size,
            (v.frame_width, v.frame_height), self.signal_data
        )
        episode.save_ass()
        self.started = 2
        self.signal_data.emit({"type": int, "data": 2})


class ProgressBar(QtWidgets.QWidget, Bar):
    def __init__(self, video_file):
        super(ProgressBar, self).__init__()
        self.task_processing = None
        self.video_name = os.path.split(video_file)[-1]
        self.setupUi(self)
        self.strings = []
        self.processing = False
        self.label_video_name.setText(self.video_name)
        self.label_video_name.repaint()

    def subtitle_output_processing(self, msg):
        if msg['type'] == str:
            self.strings.append(msg['data'] + "\n")
        elif msg['type'] == int:
            data = msg['data']
            if data == 2:
                self.processing = False
                self.label_process_status.setText("已完成")
            elif data == 1:
                self.processing = True
                self.label_process_status.setText("处理中")
            elif data == 3:
                self.processing = False
                self.label_process_status.setText("队列中")
        else:
            data = msg['data']
            self.bar_progress.setMaximum(data["total_frame"])
            self.bar_progress.setValue(data['frame'])
            fps = data['frame'] / data['time']
            self.label_process_fps.setText(f"{fps:.1f}")
            if data['frame'] % 200 == 0 or data['frame'] == data['total_frame']:
                res = f"[OpenCV] Processing FPS:{fps:.1f} eta:{(data['total_frame'] - data['frame']) / fps:.1f}s"
                self.strings.append(res)
        self.bar_progress.repaint()
        self.label_process_fps.repaint()
