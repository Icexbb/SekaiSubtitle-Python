import datetime
import json
import os

import ass
from ass.data import Color


class Subtitle:
    class ScriptInfo:
        def __init__(self, data: dict):
            self.Title: None = data.get("Title")
            self.ScriptType: None = data.get("ScriptType")
            self.ScaledBorderAndShadow: None = data.get("ScaledBorderAndShadow")
            self.YCbCr_matrix: None = data.get("YCbCr Matrix")
            if 'PlayResX' not in data or "PlayResY" not in data:
                raise KeyError
            self.PlayResX: int = data.get("PlayResX")
            self.PlayResY: int = data.get("PlayResY")

        @property
        def dict(self):
            return {
                "Title": self.Title,
                "ScriptType": self.ScriptType,
                "ScaledBorderAndShadow": self.ScaledBorderAndShadow,
                "YCbCr_matrix": self.YCbCr_matrix,
                "PlayResX": self.PlayResX,
                "PlayResY": self.PlayResY
            }

        @property
        def string(self):
            result = ("[Script Info]\n"
                      f"Title: {self.Title or 'Default Aegisub file'}\n"
                      f"ScriptType: {self.ScriptType or 'v4.00+'}\n"
                      f"WrapStyle: 0"
                      f"ScaledBorderAndShadow: {'yes' if self.ScaledBorderAndShadow else 'no'}\n"
                      f"YCbCr Matrix: {self.YCbCr_matrix}\n"
                      f'PlayResX: {self.PlayResX}\n'
                      f'PlayResY: {self.PlayResY}')
            return result

    class Garbage:
        def __init__(self, data: dict):
            self.AudioFile: None = data.get("audio") or data.get("video")
            self.VideoFile: None = data.get("video")

        @property
        def dict(self):
            return {
                "AudioFile": self.AudioFile,
                "VideoFile": self.VideoFile
            }

        @property
        def string(self):
            result = ("[Aegisub Project Garbage]\n"
                      f"Audio File: {self.AudioFile}\n"
                      f"Video File: {self.VideoFile}"
                      )
            return result

    class Styles:
        class StyleItem:

            def __init__(self, data: dict):
                self.Name: str = data.get("Name") or "Default"
                self.Fontname: str = data.get("Fontname") or "Arial"
                self.Fontsize: int = data.get("Fontsize") or 48
                self.PrimaryColour: str = data.get("PrimaryColour") or "&H00FFFFFF"
                self.SecondaryColour: str = data.get("SecondaryColour") or "&H00FFFFFF"
                self.OutlineColour: str = data.get("OutlineColour") or "&H00000000"
                self.BackColour: str = data.get("BackColour") or "&H00000000"
                self.Bold: bool = data.get("Bold") or 0
                self.Italic: bool = data.get("Italic") or 0
                self.Underline: bool = data.get("Underline") or 0
                self.StrikeOut: bool = data.get("StrikeOut") or 0
                self.ScaleX: int = data.get("ScaleX") or 100
                self.ScaleY: int = data.get("ScaleY") or 100
                self.Spacing: float = data.get("Spacing") or 0
                self.Angle: int = data.get("Angle") or 0
                self.BorderStyle: int = data.get("BorderStyle")
                self.Outline: float = data.get("Outline") or 0
                self.Shadow: float = data.get("Shadow") or 0
                self.Alignment: int = data.get("Alignment") or 2
                self.MarginL: int = data.get("MarginL") or 10
                self.MarginR: int = data.get("MarginR") or 10
                self.MarginV: int = data.get("MarginV") or 50
                self.Encoding = data.get("Encoding") or 1

            @property
            def dict(self):
                return {
                    "Name": self.Name, "Fontname": self.Fontname, "Fontsize": self.Fontsize,
                    "PrimaryColour": self.PrimaryColour, "SecondaryColour": self.SecondaryColour,
                    "OutlineColour": self.OutlineColour, "BackColour": self.BackColour, "Bold": self.Bold,
                    "Italic": self.Italic, "Underline": self.Underline, "StrikeOut": self.StrikeOut,
                    "ScaleX": self.ScaleX, "ScaleY": self.ScaleY, "Spacing": self.Spacing, "Angle": self.Angle,
                    "BorderStyle": self.BorderStyle, "Outline": self.Outline, "Shadow": self.Shadow,
                    "Alignment": self.Alignment, "MarginL": self.MarginL, "MarginR": self.MarginR,
                    "MarginV": self.MarginV, "Encoding": self.Encoding
                }

            @property
            def string(self):
                return f"Style:{self.Name},{self.Fontname},{self.Fontsize}," \
                       f"{self.PrimaryColour},{self.SecondaryColour},{self.OutlineColour},{self.BackColour}," \
                       f"{self.Bold},{self.Italic},{self.Underline},{self.StrikeOut},{self.ScaleX},{self.ScaleY}," \
                       f"{self.Spacing},{self.Angle},{self.BorderStyle},{self.Outline},{self.Shadow}," \
                       f"{self.Alignment},{self.MarginL},{self.MarginR},{self.MarginV},{self.Encoding}"

        def __init__(self, data: list):
            self.header = "Format: Name, Fontname, Fontsize, " \
                          "PrimaryColour, SecondaryColour, OutlineColour, BackColour, " \
                          "Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, " \
                          "BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding"
            self.items = [self.StyleItem(item) for item in data]

        @property
        def list(self):
            return [item.dict for item in self.items]

        @property
        def string(self):
            result = f"[V4+ Styles]\n{self.header}\n" + "\n".join([item.string for item in self.items])
            return result

    class Events:
        class EventItem:
            def __init__(self, data: dict):
                self.Type: str = data.get("Type") or "Dialogue"
                self.Layer: int = data.get("Layer") or 0
                self.Start: str = data.get("Start") or "0:00:00.00"
                self.End: str = data.get("End") or "0:00:05.00"
                self.Style: str = data.get("Style") or "Default"
                self.Name: str = data.get("Name") or ""
                self.MarginL: int = data.get("MarginL") or 0
                self.MarginR: int = data.get("MarginR") or 0
                self.MarginV: int = data.get("MarginV") or 0
                self.Effect: str = data.get("Effect") or ""
                self.Text: str = data.get("Text") or ""

            @property
            def dict(self):
                return {
                    "Layer": self.Layer, "Start": self.Start, "End": self.End, "Style": self.Style, "Name": self.Name,
                    "MarginL": self.MarginL, "MarginR": self.MarginR, "MarginV": self.MarginV, "Effect": self.Effect,
                    "Text": self.Text
                }

            @property
            def string(self):
                result = f"{self.Type}: {self.Layer},{self.Start},{self.End},{self.Style},{self.Name}," \
                         f"{self.MarginL},{self.MarginR},{self.MarginV},{self.Effect},{self.Text}"
                return result

        def __init__(self, data: list):
            self.header = "Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text"
            self.items = [self.EventItem(item) for item in data]

        @property
        def list(self):
            return [item.dict for item in self.items]

        @property
        def string(self):
            result = f"[Events]\n{self.header}\n" + "\n".join([item.string for item in self.items])
            return result

    def __init__(self, data: dict):
        self.info = Subtitle.ScriptInfo(data.get("ScriptInfo"))
        self.garbage = Subtitle.Garbage(data.get("Garbage"))
        self.styles = Subtitle.Styles(data.get("Styles"))
        self.events = Subtitle.Events(data.get("Events"))

    @property
    def dict(self):
        return {
            "ScriptInfo": self.info.dict,
            "Garbage": self.garbage.dict,
            "Styles": self.styles.list,
            "Events": self.events.list
        }

    @property
    def string(self):
        result = f"{self.info.string}\n{self.garbage.string}\n{self.styles.string}\n{self.events.string}"
        return result


def from_file_generate(file_path: str) -> Subtitle:
    if not os.path.exists(file_path):
        raise FileNotFoundError

    if os.path.splitext(file_path)[-1] == ".json":
        data = json.load(open(file_path, 'r', encoding="utf8"))
        return Subtitle(data)
    else:
        with open(file_path, 'r', encoding="utf-8-sig") as fp:
            doc = ass.parse(fp)
        styles = []
        for style in doc.styles:
            data = style.__dict__['fields']
            result = {}
            for key in data:
                value = data.get(key)
                if isinstance(value, Color):
                    res = value.to_ass()
                elif isinstance(value, bool):
                    res = int(value)
                else:
                    res = value
                result[key] = res
            styles.append(result)
        events = []
        for event in doc.events:
            data = event.__dict__['fields']
            result = {}
            for key in data:
                value = data.get(key)
                if isinstance(value, datetime.timedelta):
                    res = timedelta_to_string(value)
                elif isinstance(value, bool):
                    res = int(value)
                else:
                    res = value
                result[key] = res
            events.append(result)
        print(styles)
        data = {
            "ScriptInfo": {
                key: doc.info.get(key)
                for key in ["Title", "ScriptType", "ScaledBorderAndShadow", "YCbCr_matrix", "PlayResX", "PlayResY"]
            },
            "Garbage": {},
            "Styles": styles,
            "Events": events
        }
        return Subtitle(data)


"""
    text_box_mx = TextBox([340, 1576, 746, 896])
    text_box_mx.scale([pattern_coefficient, pattern_coefficient])
    text_box_mx.move_to(screen_data['pattern_center'])
    print(text_box_mx.string)
"""


def timedelta_to_string(time: datetime.timedelta):
    ms = f"{time.microseconds / 10000:.0f}"
    s = f"{time.seconds % 60:02d}"
    m = f"{time.seconds // 60:02d}"
    h = f"{time.seconds // 3600}"
    return f"{h}:{m}:{s}.{ms}"
