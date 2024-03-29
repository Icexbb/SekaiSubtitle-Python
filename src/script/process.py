# -*- coding: utf-8 -*-
import copy
import json
import os
import re
import time
from concurrent import futures
from datetime import timedelta
from queue import Queue

import cv2
import numpy as np
import yaml
from PySide6 import QtCore, QtWidgets

import script.tools
from script import match, reference, tools
from script.data import DISPLAY_NAME_STYLE, subtitle_styles_format, staff_style_format, get_divider_event
from script.subtitle import Subtitle


class SekaiJsonVideoProcess:
    def __init__(
            self,
            data: dict,
            signal: QtCore.Signal(dict) = None,
            queue_in: Queue = Queue(),
    ):
        self.time_start = time.time()
        self.json_data = None
        self.data = data
        self.video_file = data.get("video")
        self.json_file = data.get("json")
        self.translate_file = data.get("translate")

        self.overwrite = data.get("overwrite")
        self.font = data.get("font")
        self.dryrun = data.get("dryrun")
        self.staff = data.get("staff") or []
        self.typer_interval = data.get("typer_interval")
        self.duration = data.get("duration")
        self.debug = data.get("debug")
        self.widget_id = data.get("widget_id")
        self.output_path = os.path.realpath(os.path.splitext(self.video_file)[0] + ".ass")
        self.signal = signal
        self.log("initial", f"文件输出到 {self.output_path}")
        if self.duration:
            self.log("initial", f"设置视频处理区间：{self.duration[0]}帧 -> {self.duration[-1]}帧")

        if not os.path.exists(self.video_file):
            raise FileNotFoundError

        # self.json_file: str | list = json_file
        if not self.dryrun:
            if not self.json_file:
                predict_path = os.path.splitext(self.video_file)[0] + ".json"
                if os.path.exists(predict_path):
                    self.json_file = predict_path
                    self.log("initial", f"自动选择了JSON文件 {predict_path}")
                else:
                    self.log("initial", f"JSON文件 {predict_path} 不存在")
                    raise FileNotFoundError("Json File Not Found")
            elif isinstance(self.json_file, str):
                if not os.path.exists(self.json_file):
                    self.log("initial", f"JSON文件 {self.json_file} 不存在")
                    raise FileNotFoundError("Json File Not Found")
            elif isinstance(self.json_file, list):
                if len(self.json_file) == 1:
                    self.json_file: str = self.json_file[0]

        # self.translate_file: str = translate_file
        if self.json_file and not isinstance(self.json_file, list):
            if not self.translate_file:
                predict_path = os.path.splitext(self.video_file)[0] + ".txt"
                if os.path.exists(predict_path):
                    self.translate_file = predict_path
                    self.log("initial", f"自动选择了翻译文件 {predict_path}")
            elif not os.path.exists(self.translate_file):
                self.log("initial", f"翻译文件 {self.translate_file} 不存在")
                raise FileNotFoundError("Translate File Not Found", self.translate_file)

        # self.overwrite = overwrite
        # self.output_path = output_file

        if not self.output_path:
            predict_path = os.path.splitext(self.video_file)[0] + ".ass"
            if (not os.path.exists(predict_path)) or self.overwrite:
                self.output_path = predict_path
                self.log("initial", f"自动选择了输出位置 {predict_path}")
            else:
                raise FileExistsError
        elif os.path.exists(self.output_path):
            if not self.overwrite:
                raise FileExistsError

        if not self.dryrun:
            self.load_json()
        else:
            self.log("initial", f"不使用数据文件")
        self.VideoCapture = cv2.VideoCapture(self.video_file)
        self.log("initial", f"初始化完成")
        self.stop = False
        self.queue = queue_in

    def set_stop(self):
        self.stop = True

    def log(self, msg_type, msg: str | Exception):
        msg_type = msg_type.lower()
        from gui.gui_main import MainUi
        ui = QtWidgets.QApplication.activeWindow()
        if isinstance(ui, MainUi):
            self.debug = ui.debug
            if msg_type in ["error"]:
                ui.signal_exception.emit(msg, self.data)

        if not self.debug and msg_type in ["debug", "调试"]:
            return
        m = f"[{msg_type.capitalize()}] {msg.strip() if isinstance(msg, str) else msg.__repr__()}"
        if self.signal:
            self.signal.emit({"type": str, "data": m})
        else:
            print(m)

    def emit(self, data):
        if self.signal:
            self.signal.emit({'type': data.__class__, 'data': data})

    def load_json(self):
        if not isinstance(self.json_file, list):
            if os.path.exists(self.json_file):
                self.json_data = json.load(open(self.json_file, 'r', encoding='utf-8'))
                if self.translate_file:
                    self.log("initial", f"尝试进行翻译替换")
                    if isinstance(self.translate_file, list) and self.translate_file:
                        self.translate_file = self.translate_file[0]
                    if os.path.exists(self.translate_file):
                        if os.path.splitext(self.translate_file)[-1].lower() == ".txt":
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
                            changed = 0
                            if len(body) == len(self.json_data['TalkData']):
                                result = []
                                for i in range(len(body)):
                                    item = self.json_data['TalkData'][i]
                                    replaced = body[i]
                                    item["Body"] = replaced.replace("\\N", "\n")
                                    result.append(item)
                                self.json_data['TalkData'] = result
                                changed += 1
                            else:
                                self.log("initial", f"翻译文件与对话数据不符")

                            if len(place) == len(
                                    [item for item in self.json_data['SpecialEffectData'] if
                                     dict(item)['EffectType'] == 8]):
                                raw = self.json_data['SpecialEffectData']
                                result = []
                                for item in raw:
                                    if item['EffectType'] == 8:
                                        item["StringVal"] = place.pop(0)
                                    result.append(item)
                                self.json_data['SpecialEffectData'] = result
                                changed += 1
                            else:
                                self.log("initial", f"翻译文件与地点数据不符")
                            if changed == 2:
                                self.log("initial", f"已进行中文替换")
                        if os.path.splitext(self.translate_file)[-1].lower() == ".yml":
                            with open(self.translate_file, "r", encoding="utf8") as fp:
                                data = yaml.load(fp, yaml.Loader)

                            not_changed = 0

                            data_d: list[str] = data["dialog"]
                            if len(data_d) == len([self.json_data['TalkData']]):
                                for index, string in enumerate(data_d):
                                    self.json_data['TalkData'][index]["Body"] = string
                            else:
                                self.log("initial", f"翻译文件与对话数据不符")
                                not_changed += 1

                            effect_type = {"tag": 18, "banner": 8}
                            for effect_name, effect_id in effect_type.items():
                                data_d: list[str] = data[effect_name][:]
                                if len(data_d) == len([1 for item in self.json_data['SpecialEffectData'] if
                                                       dict(item)['EffectType'] == effect_id]):
                                    raw = self.json_data['SpecialEffectData']
                                    result = []
                                    for item in raw:
                                        if item['EffectType'] == effect_id:
                                            if p := data_d.pop(0):
                                                item["StringVal"] = p
                                        result.append(item)
                                    self.json_data['SpecialEffectData'] = result
                                else:
                                    self.log("initial", f"翻译文件与{'角标' if effect_id == 18 else '横幅'}数据不符")
                                    not_changed += 1

                            if not_changed != 3:
                                self.log("initial", f"已进行中文替换")
                    else:
                        self.log("initial", f"翻译文件不存在")
            else:
                self.log("initial", f"JSON文件不存在")
                raise FileNotFoundError("JSON文件不存在")
        else:
            if len(self.json_file) > 1:
                self.log("initial", f"使用了多个Json文件")
            res = {}
            for file in self.json_file:
                data = json.load(open(file, 'r', encoding='utf-8'))
                res = tools.merge_dict(res, data)
            self.json_data = res
        self.log("initial", f"JSON数据读取完成")

    @staticmethod
    def match_frame_dialog(frame: np.ndarray[np.uint8], pointer, last_center):
        center = match.check_frame_pointer_position(frame, pointer, last_center)
        status = match.check_frame_dialog_status(frame, pointer, center)
        return "dialog", (status, center)

    @staticmethod
    def match_frame_banner(frame, banner_mask_area, banner_edge_pattern):
        banner_frame_result: bool = match.check_frame_banner_edge(frame, banner_mask_area, banner_edge_pattern)
        return "banner", (banner_frame_result,)

    @staticmethod
    def match_frame_tag(frame, tag_pattern):
        tag_frame_result = match.check_area_tag_position(frame, tag_pattern)
        return "tag", (tag_frame_result,)

    @staticmethod
    def match_check_start(frame: np.ndarray[np.uint8]):
        start = match.check_frame_content_start(
            frame, match.get_resized_interface_menu(frame.shape[1], frame.shape[0]))
        return start

    def match(self):
        vc = cv2.VideoCapture(self.video_file)
        video_fps = vc.get(5)
        height, width = (vc.get(4), vc.get(3))
        self.log("debug", f"Video {width}x{height}@{video_fps}fps")
        dialog_last_center = None
        last_status = 0
        dialog_pointer = match.get_resized_dialog_pointer(height, width)
        dialog_data: list[dict] = []
        dialog_total_count = len(dialog_data)
        banner_data: list[dict] = []
        banner_data_count = len(banner_data)
        tag_data: list[dict] = []
        tag_data_count = len(tag_data)

        if not self.dryrun:
            dialog_data: list[dict] = copy.deepcopy(self.json_data['TalkData'])
            dialog_total_count = len(dialog_data)
            banner_data: list[dict] = [item for item in self.json_data['SpecialEffectData'] if item['EffectType'] == 8]
            banner_data_count = len(banner_data)
            tag_data: list[dict] = [item for item in self.json_data['SpecialEffectData'] if item['EffectType'] == 18]
            tag_data_count = len(tag_data)

        content_started = False

        banner_events = []
        banner_mask = reference.get_area_banner_mask(reference.get_area_mask_size((width, height)))
        banner_mask_area = match.get_banner_area(height, width)
        banner_edge_pattern = match.get_resized_area_edge(height, width)

        banner_data_processing = None
        banner_processing_frames = []
        banner_processed = 0
        banner_last_result = False
        banner_process_running = True

        tag_events = []
        tag_pattern = match.get_resized_area_tag(height, width)
        tag_processing_frames = []
        tag_data_processing = None
        tag_processed_count = 0
        tag_last_result = None
        tag_process_running = True
        dialog_data_processing = None
        dialog_processing_frames = []
        dialogs_events = []

        now_frame_count = 0
        dialog_last_end_frame = None
        dialog_last_end_event = None
        dialog_const_point_center = None
        dialog_processed = 0
        dialog_process_running = True
        dialog_is_mask_start = False
        if not self.duration:
            total_frame_count = self.VideoCapture.get(7)
        else:
            total_frame_count = self.duration[-1] - self.duration[0]
            vc.set(cv2.CAP_PROP_POS_FRAMES, self.duration[0])
        self.emit({"total": total_frame_count})
        self.log("debug", f"Video Frame {total_frame_count}")

        se_count = 0
        banner_index = []
        tag_index = []
        dialog_index = []
        td_count = 0
        total_count = 0
        if not self.dryrun:
            for item in self.json_data.get("Snippets"):
                if item["Action"] == 1:
                    total_count += 1
                    td_count += 1
                    dialog_index.append(total_count - 1)
                elif item["Action"] == 6:
                    data = self.json_data["SpecialEffectData"][se_count]
                    if data['EffectType'] == 8:
                        total_count += 1
                        banner_index.append(total_count - 1)
                    elif data['EffectType'] == 18:
                        total_count += 1
                        tag_index.append(total_count - 1)
                    se_count += 1
        if not self.dryrun:
            tag_process_running = bool(tag_data)
            banner_process_running = bool(banner_data)
            dialog_process_running = bool(dialog_data)

        while not self.stop:
            if not self.queue.empty():
                self.set_stop()
                break
            ret, frame = vc.read()
            if not ret:
                break
            g_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # c_frame = cv2.Canny(g_frame, 50, 200)
            if not content_started:
                content_started = self.match_check_start(g_frame)
                if content_started:
                    st = script.tools.timedelta_to_string_short(
                        timedelta(
                            seconds=(1 / video_fps) * (now_frame_count + (self.duration[0] if self.duration else 0))))
                    self.log('process', f'Content Started At Frame{now_frame_count} {st}')
            if content_started:
                running_process_count = sum([dialog_process_running, banner_process_running, tag_process_running])
                if running_process_count:
                    with futures.ThreadPoolExecutor(running_process_count) as executor:
                        future_tasks = []
                        if not self.dryrun:
                            unprocessed_event = dialog_index[dialog_processed:] + banner_index[banner_processed:] + \
                                                tag_index[tag_processed_count:]
                            se_index_now = min(unprocessed_event)
                        if dialog_process_running:
                            future = executor.submit(self.match_frame_dialog, g_frame, dialog_pointer,
                                                     dialog_last_center)
                            future_tasks.append(future)
                        if banner_process_running:
                            if self.duration or self.dryrun or \
                                    (not (self.dryrun and self.duration)
                                     and banner_index[banner_processed] == se_index_now):
                                future = executor.submit(
                                    self.match_frame_banner, g_frame, banner_mask_area, banner_edge_pattern)
                                future_tasks.append(future)
                        if tag_process_running:
                            if self.duration or self.dryrun or \
                                    (not (self.dryrun and self.duration)
                                     and tag_index[tag_processed_count] == se_index_now):
                                future = executor.submit(self.match_frame_tag, frame, tag_pattern)
                                future_tasks.append(future)

                        task_iter = futures.as_completed(future_tasks)
                        for future in task_iter:
                            function_type, function_result = future.result()
                            if function_type == "dialog":
                                dialog_status, dialog_point_center = function_result
                                if dialog_status in [1, 2]:
                                    dialog_processing_frames.append(
                                        {"frame": now_frame_count, "point_center": dialog_point_center})
                                if dialog_status == 1:
                                    if not self.dryrun:
                                        index = self.json_data.get('TalkData').index(dialog_data_processing)
                                        if index:
                                            dialog_is_mask_start = self.json_data.get('TalkData')[index - 1][
                                                'WhenFinishCloseWindow']
                                        else:
                                            dialog_is_mask_start = True
                                    else:
                                        if last_status == 0:
                                            dialog_is_mask_start = True
                                        elif last_status == 2:
                                            dialog_is_mask_start = False

                                if dialog_status == 2 and not dialog_const_point_center:
                                    dialog_const_point_center = dialog_point_center

                                if dialog_status in [0, 1] and last_status == 2:  # End Dialog
                                    dialog_processed += 1
                                    if not self.dryrun and dialog_data_processing:
                                        events = self.dialog_make_sequence(
                                            dialog_processing_frames, dialog_data_processing,
                                            int(dialog_pointer.shape[0]), height, width, video_fps,
                                            dialog_last_end_frame, dialog_last_end_event, dialog_is_mask_start)
                                        self.log(
                                            "process", f"Dialog {dialog_processed}: Output {len(events)} Events, "
                                                       f"Remains {dialog_total_count - dialog_processed}/{dialog_total_count}")
                                    else:
                                        events = self.dialog_make_sequence(
                                            dialog_processing_frames, None, int(dialog_pointer.shape[0]),
                                            height, width, video_fps,
                                            dialog_last_end_frame, dialog_last_end_event, dialog_is_mask_start)
                                        if self.dryrun:
                                            self.log(
                                                "process", f"Dialog {dialog_processed}: Output {len(events)} Events")
                                            self.log("警告", f"No Data For This Dialog, Please Recheck")
                                        else:
                                            self.log(
                                                "process", f"Dialog {dialog_processed}: Output {len(events)} Events")
                                            if len(events) > 2:
                                                self.log(
                                                    "警告", f"Jitter Happened in a No-Json Task, Please Recheck")

                                    dialog_last_end_frame = dialog_processing_frames[-1]
                                    dialog_last_end_event = events[-1]
                                    dialogs_events += events
                                    dialog_processing_frames = []
                                    dialog_data_processing = None
                                    dialog_is_mask_start = None

                                    if dialog_processed == dialog_total_count and not self.dryrun:
                                        dialog_process_running = False

                                if not self.dryrun and not dialog_data_processing:
                                    try:
                                        dialog_data_processing = dialog_data.pop(0)
                                    except IndexError:
                                        dialog_data_processing = None

                                last_status = dialog_status
                                dialog_last_center = dialog_point_center
                            elif function_type == "banner":
                                banner_frame_result = function_result[0]
                                if banner_frame_result:
                                    content_started = True
                                    banner_processing_frames.append(now_frame_count)

                                if banner_last_result and not banner_frame_result:
                                    banner_processed += 1

                                    if self.dryrun:
                                        events = self.area_banner_make_sequence(banner_processing_frames, None,
                                                                                banner_mask,
                                                                                video_fps)
                                        self.log(
                                            "process", f"Area Banner {banner_processed}: Output {len(events)} Events")
                                    else:
                                        events = self.area_banner_make_sequence(banner_processing_frames,
                                                                                banner_data_processing,
                                                                                banner_mask,
                                                                                video_fps)
                                        self.log(
                                            "process", f"Area Banner {banner_processed}: "
                                                       f"Output {len(events)} Events, "
                                                       f"Remain {banner_data_count - banner_processed}/{banner_data_count}")

                                    banner_events += events
                                    banner_processing_frames = []
                                    banner_data_processing = None

                                    if not self.dryrun and banner_processed == banner_data_count:
                                        banner_process_running = False

                                if not self.dryrun and not banner_data_processing:
                                    try:
                                        banner_data_processing = banner_data.pop(0)
                                    except IndexError:
                                        banner_data_processing = None
                                banner_last_result = banner_frame_result
                            elif function_type == "tag":
                                tag_frame_result = function_result[0]
                                if tag_frame_result:
                                    tag_processing_frames.append(
                                        {"frame_id": now_frame_count, "position": tag_frame_result, "height": height,
                                         "width": width}
                                    )
                                if tag_last_result and not tag_frame_result:
                                    tag_processed_count += 1

                                    if self.dryrun:
                                        events = self.area_tag_make_sequence(None, height, width, video_fps,
                                                                             tag_processing_frames)
                                        self.log(
                                            "process", f"Area Tag {tag_processed_count}: "
                                                       f"Output {len(events)} Events")
                                    else:
                                        events = self.area_tag_make_sequence(tag_data_processing, height, width,
                                                                             video_fps,
                                                                             tag_processing_frames)
                                        self.log(
                                            "process", f"Area Tag {tag_processed_count}: "
                                                       f"Output {len(events)} Events, "
                                                       f"Remain {tag_data_count - tag_processed_count}/{tag_data_count}")
                                    tag_events += events
                                    tag_processing_frames = []
                                    tag_data_processing = None

                                    if not self.dryrun and tag_processed_count == tag_data_count:
                                        tag_process_running = False

                                if not self.dryrun and not tag_data_processing:
                                    try:
                                        tag_data_processing = tag_data.pop(0)
                                    except IndexError:
                                        tag_data_processing = None
                                tag_last_result = tag_frame_result
            self.emit({"done": 1, "time": time.time() - self.time_start})
            if not now_frame_count % 5:
                self.emit(frame)
            now_frame_count += 1

            if now_frame_count > total_frame_count:
                break

        if not self.stop:
            if not dialogs_events + banner_events + tag_events:
                raise ValueError('No Event Matched')
            dialog_styles = self.dialog_make_styles(dialog_const_point_center, int(dialog_pointer.shape[0]))
            self.log("process", f"Matching Process Finished")
            if (not self.dryrun) and dialog_data + banner_data + tag_data:
                recheck = []
                if dialog_data:
                    recheck.append("Dialog")
                if banner_data:
                    recheck.append("Banner")
                if tag_data:
                    recheck.append("Tag")
                self.log("process", f"Process Not Fully Matched in " + ",".join(recheck))
            return dialogs_events, dialog_styles, banner_events, tag_events
        else:
            raise KeyboardInterrupt

    def dialog_make_styles(self, point_center, point_size: int):
        res = []
        subtitle_styles = copy.deepcopy(subtitle_styles_format)
        for key in subtitle_styles:
            item = subtitle_styles[key]
            item["Fontsize"] = int(point_size * (83 / 56))
            if not key.startswith(("staff", "screen")):
                if item["MarginL"] == 325:
                    item["MarginL"] = int(point_center[0] - 0.5 * point_size)
                    item["MarginV"] = int(point_center[1] + 1.25 * point_size)
            item["Fontname"] = self.font
            res.append(item)
        return res

    @staticmethod
    def dialog_body_typer(body: str, char_interval: list[int, int] = [80, 50]):
        return_char = ["\n", "\\n", "\\N"]
        for c in return_char:
            body.replace(c, "\n")
        body_list = list(body)
        res = []
        next_start = char_interval[1]
        for index, char in enumerate(body_list):
            if char_interval:
                start = next_start + (300 if char == '\n' else 0)
                end = start + char_interval[1]
                r = rf"{{\alphaFF\t({start},{end},1,\alpha0)}}" + (char if char != "\n" else r"\N")
                res.append(r)
                next_start = start + char_interval[0]
            else:
                res.append(char if char != "\n" else r"\N")

        return "".join(res)

    @staticmethod
    def dialog_body_typer_calculater(body: str, frame_count: int, frame_time: timedelta,
                                     char_interval: list[int, int] = [80, 50]):
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
            char_time += char_interval[0] + (300 if char == "\n" else 0)
            n_char = char if char != "\n" else r"\N"
            add_trans = ""
            if char_time < now_time_ms < char_time + char_interval[1]:
                la = int((now_time_ms - char_time) / char_interval[1] * 255)
                la_string = rf"{{\alpha{la}}}"
                add_trans = la_string
            elif char_time > now_time_ms:
                if not is_trans_now:
                    add_trans = trans_alpha_string
                    is_trans_now = True
            if char_interval:
                res.append(add_trans + n_char)
            else:
                res.append(n_char)
        return "".join(res)

    def dialog_make_sequence(
            self,
            dialog_frames: list[dict], dialog_data: dict | None,
            point_size: int, video_height: int, video_width: int,
            fps: float = 60, last_dialog_frame: dict = None, last_dialog_event: dict = None,
            dialog_is_mask_start=False
    ):
        frame_time = timedelta(seconds=1 / fps)
        start_frame = dialog_frames[0]
        end_frame = dialog_frames[-1]
        results = []
        if dialog_data:
            style = DISPLAY_NAME_STYLE[dialog_data['WindowDisplayName']] \
                if dialog_data['WindowDisplayName'] in DISPLAY_NAME_STYLE else "関連人物"
        else:
            style = "関連人物"

        offset_frame = self.duration[0] if self.duration else 0

        frame_points = np.array([item['point_center'] for item in dialog_frames])
        max_dis = [frame_points[:, i].max() - frame_points[:, i].min() for i in [0, 1]]
        jitter = max(max_dis) > 2
        if not jitter:
            start_time = tools.timedelta_to_string(frame_time * (start_frame['frame'] + offset_frame))
            end_time = tools.timedelta_to_string(frame_time * (
                    end_frame['frame'] + (
                1 if dialog_data and dialog_data.get("WhenFinishCloseWindow") else 0) + offset_frame))
            dialog_body = self.dialog_body_typer(dialog_data["Body"], self.typer_interval) if dialog_data else ""
            if not dialog_is_mask_start and last_dialog_frame:
                start_time = last_dialog_event['End']
            event_data = {
                "Layer": 2,
                "Start": start_time,
                "End": end_time,
                "Style": style,
                "Name": dialog_data['WindowDisplayName'] if dialog_data else "",
                "MarginL": 0, "MarginR": 0, "MarginV": 0,
                "Effect": '',
                "Text": dialog_body
            }
            mask_data = copy.deepcopy(event_data)
            mask_string = reference.get_dialog_mask(reference.get_frame_data(
                (video_width, video_height), dialog_frames[0]['point_center']), None)
            mask_data["Text"] = mask_string
            mask_data["Style"] = 'screen'
            mask_data['Layer'] = 1

            if dialog_is_mask_start:
                prefix = r"{\fad(100,0)}"
                mask_data["Start"] = tools.timedelta_to_string(frame_time * max(0, start_frame['frame'] - 6))
                mask_data["Text"] = prefix + mask_data["Text"]
            # if last_dialog_frame and last_dialog_event:
            #     if start_frame['frame'] - last_dialog_frame['frame'] <= 5:
            #         start_time = last_dialog_event['End']
            results.append(mask_data)
            results.append(event_data)
            return results
        else:
            masks = []
            dialogs = []
            frame_data = reference.get_frame_data((video_width, video_height), dialog_frames[0]['point_center'])
            for index, frame in enumerate(dialog_frames):
                move = r"{\an7\pos(" \
                       f"{int(frame['point_center'][0] - 0.5 * point_size)}," \
                       f"{int(frame['point_center'][1] + 1.25 * point_size)}" \
                       r")}"
                if dialog_data:
                    dialog_body = self.dialog_body_typer_calculater(
                        dialog_data["Body"], index, frame_time, self.typer_interval)
                else:
                    dialog_body = ""
                frame_body = move + dialog_body
                event_data = {
                    "Layer": 2,
                    "Start": tools.timedelta_to_string(frame_time * (frame['frame'] + offset_frame)),
                    "End": tools.timedelta_to_string(frame_time * (frame['frame'] + offset_frame + 1)),
                    "Style": style,
                    "Name": dialog_data['WindowDisplayName'] if dialog_data else "",
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

                mask = reference.get_dialog_mask(frame_data, mask_move)

                mask_data = {
                    "Layer": 1,
                    "Start": tools.timedelta_to_string(frame_time * (frame['frame'] + offset_frame)),
                    "End": tools.timedelta_to_string(frame_time * (frame['frame'] + offset_frame + 1)),
                    "Style": 'screen',
                    "Name": dialog_data['WindowDisplayName'] if dialog_data else "",
                    "MarginL": 0, "MarginR": 0, "MarginV": 0, "Effect": '',
                    "Text": mask
                }

                if masks and masks[-1]['Text'] == mask_data["Text"]:
                    ev = copy.deepcopy(masks[-1])
                    ev["End"] = mask_data["End"]
                    masks[-1] = ev
                else:
                    masks.append(mask_data)

            event_data = {
                "Layer": 2, "Type": "Comment", "Style": style, "Effect": '',
                "Start": tools.timedelta_to_string(frame_time * (dialog_frames[0]["frame"] + offset_frame)),
                "End": tools.timedelta_to_string(frame_time * (dialog_frames[-1]["frame"] + offset_frame + 1)),
                "Name": dialog_data['WindowDisplayName'] if dialog_data else "",
                "MarginL": 0, "MarginR": 0, "MarginV": 0, "Text": dialog_data["Body"]
            }
            dialogs.append(event_data)
            mask_data = copy.deepcopy(event_data)
            mask_data["Text"] = reference.get_dialog_mask(frame_data)
            mask_data['Layer'] = 1
            masks.append(mask_data)
            return masks + dialogs

    def area_banner_make_sequence(self, frame_array: list[int], area_info: dict | None, area_mask, fps):
        events = []
        frame_time = timedelta(seconds=1 / fps)

        offset_frame = self.duration[0] if self.duration else 0
        fading_frame = int(100 / (1000 / fps))
        event_mask = {
            "Layer": 1,
            "Start": tools.timedelta_to_string((max(0, frame_array[0] - fading_frame + offset_frame)) * frame_time),
            "End": tools.timedelta_to_string((frame_array[-1] + fading_frame + offset_frame) * frame_time),
            "Style": "address", "Name": '',
            "MarginL": 0, "MarginR": 0, "MarginV": 0, "Effect": '',
            "Text": r"{\fad(100,100)}" + area_mask
        }
        event_data = copy.deepcopy(event_mask)
        event_data["Text"] = r"{\fad(100,100)}" + (area_info["StringVal"] if area_info else "LOCATION")
        event_data['Layer'] = 2
        events.append(event_mask)
        events.append(event_data)
        return events

    def area_tag_make_sequence(self, tag_info: dict | None, h: int, w: int, fps: int,
                               frames: list[dict[str, tuple[int, int] | int]]):
        events_mask = []
        events_body = []
        frame_time = timedelta(seconds=1 / fps)
        offset_frame = self.duration[0] if self.duration else 0

        body = tag_info["StringVal"] if tag_info else ""
        for frame in frames:
            right_position = np.multiply(frame['position'], (1, 7 / 6)).tolist()
            mask_string, mask_size = reference.get_area_tag_mask(h, w, move=right_position)
            body_pos = rf"{{\an7\fs{int(mask_size[0] * 0.85)}" \
                       rf"\pos({int(right_position[0] - mask_size[1] * 19 / 20)}," \
                       rf"{int(right_position[1] - mask_size[0] * 0.4)})}}"
            body_event_data = {
                "Layer": 2, "Style": "address", "Name": '', "MarginL": 0, "MarginR": 0, "MarginV": 0,
                "Start": tools.timedelta_to_string(frame_time * (frame['frame_id'] + offset_frame)),
                "End": tools.timedelta_to_string(frame_time * (frame['frame_id'] + offset_frame + 1)),
                "Effect": '', "Text": body_pos + body
            }
            if events_body and events_body[-1]["Text"] == body_event_data["Text"]:
                events_body[-1]["End"] = body_event_data["End"]
                events_mask[-1]["End"] = body_event_data["End"]
            else:
                events_body.append(body_event_data)
                mask_event_data = copy.deepcopy(body_event_data)
                mask_event_data["Text"] = mask_string
                mask_event_data['Layer'] = 1
                events_mask.append(mask_event_data)

        body_event_data = {
            "Layer": 2, "Style": "address", "Name": '', "Type": "Comment",
            "Start": tools.timedelta_to_string(frame_time * (frames[0]['frame_id'] + offset_frame)),
            "End": tools.timedelta_to_string(frame_time * (frames[-1]['frame_id'] + offset_frame + 1)),
            "MarginL": 0, "MarginR": 0, "MarginV": 0, "Effect": '', "Text": body
        }
        events_body.append(body_event_data)
        mask_event_data = copy.deepcopy(body_event_data)
        mask_string, _ = reference.get_area_tag_mask(h, w)
        mask_event_data["Text"] = mask_string
        mask_event_data["Layer"] = 1
        events_mask.append(mask_event_data)
        return events_mask + events_body

    def run(self):
        self.time_start = time.time()
        self.log("process", f"Start Processing {os.path.split(self.video_file)[-1]}")
        self.emit(1)

        video_height = self.VideoCapture.get(4)
        video_width = self.VideoCapture.get(3)
        try:
            dialogs_events, dialog_styles, banner_events, tag_events = self.match()
        except KeyboardInterrupt:
            self.log("process", f"Process Terminated Prematurely By User,No File Changed")
        except Exception as e:
            self.log("error", e)
            self.emit(4)
        else:
            self.VideoCapture.release()
            staff_style = []
            for staff in self.staff:
                style = copy.deepcopy(staff_style_format)
                style['Name'] = staff["Style"]
                style_align = int(staff["Style"][-1])
                style['Alignment'] = style_align
                if style_align == 1:
                    style["MarginL"] = int(style["MarginL"] * (5 / 3))
                staff_style.append(style)
            filename = os.path.splitext(os.path.split(self.video_file)[-1])[0]
            events = \
                get_divider_event(f"{filename} - Made by SekaiSubtitle", 10) + \
                get_divider_event("Staff Start") + self.staff + get_divider_event("Staff End") + \
                get_divider_event("Banner Start") + banner_events + get_divider_event("Banner End") + \
                get_divider_event("Tag Start") + tag_events + get_divider_event("Tag End") + \
                get_divider_event("Dialog Start") + dialogs_events + get_divider_event("Dialog End")

            res = {
                "ScriptInfo": {"PlayResX": video_width, "PlayResY": video_height},
                "Garbage": {"video": self.video_file},
                "Styles": dialog_styles + staff_style,
                "Events": Subtitle.Events(events).list,
            }
            subtitle = Subtitle(res)
            if os.path.exists(self.output_path):
                if self.overwrite:
                    os.remove(self.output_path)
                    self.log("output", f"Existing output files with the same name have been purged")
                else:
                    raise FileExistsError

            with open(self.output_path, 'w', encoding='utf8') as fp:
                fp.write(subtitle.string)

            self.log("success", f"File Exported to {os.path.realpath(self.output_path)} Successfully")
            if self.signal:
                self.emit(True)
                self.emit({"done": 1, "end": True, "time": time.time() - self.time_start})
                self.emit(2)
