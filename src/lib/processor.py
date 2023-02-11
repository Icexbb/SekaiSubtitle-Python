import json
import os
import re
import time
from datetime import timedelta

import cv2
import numpy as np
from PySide6.QtCore import Signal

from lib.data import subtitle_styles, DISPLAY_NAME_STYLE
from script import match
from script.tools import timedelta_to_string, check_distance
from .reference import get_area_mask, get_dialog_mask
from .subtitle import Subtitle


class Frame:
    def __init__(
            self,
            frame_id: int,
            status: tuple,
            points: list[tuple | None],
            constant_point,
            # timestamp: timedelta,
            mask_status: tuple,
            time_ms: float
    ):
        self.timestamp = timedelta(seconds=frame_id * time_ms)
        self.frame_id = frame_id
        self.point = points[frame_id]
        self.points = points
        self.status = status
        self.constant_point = constant_point
        self.mask_status = mask_status

    def is_area_mask_start(self):
        if self.mask_status == (0, 1, 1):
            return True
        return False

    def is_area_mask_end(self):
        if self.mask_status == (1, 1, 0):
            return True
        return False

    def is_constant(self, point=None):
        point = point if point else self.point
        if point:
            if check_distance(point, self.constant_point) <= pow(50, 0.5):
                return True
        return False

    def is_dialog_start(self):
        if self.status in [(0, 1, 1), (0, 1, 2), (2, 1, 1), (2, 1, 2)]:
            return True
        return False

    def is_dialog_end(self):
        if self.status in [(2, 2, 0), (2, 2, 1)]:  # , (1, 2, 0), (1, 2, 1)]:
            return True
        # if self.status in [(2, 2, 2), (1, 2, 2)] and (not self.is_constant(self.points[self.frame_id + 1])):
        #    return True
        return False

    def is_mask_start(self):
        if self.status in [(0, 1, 1), (0, 1, 2)]:
            return True
        return False

    def is_mask_end(self):
        if self.status in [(2, 2, 0), (1, 2, 0)]:
            return True
        return False


class VideoProcessor:

    def __init__(self, video_path: str, signal: Signal, json_file: str):

        self.result_frames = None
        self.frame_ms = None
        self.pointer_pixel_count = None
        self.video_path: str = video_path
        self.signal = signal
        self.second_count = None
        self.menu_sign = None
        self.area_mask = None
        self.start = False
        self.frame_gray = None
        self.frame = None
        self.initialed = False
        self.video = None
        self.pointer_size = None
        self.frame_height = None
        self.frame_width = None
        self.constant_point_center = None
        self.pointer = None
        self.frame_count = None
        # self.point_pattern_path: str = r"asset/point.png"
        # self.menu_pattern_path: str = r"asset/menu.png"
        data = json.load(open(json_file, 'r', encoding="utf8"))
        self.area_mask_count = len([item for item in data['SpecialEffectData'] if item['EffectType'] == 8])
        self.dialog_count = len(data['TalkData'])

    def initial(self):
        assert os.path.exists(self.video_path), "Video Not Exists"

        self.video: cv2.VideoCapture = cv2.VideoCapture(self.video_path)
        self.frame_height = int(self.video.get(4))
        self.frame_width = int(self.video.get(3))
        self.frame_count: int = int(self.video.get(7))
        self.frame_ms = (1 / self.video.get(5))
        self.second_count: float = int((self.frame_count / self.video.get(5)) * 100) / 100

        self.initial_sign()
        self.initial_area_mask()

        self.pointer_size: int = self.pointer.shape[0]
        self.constant_point_center: tuple[int, int] | None = None
        self.pointer_pixel_count = pow(self.pointer_size, 2)
        self.initialed = True

    def initial_area_mask(self):
        self.area_mask = match.get_square_mask_area(self.frame_height, self.frame_width)

    def initial_sign(self):
        self.pointer = match.get_resized_dialog_pointer(self.frame_height, self.frame_width)
        self.menu_sign = match.get_resized_interface_menu(self.frame_height, self.frame_width)

    '''def check_frame_pointer_position(self, frame: np.ndarray):
        height = self.frame_height
        width = self.frame_width
        if self.constant_point_center:
            lft, tp = self.constant_point_center
            border = self.pointer_size * 0.9
            cut_up = int(tp - border)
            cut_down = int(tp + border)
            cut_left = int(lft - border)
            cut_right = int(lft + border)
        else:
            cut_up = int(height * 0.6)
            cut_down = int(height * 9)
            cut_left = int(width * 0)
            cut_right = int(width * 0.4)
        cut = frame[cut_up:cut_down, cut_left:cut_right]

        res = cv2.matchTemplate(cut, self.pointer, cv2.TM_CCOEFF_NORMED)
        threshold = 0.85

        loc = divmod(np.argmax(res), res.shape[1])
        if res[loc[0], loc[1]] < threshold:
            center = None
        else:
            left_top = (cut_left + loc[1].item(), cut_up + loc[0].item())
            center = (int(left_top[0] + (self.pointer_size / 2)), int(left_top[1] + (self.pointer_size / 2)))
        return center'''

    '''def check_frame_dialog_status(self, frame: np.ndarray, point_center: tuple[int, int] | None):
        if not point_center:
            return 0
        pointer_size = self.pointer_size
        color = 128  # (106, 75, 78)

        left = int(point_center[0] - pointer_size / 2)
        top = int(point_center[1] - pointer_size / 2)
        right = int(point_center[0] + pointer_size / 2)
        bottom = int(point_center[1] + pointer_size / 2)

        top = int(top + 0.9 * pointer_size + pointer_size)
        bottom = int(bottom + 0.9 * pointer_size + pointer_size)

        cut = frame[top:bottom, left:right]
        first_exist = check_dark(cut, color)

        left = int(left + 0.15 * pointer_size + pointer_size)
        right = int(right + 0.15 * pointer_size + pointer_size)

        cut = frame[top:bottom, left:right]
        second_exist = check_dark(cut, color)

        result = int(first_exist + second_exist)
        if result == 2 and not self.constant_point_center:
            self.constant_point_center = point_center
        return result'''

    '''def check_frame_content_start(self, frame: np.ndarray):
        menu_height = self.menu_sign.shape[1]
        menu_width = self.menu_sign.shape[0]
        cut_down = int(2.5 * menu_height)
        cut_left = -1 * int(2.5 * menu_width)
        cut = frame[:cut_down, cut_left:]
        res = cv2.matchTemplate(cut, self.menu_sign, cv2.TM_CCOEFF_NORMED)
        threshold = 0.70

        loc = divmod(np.argmax(res), res.shape[1])
        exist = (not (res[loc[0], loc[1]] < threshold))
        self.start = exist'''

    '''def check_frame_area_mask(self, frame: np.ndarray):
        cut1 = frame[
               self.area_mask[0]:self.area_mask[0] + self.pointer_size,
               self.area_mask[2]:self.area_mask[2] + self.pointer_size
               ]
        num = pow(self.pointer_size, 2)
        self.pointer_pixel_count = pow(self.pointer_size, 2)
        exist = 0
        for array in cut1:
            for pixel in array:
                dis = check_distance(pixel, (178, 145, 139))
                if dis < 25:
                    exist += 1
                if exist > num * 0.8:
                    return True
        return False'''

    def video_process(self):
        status_chain = np.zeros(self.frame_count + 2)  # [0]
        point_chain: list = [None for _ in range(self.frame_count + 1)]
        mask_chain = np.zeros(self.frame_count + 2)

        frame_count = 0
        last_process_frame = 0
        next_process_frame = 0
        frame_step = 5
        time_start = time.time()

        area_mask_count = 0
        dialog_count = 0
        while True:
            center = None
            frame_dialog_status = 0
            frame_area_mask_status = 0
            if frame_count == next_process_frame:
                # if self.video.get(1) != frame_count:
                #    self.video.set(cv2.CAP_PROP_POS_FRAMES, frame_count)
                ret, frame = self.video.read()
                if not ret:
                    break
                gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                if not self.start:
                    self.start = match.check_frame_content_start(gray_frame, self.menu_sign)
                    # self.check_frame_content_start(gray_frame)
                next_process_frame = frame_count + frame_step

                if self.start:
                    if dialog_count != self.dialog_count:
                        center = match.check_frame_pointer_position(gray_frame, self.pointer,
                                                                    self.constant_point_center)
                        # self.check_frame_pointer_position(gray_frame)
                        # frame_dialog_status = self.check_frame_dialog_status(gray_frame, center)
                        frame_dialog_status = match.check_frame_dialog_status(gray_frame, self.pointer, center)
                    if area_mask_count != self.area_mask_count and not frame_dialog_status:
                        frame_area_mask_status = int(match.check_frame_area_mask(frame, self.area_mask, self.pointer))
                        # self.check_frame_area_mask(frame))
                    if frame_step != 1:
                        next_process_frame = last_process_frame + 1
                        frame_count = last_process_frame
                        frame_step = 1
                last_process_frame = frame_count
            else:
                self.video.grab()
            frame_count += 1
            point_chain[frame_count] = center
            status_chain[frame_count + 1] = frame_dialog_status
            mask_chain[frame_count + 1] = frame_area_mask_status
            if mask_chain[frame_count + 1] == 0 and mask_chain[frame_count] == 1:
                area_mask_count += 1
            if status_chain[frame_count + 1] != 2 and status_chain[frame_count] == 2:
                dialog_count += 1
            # signal
            self.signal.emit({
                "type": dict,
                "data": {
                    "time": time.time() - time_start,
                    "frame": frame_count,
                    "total_frame": self.frame_count}
            })
            if frame_count > self.frame_count:
                break
        frame_chain = []
        ps = [point_chain[i] for i in range(len(point_chain)) if status_chain[i + 1] == 2]
        constant_point = max(ps, key=ps.count)
        for i in range(self.frame_count):
            f = Frame(
                i,
                tuple(status_chain[i:i + 3]),
                point_chain,
                constant_point,
                tuple(mask_chain[i - 1:i + 2]),
                self.frame_ms
            )
            frame_chain.append(f)
        return frame_chain


class JsonProcessor:
    def __init__(
            self,
            file_path: str,
            json_file: str,
            fitting_file: str | None,
            output_path: str,
            frames: list[Frame],
            screen_data: dict,
            point_center: tuple,
            point_size: int,
            video_size: tuple,
            signal: Signal
    ):
        self.file_path = file_path
        self.output_path = output_path
        self.fitting_file = fitting_file
        self.regular_dialog_mask = get_dialog_mask(screen_data)
        self.area_mask = get_area_mask(screen_data)
        self.screen_data = screen_data
        self.point_center = point_center
        self.point_size = point_size
        self.video_size = video_size
        self.signal = signal

        data = json.load(open(json_file, 'r', encoding="utf8"))
        self.area_mask_data = [item for item in data['SpecialEffectData'] if item['EffectType'] == 8]
        self.talk_data_data = [item for item in data['TalkData']]
        self.frames = frames

    def generate_ass_area_mask(self):
        area_mask_frame_pair: list[tuple[Frame, Frame]] = []
        area_mask_start_keyframes = [frame for frame in self.frames if frame.is_area_mask_start()]
        area_mask_end_keyframes = [frame for frame in self.frames if frame.is_area_mask_end()]
        assert len(area_mask_end_keyframes) == len(area_mask_start_keyframes), "Area Mask Start and End Not Correspond"
        for i in range(len(area_mask_end_keyframes)):
            if not i == len(area_mask_end_keyframes) - 1:
                assert area_mask_end_keyframes[i].frame_id < area_mask_start_keyframes[
                    i + 1].frame_id, "Area Mask Chaos"
            area_mask_frame_pair.append((area_mask_start_keyframes[i], area_mask_end_keyframes[i]))
        assert len(area_mask_frame_pair) >= len(self.area_mask_data), "Area Mask and Json Data Not Correspond"
        if len(area_mask_frame_pair) > len(self.area_mask_data):
            self.signal.emit({"type": str, "data": "[Error] Area Mask Found More Than Json Data"})
        results = []
        for i in range(len(self.area_mask_data)):
            item = self.area_mask_data[i]
            pair = area_mask_frame_pair[i]
            event_mask = {
                "Layer": 0,
                "Start": timedelta_to_string(pair[0].timestamp),
                "End": timedelta_to_string(pair[1].timestamp),
                "Style": "address", "Name": '',
                "MarginL": 0, "MarginR": 0, "MarginV": 0, "Effect": '',
                "Text": r"{\fad(100,100)}" + self.area_mask
            }
            event_data = {
                "Layer": 1,
                "Start": timedelta_to_string(pair[0].timestamp),
                "End": timedelta_to_string(pair[1].timestamp),
                "Style": "address", "Name": '',
                "MarginL": 0, "MarginR": 0, "MarginV": 0, "Effect": '',
                "Text": item["StringVal"]
            }
            results.append(event_data)
            results.append(event_mask)
        return results

    def generate_ass_dialog_mask(self, jitter_area: list[tuple[Frame, Frame]]):
        dialog_mask_frame_pair: list[tuple[Frame, Frame]] = []
        dialog_mask_start_keyframes = [frame for frame in self.frames if frame.is_mask_start()]
        dialog_mask_end_keyframes = [frame for frame in self.frames if frame.is_mask_end()]
        assert len(dialog_mask_end_keyframes) == len(
            dialog_mask_start_keyframes), "Dialog Mask Start and End Not Correspond"
        for i in range(len(dialog_mask_end_keyframes)):
            if not i == len(dialog_mask_end_keyframes) - 1:
                assert dialog_mask_end_keyframes[i].frame_id < dialog_mask_start_keyframes[
                    i + 1].frame_id, "Dialog Mask Chaos"
            dialog_mask_frame_pair.append((dialog_mask_start_keyframes[i], dialog_mask_end_keyframes[i]))
        results = []
        for i in range(len(dialog_mask_frame_pair)):
            pair = dialog_mask_frame_pair[i]
            save_place = []
            jitter_place = []
            not_current = []
            while jitter_area:
                ji = jitter_area.pop()
                if pair[0].frame_id <= ji[0].frame_id and ji[1].frame_id <= pair[1].frame_id:
                    jitter_place.append(ji)
                else:
                    not_current.append(ji)
            jitter_area = not_current
            ji_count = len(jitter_place)
            cu_count = 0
            last_frame = None
            for ji in jitter_place:
                if cu_count == 0:
                    save_place.append((pair[0], ji[0]))
                else:
                    save_place.append((last_frame, ji[0]))
                last_frame = ji[1]
                cu_count += 1
                if ji_count == cu_count:
                    save_place.append((last_frame, pair[1]))

            if not jitter_place:
                save_place = [pair]

            for pair in jitter_place:
                range_frame = list(range(pair[0].frame_id, pair[1].frame_id))
                count = 1
                last_move = None
                start = range_frame[0]
                for j in range_frame:
                    move = None
                    if self.frames[j].point:
                        move = [self.frames[j].point[0] - pair[0].constant_point[0],
                                self.frames[j].point[1] - pair[0].constant_point[1]]

                    if last_move != move or j == range_frame[-1]:
                        event_mask = {
                            "Layer": 1, "Style": DISPLAY_NAME_STYLE["screen"],
                            "Start": timedelta_to_string(self.frames[start].timestamp),
                            "End": timedelta_to_string(self.frames[start + count].timestamp),
                            "Name": '', "MarginL": 0, "MarginR": 0, "MarginV": 0, "Effect": '',
                            "Text": get_dialog_mask(self.screen_data, move)
                        }
                        start = j
                        last_move = move
                        results.append(event_mask)
                    else:
                        count += 1
            for pair in save_place:
                event_mask = {
                    "Layer": 1, "Style": DISPLAY_NAME_STYLE["screen"],
                    "Start": timedelta_to_string(pair[0].timestamp),
                    "End": timedelta_to_string(self.frames[pair[1].frame_id + 1].timestamp),
                    "Name": '', "MarginL": 0, "MarginR": 0, "MarginV": 0, "Effect": '',
                    "Text": self.regular_dialog_mask
                }
                results.append(event_mask)
            if jitter_place:
                self.signal.emit({"type": str, "data": f"[Warning] Jitter Happened in Dialog Mask {i}"})
        return results

    def generate_ass_dialog(self):
        dialog_frame_pair: list[tuple[Frame, Frame]] = []
        dialog_start_keyframes = [frame for frame in self.frames if frame.is_dialog_start()]
        dialog_end_keyframes = [frame for frame in self.frames if frame.is_dialog_end()]
        assert len(dialog_end_keyframes) == len(dialog_start_keyframes), "Dialog Start and End Not Correspond"
        for i in range(len(dialog_end_keyframes)):
            if not i == len(dialog_end_keyframes) - 1:
                assert dialog_end_keyframes[i].frame_id < dialog_start_keyframes[
                    i + 1].frame_id, "Dialog Chaos"
            dialog_frame_pair.append((dialog_start_keyframes[i], dialog_end_keyframes[i]))
        assert len(dialog_frame_pair) == len(self.talk_data_data), "Dialog and Json Data Not Correspond"
        results = []
        jitter_pair = []
        for i in range(len(dialog_frame_pair)):
            item = self.talk_data_data[i]
            pair = dialog_frame_pair[i]
            jitter = False
            for j in range(pair[0].frame_id, pair[1].frame_id):
                if check_distance(self.frames[j].point, pair[0].point) > pow(pow(5, 2) * 2, 0.5):
                    jitter = True
                    break
            style = DISPLAY_NAME_STYLE[item['WindowDisplayName']] \
                if item['WindowDisplayName'] in DISPLAY_NAME_STYLE else "関連人物"
            if jitter:
                range_frame = list(range(pair[0].frame_id, pair[1].frame_id))
                st = pair[0].timestamp
                last_move = ""
                start = range_frame[0]
                count = 1
                for j in range_frame:
                    move = r"{\pos(" \
                           f"{int(self.frames[j].point[0] - 0.5 * self.point_size)}," \
                           f"{int(self.frames[j].point[1] + 1.25 * self.point_size)}" \
                           r")}"
                    trans = (r"{\clip(0,0,0,0)\t("
                             f"{int((self.frames[start].timestamp - st).total_seconds() * 1000)},"
                             f"{int((self.frames[start].timestamp - st).total_seconds() * 1000) + 1},"
                             rf"\clip(0,0,{self.video_size[0]},{self.video_size[1]}))"
                             "}")
                    if last_move != move or j == range_frame[-1]:
                        event_data = {
                            "Layer": 1,
                            "Start": timedelta_to_string(pair[0].timestamp),
                            "End": timedelta_to_string(self.frames[start + count].timestamp),
                            "Style": style,
                            "Name": item['WindowDisplayName'],
                            "MarginL": 0, "MarginR": 0, "MarginV": 0,
                            "Effect": '',
                            "Text": move.removesuffix("}") + trans.removeprefix("{") + item["Body"].replace("\n", r"\N")
                        }
                        start = j
                        count = 1
                        last_move = move
                        results.append(event_data)
                    else:
                        count += 1
                self.signal.emit({
                    "type": str, "data": f"[Warning] Jitter Happened in Dialog {i}"
                })
                jitter_pair.append(pair)
            else:
                event_data = {
                    "Layer": 1,
                    "Start": timedelta_to_string(pair[0].timestamp),
                    "End": timedelta_to_string(self.frames[pair[1].frame_id + 1].timestamp),
                    "Style": style,
                    "Name": item['WindowDisplayName'],
                    "MarginL": 0, "MarginR": 0, "MarginV": 0,
                    "Effect": '',
                    "Text": item["Body"].replace("\n", r"\N")
                }
                results.append(event_data)
        return results, jitter_pair

    def generate_styles(self):
        res = []
        for key in subtitle_styles:
            item = subtitle_styles[key]
            if item["Fontname"] == "思源黑体 CN Bold":
                item["Fontname"] = "思源黑体 CN"
                item['Bold'] = True
            if item["MarginL"] == 325:
                item["MarginL"] = int(self.point_center[0] - 0.5 * self.point_size)
                item["MarginV"] = int(self.point_center[1] + 1.25 * self.point_size)
                item["Fontsize"] = self.screen_data['pattern_coefficient'] * self.point_size
            res.append(item)
        return res

    def replace_chinese_body(self):
        pattern_body = re.compile(r"^(?P<name>\S*)：(?P<body>.+)$")
        pattern_place = re.compile(r"^(?P<place>\S[^：]*)$")
        if self.fitting_file and os.path.exists(self.fitting_file):
            with open(self.fitting_file, 'r', encoding="utf8") as fp:
                fitting_data = fp.readlines()
            body = [
                re.match(pattern_body, string).group("body") for string in fitting_data if
                re.match(pattern_body, string.strip())
            ]
            place = [
                re.match(pattern_place, string).group("place") for string in fitting_data if
                re.match(pattern_place, string.strip())
            ]
            if len(body) == len(self.talk_data_data):
                result = []
                for i in range(len(body)):
                    item = self.talk_data_data[i]
                    item["Body"] = body[i]
                    result.append(item)
                self.talk_data_data = result
            if len(place) == len(self.area_mask_data):
                result = []
                for i in range(len(place)):
                    item = self.area_mask_data[i]
                    item["StringVal"] = place[i]
                    result.append(item)
                self.area_mask_data = result
            self.signal.emit({"type": str, "data": "[Output] 已进行中文替换"})

    def save_ass(self):
        try:
            self.replace_chinese_body()
            dia, jit = self.generate_ass_dialog()
            d_mask = []  # self.generate_ass_dialog_mask(jit)
            a_mask = self.generate_ass_area_mask()
            res = {
                "ScriptInfo": {"PlayResX": self.video_size[0], "PlayResY": self.video_size[1]},
                "Garbage": {"video": self.file_path},
                "Styles": self.generate_styles(),
                "Events": Subtitle.Events(
                    a_mask + d_mask + dia).list,
            }
            subtitle = Subtitle(res)
        except AssertionError as e:
            self.signal.emit({"type": str, "data": f"[Error] {e.args[0]}"})
            self.signal.emit({"type": int, "data": 4})
            return
        else:
            if os.path.exists(self.output_path):
                self.signal.emit({"type": str, "data": "[Output] File Exists,Removed"})
                os.remove(self.output_path)
            with open(self.output_path, 'w', encoding='utf8') as fp:
                fp.write(subtitle.string)
            self.signal.emit({"type": str, "data": f"[Output] Output into {os.path.realpath(self.output_path)}"})
            self.signal.emit({"type": bool, "data": True})
