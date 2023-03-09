# -*- coding: utf-8 -*-
import datetime
import json
import os
from typing import Union

import ass
from ass.data import Color

from script.tools import timedelta_to_string


class Subtitle:
    class ScriptInfo:
        def __init__(self, data: dict):
            self.Title: str = data.get("Title") or "Default Aegisub file"
            self.ScriptType: str = data.get("ScriptType") or "v4.00+"
            if 'PlayResX' not in data or "PlayResY" not in data:
                raise KeyError
            self.PlayResX: int = data.get("PlayResX")
            self.PlayResY: int = data.get("PlayResY")

        @property
        def dict(self):
            return {
                "Title": self.Title,
                "ScriptType": self.ScriptType,
                "PlayResX": self.PlayResX,
                "PlayResY": self.PlayResY
            }

        @property
        def string(self):
            result = ("[Script Info]\n"
                      f"Title: {self.Title or 'Default Aegisub file'}\n"
                      f"ScriptType: {self.ScriptType or 'v4.00+'}\n"
                      f'PlayResX: {self.PlayResX}\n'
                      f'PlayResY: {self.PlayResY}\n')
            return result

    class Garbage:
        def __init__(self, data: dict):
            self.AudioFile: None = data.get("audio") or data.get("../video")
            self.VideoFile: None = data.get("../video")

        @property
        def dict(self):
            return {
                "AudioFile": self.AudioFile,
                "VideoFile": self.VideoFile
            }

        @property
        def string(self):
            result = [
                "[Aegisub Project Garbage]",
                f"Audio File: {os.path.realpath(self.AudioFile)}" if self.AudioFile else "",
                f"Video File: {os.path.realpath(self.VideoFile)}" if self.VideoFile else ""
            ]
            return "\n".join(result).strip()

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
                return f"Style:{self.Name},{self.Fontname},{int(self.Fontsize)}," \
                       f"{self.PrimaryColour},{self.SecondaryColour},{self.OutlineColour},{self.BackColour}," \
                       f"{int(self.Bold)},{int(self.Italic)},{int(self.Underline)},{int(self.StrikeOut)}," \
                       f"{int(self.ScaleX)},{int(self.ScaleY)}," \
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
                    "Type": self.Type, "Layer": self.Layer, "Start": self.Start, "End": self.End, "Style": self.Style,
                    "Name": self.Name, "MarginL": self.MarginL, "MarginR": self.MarginR, "MarginV": self.MarginV,
                    "Effect": self.Effect, "Text": self.Text
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
        data = {
            "ScriptInfo": {
                key: doc.info.get(key)
                for key in ["Title", "ScriptType", "ScaledBorderAndShadow", "PlayResX", "PlayResY"]
            },
            "Garbage": {},
            "Styles": styles,
            "Events": events
        }
        return Subtitle(data)


class AssDraw:
    class Move:
        def __init__(self, point: list[int, int]):
            self.point = point

        def move(self, offset: list[int, int]):
            self.point[0] = int(self.point[0] + offset[0])
            self.point[1] = int(self.point[1] + offset[1])

        def scale(self, coefficient: list[float, float]):
            self.point[0] = int(self.point[0] * coefficient[0])
            self.point[1] = int(self.point[1] * coefficient[1])

        @property
        def string(self):
            return f'm {self.point[0]} {self.point[1]}'

    class Bezier:
        def __init__(self, points: list[list[int, int], list[int, int], list[int, int]]):
            self.points = points

        def move(self, offset: list[int, int]):
            for i in [0, 1, 2]:
                self.points[i][0] = int(self.points[i][0] + offset[0])
                self.points[i][1] = int(self.points[i][1] + offset[1])

        def scale(self, coefficient: list[float, float]):
            for i in [0, 1, 2]:
                self.points[i][0] = int(self.points[i][0] * coefficient[0])
                self.points[i][1] = int(self.points[i][1] * coefficient[1])

        @property
        def string(self):
            return f'b ' + ' '.join([' '.join(map(str, x)) for x in self.points])

    class Line:
        def __init__(self, point: list[int, int]):
            self.point = point

        def move(self, offset: list[int, int]):
            self.point[0] = int(self.point[0] + offset[0])
            self.point[1] = int(self.point[1] + offset[1])

        def scale(self, coefficient: list[float, float]):
            self.point[0] = int(self.point[0] * coefficient[0])
            self.point[1] = int(self.point[1] * coefficient[1])

        @property
        def string(self):
            return f'l {self.point[0]} {self.point[1]}'

    def __init__(self, string: str):
        self.ad_list: list[Union[AssDraw.Move, AssDraw.Bezier, AssDraw.Line]] = self.generate_ad_string(string)

    def generate_ad_string(self, string: str) -> list:
        i = 0
        blist = string.split(' ')
        blist: list = [int(x) if x.isdigit() else x for x in blist]
        result = []
        while i < len(blist):
            if blist[i] == 'm':
                result.append(self.Move([int(blist[i + 1]), int(blist[i + 2])]))
                i += 3
            elif blist[i] == 'b':
                result.append(
                    self.Bezier(
                        [[int(blist[i + 1]), int(blist[i + 2])],
                         [int(blist[i + 3]), int(blist[i + 4])],
                         [int(blist[i + 5]), int(blist[i + 6])]]
                    )
                )
                i += 7
            elif blist[i] == 'l':
                result.append(self.Line([int(blist[i + 1]), int(blist[i + 2])]))
                i += 3
        return result

    def move(self, offset: list[int, int]):
        for x in self.ad_list:
            x.move(offset)

    def scale(self, coefficient: Union[list[float, float], float]):
        if not isinstance(coefficient, list):
            c = [coefficient, coefficient]
        else:
            c = coefficient
        for x in self.ad_list:
            x.scale(c)

    def string(self):
        return ' '.join([x.string for x in self.ad_list])
