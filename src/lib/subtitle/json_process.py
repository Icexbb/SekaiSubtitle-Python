import json
import os

from PySide6.QtCore import Signal

from . import timedelta_to_string, check_distance
from .data import subtitle_styles, DISPLAY_NAME_STYLE
from .reference import get_dialog_mask, get_area_mask
from .subtitle import Subtitle
from .video_process import Frame


class Episode:
    def __init__(
            self,
            file_path: str, json_file: str, output_path: str,
            frames: list[Frame],
            screen_data: dict,
            point_center: tuple,
            point_size: int,
            video_size: tuple,
            signal: Signal
    ):
        self.file_path = file_path
        self.output_path = output_path
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
                count = 1
                last_move = ""
                start = range_frame[0]
                for j in range_frame:
                    move = ""
                    if self.frames[j].point:
                        move = r"{\pos(" \
                               f"{int(self.frames[j].point[0] - 0.5 * self.point_size)}," \
                               f"{int(self.frames[j].point[1] + 1.25 * self.point_size)}" \
                               r")}"
                    if last_move != move or j == range_frame[-1]:
                        event_data = {
                            "Layer": 1,
                            "Start": timedelta_to_string(self.frames[start].timestamp),
                            "End": timedelta_to_string(self.frames[start + count].timestamp),
                            "Style": style,
                            "Name": item['WindowDisplayName'],
                            "MarginL": 0, "MarginR": 0, "MarginV": 0,
                            "Effect": '',
                            "Text": move + item["Body"].replace("\n", r"\N")
                        }
                        start = j
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

    def save_ass(self):
        dia, jit = self.generate_ass_dialog()
        d_mask = self.generate_ass_dialog_mask(jit)
        a_mask = self.generate_ass_area_mask()
        try:
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
            return
        if os.path.exists(self.output_path):
            self.signal.emit({"type": str, "data": "[Output] File Exists,Removed"})
            os.remove(self.output_path)
        with open(self.output_path, 'w', encoding='utf8') as fp:
            fp.write(subtitle.string)
        self.signal.emit({"type": str, "data": f"[Output] Output into {os.path.realpath(self.output_path)}"})
