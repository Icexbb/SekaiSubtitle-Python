# -*- coding: utf-8 -*-
import copy
import json
import os
import re
import time
from datetime import timedelta
from queue import Queue

import cv2
import numpy
from PySide6 import QtCore

import lib.tools
from lib.data import DISPLAY_NAME_STYLE, subtitle_styles_format
from lib.reference import get_dialog_mask, get_frame_data, get_area_mask, get_area_mask_size
from lib.subtitle import Subtitle
from lib import match


class SekaiJsonVideoProcess:

    def __init__(
            self,
            video_file: str,
            json_file: str = None,
            translate_file: str = None,
            output_file: str = None,
            signal: QtCore.Signal(dict) = None,
            overwrite: bool = False,
            queue_in: Queue = Queue(),
            font_custom: str = None
    ):
        self.time_start = time.time()
        self.json_data = None
        self.font = font_custom
        self.signal = signal

        self.video_file = video_file
        if not os.path.exists(self.video_file):
            raise FileNotFoundError

        self.json_file = json_file
        if not self.json_file:
            predict_path = os.path.splitext(self.video_file)[0] + ".json"
            if os.path.exists(predict_path):
                self.json_file = predict_path
                self.log(f"[Initial] 自动选择了JSON文件 {predict_path}")
            else:
                self.log(f"[Initial] JSON文件 {predict_path} 不存在")
                raise FileNotFoundError("Json File Not Found")
        elif not os.path.exists(self.json_file):
            self.log(f"[Initial] JSON文件 {self.json_file} 不存在")
            raise FileNotFoundError("Json File Not Found")

        self.translate_file = translate_file
        if not self.translate_file:
            predict_path = os.path.splitext(self.video_file)[0] + ".txt"
            if os.path.exists(predict_path):
                self.translate_file = predict_path
                self.log(f"[Initial] 自动选择了翻译文件 {predict_path}")
        elif not os.path.exists(self.translate_file):
            self.log(f"[Initial] 翻译文件 {self.translate_file} 不存在")
            raise FileNotFoundError("Translate File Not Found")

        self.overwrite = overwrite
        self.output_path = output_file

        if not self.output_path:
            predict_path = os.path.splitext(self.video_file)[0] + ".ass"
            if (not os.path.exists(predict_path)) or self.overwrite:
                self.output_path = predict_path
                self.log(f"[Initial] 自动选择了输出位置 {predict_path}")
            else:
                raise FileExistsError
        elif os.path.exists(self.output_path):
            if not self.overwrite:
                raise FileExistsError

        self.load_json()
        self.VideoCapture = cv2.VideoCapture(self.video_file)
        self.log("[Initial] 初始化完成")
        self.stop = False
        self.queue = queue_in

    def set_stop(self):
        self.stop = True

    def log(self, message: str):
        if self.signal:
            self.signal.emit({"type": str, "data": message})
        else:
            print(message)

    def emit(self, data):
        if self.signal:
            self.signal.emit({'type': data.__class__, 'data': data})

    def load_json(self):
        if os.path.exists(self.json_file):
            self.json_data = json.load(open(self.json_file, 'r', encoding='utf-8'))
            if self.translate_file and os.path.exists(self.translate_file):
                pattern_body = re.compile(r"^(?P<name>\S*)：(?P<body>.+)$")
                pattern_place = re.compile(r"^(?P<place>\S[^：]*)$")
                with open(self.translate_file, 'r', encoding='utf-8') as fp:
                    translate_data = fp.readlines()
                body = [
                    re.match(pattern_body, string).group("body") for string in translate_data if
                    re.match(pattern_body, string.strip())
                ]
                place = [
                    re.match(pattern_place, string).group("place") for string in translate_data if
                    re.match(pattern_place, string.strip())
                ]
                if len(body) == len(self.json_data['TalkData']):
                    result = []
                    for i in range(len(body)):
                        item = self.json_data['TalkData'][i]
                        replaced = body[i]
                        item["Body"] = replaced.replace("\\N", "\n")
                        result.append(item)
                    self.json_data['TalkData'] = result
                if len(place) == len([item for item in self.json_data['SpecialEffectData'] if item['EffectType'] == 8]):
                    raw = self.json_data['SpecialEffectData']
                    result = []
                    for item in raw:
                        if item['EffectType'] == 8:
                            item["StringVal"] = place.pop(0)
                        result.append(item)
                    self.json_data['SpecialEffectData'] = result
                self.log("[Initial] 已进行中文替换")
        else:
            self.log("[Error] JSON文件不存在")
            assert False, "[Error] JSON文件不存在"
        self.log("[Initial] JSON数据读取完成")

    def dialog_match(self, queue: Queue, results: list):
        vc = self.VideoCapture
        total_frame_count = int(vc.get(7))
        video_fps = vc.get(5)
        height, width = (vc.get(4), vc.get(3))

        last_center = None
        last_status = 0
        pointer = match.get_resized_dialog_pointer(height, width)

        dialog_data: list[dict] = copy.deepcopy(self.json_data['TalkData'])

        dialog_processing = None
        dialog_processing_frames = []

        dialog_events = []
        dialog_count_total = len(dialog_data)

        now_frame_count = 0
        last_end_frame = None
        last_end_event = None
        constant_pc = None
        dialog_processed = 0

        self.emit({"total": dialog_count_total})

        while not self.stop:
            frame = queue.get()

            if isinstance(frame, numpy.ndarray) and dialog_data:

                g_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                pc = match.check_frame_pointer_position(g_frame, pointer, last_center)
                status = match.check_frame_dialog_status(g_frame, pointer, pc)

                if status in [1, 2]:
                    dialog_processing_frames.append({"frame": now_frame_count, "point_center": pc})
                if status == 2 and not constant_pc:
                    constant_pc = pc
                if status in [0, 1] and last_status == 2:  # End Dialog
                    dialog_processed += 1
                    self.emit({"done": 1, "time": time.time() - self.time_start})

                    events = self.dialog_make_sequence(
                        dialog_processing_frames, dialog_processing, int(pointer.shape[0]),
                        height, width, video_fps, last_end_frame, last_end_event)

                    last_end_frame = dialog_processing_frames[-1]
                    last_end_event = events[-1]

                    self.log(f"[Processing] Dialog {dialog_processed}: Output {len(events)} Events, "
                             f"Remain {dialog_count_total - dialog_processed}/{dialog_count_total}")

                    dialog_events += events

                    dialog_processing = None
                    dialog_processing_frames = []

                    if not dialog_data:
                        break
                if last_status in [0, 2] and status == 1:
                    # Start Dialog
                    if not (dialog_processing and dialog_data):
                        try:
                            dialog_processing = dialog_data.pop(0)
                        except IndexError:
                            dialog_processing = None

                last_status = status
                last_center = pc
                now_frame_count += 1

            else:
                if not isinstance(frame, numpy.ndarray):
                    break
            self.emit({"done": 1, "time": time.time() - self.time_start})

        if not self.stop:
            dialog_styles = self.dialog_make_styles(
                point_center=constant_pc,
                point_size=int(pointer.shape[0]),
                # screen_data=get_frame_data((width, height), constant_pc)
            )
            for i in (dialog_events, dialog_styles, height, width):
                results.append(i)

            self.log(
                "[Processing] Dialog Matching Process Finished" + (" But not Fully Matched" if dialog_data else ""))

    def dialog_make_styles(self, point_center, point_size: int):
        res = []
        subtitle_styles = copy.deepcopy(subtitle_styles_format)
        for key in subtitle_styles:
            item = subtitle_styles[key]
            if item["MarginL"] == 325:
                item["MarginL"] = int(point_center[0] - 0.5 * point_size)
                item["MarginV"] = int(point_center[1] + 1.25 * point_size)
                item["Fontsize"] = int(point_size * (83 / 56))
            if self.font:
                item["Font"] = self.font
            res.append(item)
        return res

    @staticmethod
    def dialog_body_typer(body: str, char_interval: int = 50):
        return_char = ["\n", "\\n", "\\N"]
        for c in return_char:
            body.replace(c, "\n")
        body_list = list(body)
        res = []
        return_count = 0
        for index, char in enumerate(body_list):
            return_count += 1 if char == "\n" else 0
            res.append(
                rf"{{\alphaFF\t({char_interval * (index * 2 + 1) + return_count * 300},"
                rf"{char_interval * (index * 2 + 2) + return_count * 300},1,\alpha0)}}"
                + (char if char != "\n" else r"\N"))
        return "".join(res)

    @staticmethod
    def dialog_body_typer_calculater(body: str, frame_count: int, frame_time: timedelta, char_interval: int = 50):
        return_char = ["\n", "\\n", "\\N"]
        for c in return_char:
            body.replace(c, "\n")
        now_time = frame_time * frame_count
        now_time_ms = int(now_time.total_seconds() * 1000)
        trans_alpha_string = r"{\alpha&HFF&}"
        is_trans_now = False
        body_list = list(body)
        res = []
        char_time = 0
        for index, char in enumerate(body_list):
            char_time += 300 + char_interval if char == "\n" else char_interval
            n_char = char
            if char_time < now_time_ms < char_time + char_interval:
                la = 255 - int((now_time_ms - char_time) / char_interval * 255)
                la_string = rf"{{\alpha{int(la)}}}"
                n_char = la_string + (char if char != "\n" else r"\N")
            elif char_time > now_time_ms:
                if not is_trans_now:
                    n_char = trans_alpha_string + (char if char != "\n" else r"\N")
                    is_trans_now = True
            res.append(n_char)
        return "".join(res)

    @staticmethod
    def dialog_make_sequence(
            dialog_frames: list[dict], dialog_data: dict,
            point_size: int, video_height: int, video_width: int,
            fps: float = 60, last_dialog_frame: dict = None, last_dialog_event: dict = None
    ):
        frame_time = timedelta(seconds=1 / fps)
        start_frame = dialog_frames[0]
        end_frame = dialog_frames[-1]
        results = []

        style = DISPLAY_NAME_STYLE[dialog_data['WindowDisplayName']] \
            if dialog_data['WindowDisplayName'] in DISPLAY_NAME_STYLE else "関連人物"

        jitter = False
        for item in dialog_frames:
            if lib.tools.check_distance(item["point_center"], start_frame["point_center"]) > pow(pow(5, 2) * 2, 0.5):
                jitter = True
                break

        if not jitter:
            start_time = lib.tools.timedelta_to_string(frame_time * start_frame['frame'])
            if last_dialog_frame and last_dialog_event:
                if start_frame['frame'] - last_dialog_frame['frame'] <= 1:
                    start_time = last_dialog_event['End']
            dialog_body = SekaiJsonVideoProcess.dialog_body_typer(dialog_data["Body"], 50)
            event_data = {
                "Layer": 1,
                "Start": start_time,
                "End": lib.tools.timedelta_to_string(frame_time * end_frame['frame']),
                "Style": style,
                "Name": dialog_data['WindowDisplayName'],
                "MarginL": 0, "MarginR": 0, "MarginV": 0,
                "Effect": '',
                "Text": dialog_body
            }
            mask_data = copy.deepcopy(event_data)

            mask_data["Text"] = get_dialog_mask(
                get_frame_data((video_width, video_height), dialog_frames[0]['point_center']), None)
            mask_data["Style"] = 'screen'
            results.append(mask_data)
            results.append(event_data)
            return results
        else:
            masks = []
            dialogs = []
            frame_data = get_frame_data((video_width, video_height), dialog_frames[0]['point_center'])
            for index, frame in enumerate(dialog_frames):
                move = r"{\an7\pos(" \
                       f"{int(frame['point_center'][0] - 0.5 * point_size)}," \
                       f"{int(frame['point_center'][1] + 1.25 * point_size)}" \
                       r")}"
                dialog_body = SekaiJsonVideoProcess.dialog_body_typer_calculater(
                    dialog_data["Body"], index, frame_time, 50)
                frame_body = move + dialog_body

                event_data = {
                    "Layer": 1,
                    "Start": lib.tools.timedelta_to_string(frame_time * frame['frame']),
                    "End": lib.tools.timedelta_to_string(frame_time * (frame['frame'] + 1)),
                    "Style": style,
                    "Name": dialog_data['WindowDisplayName'],
                    "MarginL": 0, "MarginR": 0, "MarginV": 0,
                    "Effect": '',
                    "Text": frame_body  # move + trans + dialog_body.replace("\n", r"\N")
                }

                if dialogs and dialogs[-1]['Text'] == event_data["Text"]:
                    ev = copy.deepcopy(dialogs[-1])
                    ev["End"] = event_data["End"]
                    dialogs[-1] = ev
                else:
                    dialogs.append(event_data)

                pc_str = 'point_center'
                mask_move = [(frame[pc_str][i] - start_frame[pc_str][i]) for i in range(len(frame[pc_str]))]

                mask = get_dialog_mask(frame_data, mask_move)

                mask_data = {
                    "Layer": 1,
                    "Start": lib.tools.timedelta_to_string(frame_time * frame['frame']),
                    "End": lib.tools.timedelta_to_string(frame_time * (frame['frame'] + 1)),
                    "Style": 'screen',
                    "Name": dialog_data['WindowDisplayName'],
                    "MarginL": 0, "MarginR": 0, "MarginV": 0, "Effect": '',
                    "Text": mask
                }

                if masks and masks[-1]['Text'] == mask_data["Text"]:
                    ev = copy.deepcopy(masks[-1])
                    ev["End"] = mask_data["End"]
                    masks[-1] = ev
                else:
                    masks.append(mask_data)

            return masks + dialogs

    def area_match(self, queue: Queue, result: list):
        vc = self.VideoCapture
        video_fps = vc.get(5)
        height, width = (vc.get(4), vc.get(3))

        area_mask = get_area_mask(get_area_mask_size((width, height)))
        area_data: list[dict] = [item for item in self.json_data['SpecialEffectData'] if item['EffectType'] == 8]

        area_events = []
        area_mask_area = match.get_square_mask_area(height, width)
        now_frame_count = 0

        area_processing = None
        area_processing_frames = []
        area_processed = 0
        area_count_total = len(area_data)
        content_started = False
        last_result = False
        time_start = time.time()
        self.emit({"total": area_count_total})

        while not self.stop:
            # ret, frame = vc.read()
            frame = queue.get()
            if isinstance(frame, numpy.ndarray) and area_data:

                frame_result: bool = match.check_frame_area_mask(frame, area_mask_area, content_started)
                if frame_result:
                    content_started = True
                    area_processing_frames.append(now_frame_count)

                if frame_result and not last_result:
                    if not (area_processing and area_data):
                        try:
                            area_processing = area_data.pop(0)
                        except IndexError:
                            area_processing = None
                if last_result and not frame_result:
                    area_processed += 1
                    self.emit({"done": 1, "time": time.time() - self.time_start})

                    events = self.area_make_sequence(area_processing_frames, area_processing, area_mask, video_fps)

                    self.log(f"[Processing] AreaInfo {area_processed}: Output {len(events)} Events, "
                             f"Remain {area_count_total - area_processed}/{area_count_total}")
                    area_events += events

                    area_processing = None
                    area_processing_frames = []

                    if not area_data:
                        break

                now_frame_count += 1
                last_result = frame_result
            else:
                if not isinstance(frame, numpy.ndarray):
                    break
            self.emit({"done": 1, "time": time.time() - self.time_start})
        if not self.stop:
            result.append(area_events)
            # return area_events
            self.log(
                "[Processing] AreaInfo Matching Process Finished" + (" But not Fully Matched" if area_data else ""))

    @staticmethod
    def area_make_sequence(frame_array: list[int], area_info: dict, area_mask, fps):
        events = []
        frame_time = timedelta(seconds=1 / fps)
        event_mask = {
            "Layer": 0,
            "Start": lib.tools.timedelta_to_string(frame_array[0] * frame_time),
            "End": lib.tools.timedelta_to_string(frame_array[-1] * frame_time),
            "Style": "address", "Name": '',
            "MarginL": 0, "MarginR": 0, "MarginV": 0, "Effect": '',
            "Text": r"{\fad(100,100)}" + area_mask
        }
        event_data = {
            "Layer": 1,
            "Start": lib.tools.timedelta_to_string(frame_array[0] * frame_time),
            "End": lib.tools.timedelta_to_string(frame_array[-1] * frame_time),
            "Style": "address", "Name": '',
            "MarginL": 0, "MarginR": 0, "MarginV": 0, "Effect": '',
            "Text": area_info["StringVal"]
        }
        events.append(event_mask)
        events.append(event_data)
        return events

    def queue_video_frame(self, queue_array: list[Queue]):
        ret = True
        self.emit({"total": 2 * self.VideoCapture.get(7)})
        while ret:
            ret, frame = self.VideoCapture.read()
            for queue in queue_array:
                queue.put(frame)
            if not self.queue.empty():
                self.set_stop()
                break
        for queue in queue_array:
            queue.put(False)

    def process(self):

        from threading import Thread
        t1r = []
        t2r = []
        dialog_frame_queue = Queue()
        area_frame_queue = Queue()
        queue_array = [dialog_frame_queue, area_frame_queue]

        thread_read_video = Thread(target=self.queue_video_frame, args=(queue_array,))
        dialog_match_thread = Thread(target=self.dialog_match, args=(dialog_frame_queue, t1r,))
        area_match_thread = Thread(target=self.area_match, args=(area_frame_queue, t2r,))

        thread_read_video.start()
        dialog_match_thread.start()
        area_match_thread.start()

        dialog_match_thread.join()
        area_match_thread.join()
        thread_read_video.join()

        if self.stop:
            raise KeyboardInterrupt
        else:
            [dialogs_events, dialog_styles, video_height, video_width] = t1r
            [area_events] = t2r
            return dialogs_events, dialog_styles, video_height, video_width, area_events

    def run(self):
        self.time_start = time.time()
        self.log(f"[Processing] Start Processing {os.path.split(self.video_file)[-1]}")
        self.emit(1)
        try:
            dialogs_events, dialog_styles, video_height, video_width, area_events = self.process()

        except KeyboardInterrupt:
            self.log(f"[Terminated] Process Terminated Prematurely By User")
            self.log(f"[Terminated] No File Changed")

        except Exception as e:
            self.log(f"[Error] {e}")
            self.emit(4)
        else:
            res = {
                "ScriptInfo": {"PlayResX": video_width, "PlayResY": video_height},
                "Garbage": {"video": self.video_file},
                "Styles": dialog_styles,
                "Events": Subtitle.Events(area_events + dialogs_events).list,
            }
            subtitle = Subtitle(res)
            if os.path.exists(self.output_path):
                if self.overwrite:
                    self.log("[Output] File Exists,Removed")
                    os.remove(self.output_path)
                    self.log(f"[Success] Existing output files with the same name have been purged {self.output_path}")
                else:
                    raise FileExistsError

            with open(self.output_path, 'w', encoding='utf8') as fp:
                fp.write(subtitle.string)

            time_end = time.time()

            self.log(f"[Success] Output into {os.path.realpath(self.output_path)}")
            self.log(f"[Success] Make ASS File Succeeded, Used {time_end - self.time_start:.2f}s")
            if self.signal:
                self.emit(2)
                self.emit(True)
