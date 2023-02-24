# -*- coding: utf-8 -*-
import os

from PySide6 import QtWidgets, QtCore

from gui.design.qt_bar import Ui_Form as Bar


class VideoProcessThread(QtCore.QThread):
    signal_data = QtCore.Signal(dict)

    def __init__(self, video_file, json_file, translate_file=None):
        super().__init__()
        self.started = 0
        self.video_file = video_file
        self.json_file = json_file
        self.translate_file = translate_file
        self.bar = ProgressBar(self.video_file)
        self.signal_data.connect(self.bar.subtitle_output_processing)

    def run(self):
        from lib.process import SekaiJsonVideoProcess
        self.started = 1
        self.signal_data.emit({"type": int, "data": 1})
        output = os.path.realpath(os.path.splitext(self.video_file)[0] + ".ass")
        vp = SekaiJsonVideoProcess(self.video_file, self.json_file, self.translate_file, output, self.signal_data, True)
        vp.run()


class ProgressBar(QtWidgets.QWidget, Bar):
    def __init__(self, video_file):
        super(ProgressBar, self).__init__()
        self.video_name = os.path.split(video_file)[-1]
        self.setupUi(self)
        self.strings = []
        self.processing = False
        self.label_video_name.setText(self.video_name)
        self.label_video_name.repaint()
        self.last_emit_time = 0
        self.bar_progress.setMaximum(0)

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
            elif data == 4:
                self.processing = False
                self.label_process_status.setText("错误")
                # self.bar_progress.setStyle("chunk {background-color: #F44336;}")
        elif msg['type'] == bool:
            self.bar_progress.setMaximum(1)
            self.bar_progress.setValue(1)
        else:
            data = msg['data']
            if s := data.get("total"):
                self.bar_progress.setMaximum(self.bar_progress.maximum() + s)
            if data.get("done"):
                self.bar_progress.setValue(self.bar_progress.value() + 1)
            # total_fps = data['frame'] / data['time']
            # current_speed = 1 / (data['time'] - self.last_emit_time) if (data['time'] - self.last_emit_time) else 0
            # self.last_emit_time = data['time']
            # self.label_process_fps.setText(f"{total_fps:.1f}")
            # b_count = len(str(data['total_frame']))
            # if data['frame']:
            #     res = f"[OpenCV] Processing Frame: {int(data['frame']):>{b_count}} " \
            #           f"FPS: {total_fps:>4.1f} Speed:{current_speed:.0f}it/s " \
            #           f"eta: {(data['total_frame'] - data['frame']) / total_fps:>5.1f}s\r"
            #     if str(self.strings[-1]).startswith("[OpenCV] Processing Frame:"):
            #         self.strings[-1] = res
            #     else:
            #         self.strings.append(res)
        self.bar_progress.repaint()
        self.label_process_fps.repaint()
