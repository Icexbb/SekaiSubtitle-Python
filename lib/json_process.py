import json
import os.path

from lib import timedelta_to_string
from lib.reference import get_dialog_mask, get_area_mask
from lib.subtitle import Subtitle
from lib.video_process import Frame

DISPLAY_NAME_STYLE = json.load(
    open(os.path.join(os.path.dirname(__file__), "asset/name_style.json"), "r", encoding="utf8"))

subtitle_styles = json.load(
    open(os.path.join(os.path.dirname(__file__), "asset/subtitle_styles.json"), "r", encoding="utf8"))


class Episode:
    def __init__(
            self,
            file_path: str, json_file: str, output_path: str,
            frames: list[Frame],
            screen_data: dict,
            point_center: tuple,
            point_size: int,
            video_size: tuple
    ):
        self.file_path = file_path
        self.output_path = output_path
        self.dialog_mask = get_dialog_mask(screen_data)
        self.area_mask = get_area_mask(screen_data)
        self.screen_data = screen_data
        self.point_center = point_center
        self.point_size = point_size
        self.video_size = video_size

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
        assert len(area_mask_frame_pair) == len(self.area_mask_data), "Area Mask and Json Data Not Correspond"
        results = []
        for i in range(len(area_mask_frame_pair)):
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

    def generate_ass_dialog_mask(self):
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
            event_mask = {
                "Layer": 0, "Style": DISPLAY_NAME_STYLE["screen"],
                "Start": timedelta_to_string(pair[0].timestamp),
                "End": timedelta_to_string(pair[1].timestamp),
                "Name": '', "MarginL": 0, "MarginR": 0, "MarginV": 0, "Effect": '',
                "Text": self.dialog_mask
            }
            results.append(event_mask)
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
        for i in range(len(dialog_frame_pair)):
            item = self.talk_data_data[i]
            pair = dialog_frame_pair[i]
            style = DISPLAY_NAME_STYLE[item['WindowDisplayName']] \
                if item['WindowDisplayName'] in DISPLAY_NAME_STYLE else "関連人物"
            event_data = {
                "Layer": 1,
                "Start": timedelta_to_string(pair[0].timestamp),
                "End": timedelta_to_string(pair[1].timestamp),
                "Style": style,
                "Name": item['WindowDisplayName'],
                "MarginL": 0, "MarginR": 0, "MarginV": 0,
                "Effect": '',
                "Text": item["Body"].replace("\n", r"\N")
            }
            results.append(event_data)
        return results

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

        res = {
            "ScriptInfo": {"PlayResX": self.video_size[0], "PlayResY": self.video_size[1]},
            "Garbage": {"video": self.file_path},
            "Styles": self.generate_styles(),
            "Events": Subtitle.Events(
                self.generate_ass_dialog_mask() + self.generate_ass_area_mask() + self.generate_ass_dialog()).list,
        }
        subtitle = Subtitle(res)
        if os.path.exists(self.output_path):
            print(f"[Output] File Exists,Removed")
            os.remove(self.output_path)
        with open(self.output_path, 'w', encoding='utf8') as fp:
            fp.write(subtitle.string)
        print(f"[Output] Output into {os.path.realpath(self.output_path)}")
