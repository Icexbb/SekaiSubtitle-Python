# -*- coding: utf-8 -*-
import os
import sys

import cv2

chara_name = {
    "1": "一歌", "2": "咲希", "3": "穗波", "4": "志步",
    "5": "实乃理", "6": "遥", "7": "爱莉", "8": "雫",
    "9": "心羽", "10": "杏", "11": "彰人", "12": "冬弥",
    "13": "司", "14": "笑梦", "15": "宁宁", "16": "类",
    "17": "奏", "18": "真冬", "19": "绘名", "20": "瑞希",
    "21": "MIKU", "22": "RIN", "23": "LEN",
    "24": "LUKA", "25": "MEIKO", "26": "KAITO",
}
staff_style_format = {
    "Name": "staff",
    "Fontname": "思源黑体 CN Bold",
    "Fontsize": 83,
    "PrimaryColour": "&H00715659",
    "SecondaryColour": "&H000000FF",
    "OutlineColour": "&H00FFFFFF",
    "BackColour": "&H00000000",
    "Bold": 0,
    "Italic": 0,
    "Underline": 0,
    "StrikeOut": 0,
    "ScaleX": 100.0,
    "ScaleY": 100.0,
    "Spacing": 0,
    "Angle": 0,
    "BorderStyle": 1,
    "Outline": 5.0,
    "Shadow": 5.0,
    "Alignment": 7,
    "MarginL": 30,
    "MarginR": 10,
    "MarginV": 30,
    "Encoding": 1
}
subtitle_styles_format = {
    "初音ミク": {
        "Name": "初音ミク",
        "Fontname": "思源黑体 CN Bold",
        "Fontsize": 83.0,
        "PrimaryColour": "&H00BBCC33",
        "SecondaryColour": "&H000000FF",
        "OutlineColour": "&H00FFFFFF",
        "BackColour": "&H00BBCC33",
        "Bold": 0,
        "Italic": 0,
        "Underline": 0,
        "StrikeOut": 0,
        "ScaleX": 100.0,
        "ScaleY": 100.0,
        "Spacing": 0,
        "Angle": 0,
        "BorderStyle": 1,
        "Outline": 3.0,
        "Shadow": 0,
        "Alignment": 7,
        "MarginL": 325,
        "MarginR": 10,
        "MarginV": 1240,
        "Encoding": 1
    },
    "鏡音リン": {
        "Name": "鏡音リン",
        "Fontname": "思源黑体 CN Bold",
        "Fontsize": 83.0,
        "PrimaryColour": "&H0011CCFF",
        "SecondaryColour": "&H000000FF",
        "OutlineColour": "&H00FFFFFF",
        "BackColour": "&H0011CCFF",
        "Bold": 0,
        "Italic": 0,
        "Underline": 0,
        "StrikeOut": 0,
        "ScaleX": 100.0,
        "ScaleY": 100.0,
        "Spacing": 0,
        "Angle": 0,
        "BorderStyle": 1,
        "Outline": 3.0,
        "Shadow": 0,
        "Alignment": 7,
        "MarginL": 325,
        "MarginR": 10,
        "MarginV": 1240,
        "Encoding": 1
    },
    "鏡音レン": {
        "Name": "鏡音レン",
        "Fontname": "思源黑体 CN Bold",
        "Fontsize": 83.0,
        "PrimaryColour": "&H0011EEFF",
        "SecondaryColour": "&H000000FF",
        "OutlineColour": "&H000996B5",
        "BackColour": "&H0011EEFF",
        "Bold": 0,
        "Italic": 0,
        "Underline": 0,
        "StrikeOut": 0,
        "ScaleX": 100.0,
        "ScaleY": 100.0,
        "Spacing": 0,
        "Angle": 0,
        "BorderStyle": 1,
        "Outline": 3.0,
        "Shadow": 0,
        "Alignment": 7,
        "MarginL": 325,
        "MarginR": 10,
        "MarginV": 1240,
        "Encoding": 1
    },
    "巡音ルカ": {
        "Name": "巡音ルカ",
        "Fontname": "思源黑体 CN Bold",
        "Fontsize": 83.0,
        "PrimaryColour": "&H00CCBBFF",
        "SecondaryColour": "&H000000FF",
        "OutlineColour": "&H00BB66FF",
        "BackColour": "&H00CCBBFF",
        "Bold": 0,
        "Italic": 0,
        "Underline": 0,
        "StrikeOut": 0,
        "ScaleX": 100.0,
        "ScaleY": 100.0,
        "Spacing": 0,
        "Angle": 0,
        "BorderStyle": 1,
        "Outline": 3.0,
        "Shadow": 0,
        "Alignment": 7,
        "MarginL": 325,
        "MarginR": 10,
        "MarginV": 1240,
        "Encoding": 1
    },
    "MEIKO": {
        "Name": "MEIKO",
        "Fontname": "思源黑体 CN Bold",
        "Fontsize": 83.0,
        "PrimaryColour": "&H004444DD",
        "SecondaryColour": "&H000000FF",
        "OutlineColour": "&H00FFFFFF",
        "BackColour": "&H004444DD",
        "Bold": 0,
        "Italic": 0,
        "Underline": 0,
        "StrikeOut": 0,
        "ScaleX": 100.0,
        "ScaleY": 100.0,
        "Spacing": 0,
        "Angle": 0,
        "BorderStyle": 1,
        "Outline": 3.0,
        "Shadow": 0,
        "Alignment": 7,
        "MarginL": 325,
        "MarginR": 10,
        "MarginV": 1240,
        "Encoding": 1
    },
    "KAITO": {
        "Name": "KAITO",
        "Fontname": "思源黑体 CN Bold",
        "Fontsize": 83.0,
        "PrimaryColour": "&H00FF0000",
        "SecondaryColour": "&H000000FF",
        "OutlineColour": "&H00FFFFFF",
        "BackColour": "&H00FF0000",
        "Bold": 0,
        "Italic": 0,
        "Underline": 0,
        "StrikeOut": 0,
        "ScaleX": 100.0,
        "ScaleY": 100.0,
        "Spacing": 0,
        "Angle": 0,
        "BorderStyle": 1,
        "Outline": 3.0,
        "Shadow": 0,
        "Alignment": 7,
        "MarginL": 325,
        "MarginR": 10,
        "MarginV": 1240,
        "Encoding": 1
    },
    "星乃一歌": {
        "Name": "星乃一歌",
        "Fontname": "思源黑体 CN Bold",
        "Fontsize": 83.0,
        "PrimaryColour": "&H00EEAA33",
        "SecondaryColour": "&H000000FF",
        "OutlineColour": "&H00FFFFFF",
        "BackColour": "&H00EEAA33",
        "Bold": 0,
        "Italic": 0,
        "Underline": 0,
        "StrikeOut": 0,
        "ScaleX": 100.0,
        "ScaleY": 100.0,
        "Spacing": 0,
        "Angle": 0,
        "BorderStyle": 1,
        "Outline": 3.0,
        "Shadow": 0,
        "Alignment": 7,
        "MarginL": 325,
        "MarginR": 10,
        "MarginV": 1240,
        "Encoding": 1
    },
    "天馬咲希": {
        "Name": "天馬咲希",
        "Fontname": "思源黑体 CN Bold",
        "Fontsize": 83.0,
        "PrimaryColour": "&H0043D9FE",
        "SecondaryColour": "&H000000FF",
        "OutlineColour": "&H00F17CFD",
        "BackColour": "&H0044DDFF",
        "Bold": 0,
        "Italic": 0,
        "Underline": 0,
        "StrikeOut": 0,
        "ScaleX": 100.0,
        "ScaleY": 100.0,
        "Spacing": 0,
        "Angle": 0,
        "BorderStyle": 1,
        "Outline": 3.0,
        "Shadow": 0,
        "Alignment": 7,
        "MarginL": 325,
        "MarginR": 10,
        "MarginV": 1240,
        "Encoding": 1
    },
    "望月穗波": {
        "Name": "望月穗波",
        "Fontname": "思源黑体 CN Bold",
        "Fontsize": 83.0,
        "PrimaryColour": "&H006666EE",
        "SecondaryColour": "&H000000FF",
        "OutlineColour": "&H00FFFFFF",
        "BackColour": "&H006666EE",
        "Bold": 0,
        "Italic": 0,
        "Underline": 0,
        "StrikeOut": 0,
        "ScaleX": 100.0,
        "ScaleY": 100.0,
        "Spacing": 0,
        "Angle": 0,
        "BorderStyle": 1,
        "Outline": 3.0,
        "Shadow": 0,
        "Alignment": 7,
        "MarginL": 325,
        "MarginR": 10,
        "MarginV": 1240,
        "Encoding": 1
    },
    "日野森志步": {
        "Name": "日野森志步",
        "Fontname": "思源黑体 CN Bold",
        "Fontsize": 83.0,
        "PrimaryColour": "&H0022DDBB",
        "SecondaryColour": "&H000000FF",
        "OutlineColour": "&H00828B54",
        "BackColour": "&H0022DDBB",
        "Bold": 0,
        "Italic": 0,
        "Underline": 0,
        "StrikeOut": 0,
        "ScaleX": 100.0,
        "ScaleY": 100.0,
        "Spacing": 0,
        "Angle": 0,
        "BorderStyle": 1,
        "Outline": 3.0,
        "Shadow": 0,
        "Alignment": 7,
        "MarginL": 325,
        "MarginR": 10,
        "MarginV": 1240,
        "Encoding": 1
    },
    "花里みのり": {
        "Name": "花里みのり",
        "Fontname": "思源黑体 CN Bold",
        "Fontsize": 83.0,
        "PrimaryColour": "&H00AACCFF",
        "SecondaryColour": "&H000000FF",
        "OutlineColour": "&H006B6CC4",
        "BackColour": "&H00AACCFF",
        "Bold": 0,
        "Italic": 0,
        "Underline": 0,
        "StrikeOut": 0,
        "ScaleX": 100.0,
        "ScaleY": 100.0,
        "Spacing": 0,
        "Angle": 0,
        "BorderStyle": 1,
        "Outline": 3.0,
        "Shadow": 0,
        "Alignment": 7,
        "MarginL": 325,
        "MarginR": 10,
        "MarginV": 1240,
        "Encoding": 1
    },
    "桐谷遥": {
        "Name": "桐谷遥",
        "Fontname": "思源黑体 CN Bold",
        "Fontsize": 83.0,
        "PrimaryColour": "&H00FFCC99",
        "SecondaryColour": "&H000000FF",
        "OutlineColour": "&H00B78240",
        "BackColour": "&H00FFCC99",
        "Bold": 0,
        "Italic": 0,
        "Underline": 0,
        "StrikeOut": 0,
        "ScaleX": 100.0,
        "ScaleY": 100.0,
        "Spacing": 0,
        "Angle": 0,
        "BorderStyle": 1,
        "Outline": 3.0,
        "Shadow": 0,
        "Alignment": 7,
        "MarginL": 325,
        "MarginR": 10,
        "MarginV": 1240,
        "Encoding": 1
    },
    "桃井愛莉": {
        "Name": "桃井愛莉",
        "Fontname": "思源黑体 CN Bold",
        "Fontsize": 83.0,
        "PrimaryColour": "&H00CCAAFF",
        "SecondaryColour": "&H000000FF",
        "OutlineColour": "&H009454C6",
        "BackColour": "&H00CCAAFF",
        "Bold": 0,
        "Italic": 0,
        "Underline": 0,
        "StrikeOut": 0,
        "ScaleX": 100.0,
        "ScaleY": 100.0,
        "Spacing": 0,
        "Angle": 0,
        "BorderStyle": 1,
        "Outline": 3.0,
        "Shadow": 0,
        "Alignment": 7,
        "MarginL": 325,
        "MarginR": 10,
        "MarginV": 1240,
        "Encoding": 1
    },
    "日野森雫": {
        "Name": "日野森雫",
        "Fontname": "思源黑体 CN Bold",
        "Fontsize": 83.0,
        "PrimaryColour": "&H00DDEE99",
        "SecondaryColour": "&H000000FF",
        "OutlineColour": "&H007DA237",
        "BackColour": "&H00DFEFA6",
        "Bold": 0,
        "Italic": 0,
        "Underline": 0,
        "StrikeOut": 0,
        "ScaleX": 100.0,
        "ScaleY": 100.0,
        "Spacing": 0,
        "Angle": 0,
        "BorderStyle": 1,
        "Outline": 3.0,
        "Shadow": 0,
        "Alignment": 7,
        "MarginL": 325,
        "MarginR": 10,
        "MarginV": 1240,
        "Encoding": 1
    },
    "小豆沢こはね": {
        "Name": "小豆沢こはね",
        "Fontname": "思源黑体 CN Bold",
        "Fontsize": 83.0,
        "PrimaryColour": "&H009966FF",
        "SecondaryColour": "&H000000FF",
        "OutlineColour": "&H00FFFFFF",
        "BackColour": "&H009966FF",
        "Bold": 0,
        "Italic": 0,
        "Underline": 0,
        "StrikeOut": 0,
        "ScaleX": 100.0,
        "ScaleY": 100.0,
        "Spacing": 0,
        "Angle": 0,
        "BorderStyle": 1,
        "Outline": 3.0,
        "Shadow": 0,
        "Alignment": 7,
        "MarginL": 325,
        "MarginR": 10,
        "MarginV": 1240,
        "Encoding": 1
    },
    "白石杏": {
        "Name": "白石杏",
        "Fontname": "思源黑体 CN Bold",
        "Fontsize": 83.0,
        "PrimaryColour": "&H00DDBB00",
        "SecondaryColour": "&H000000FF",
        "OutlineColour": "&H00FFFFFF",
        "BackColour": "&H00DDBB00",
        "Bold": 0,
        "Italic": 0,
        "Underline": 0,
        "StrikeOut": 0,
        "ScaleX": 100.0,
        "ScaleY": 100.0,
        "Spacing": 0,
        "Angle": 0,
        "BorderStyle": 1,
        "Outline": 3.0,
        "Shadow": 0,
        "Alignment": 7,
        "MarginL": 325,
        "MarginR": 10,
        "MarginV": 1240,
        "Encoding": 1
    },
    "東雲彰人": {
        "Name": "東雲彰人",
        "Fontname": "思源黑体 CN Bold",
        "Fontsize": 83.0,
        "PrimaryColour": "&H002277FF",
        "SecondaryColour": "&H000000FF",
        "OutlineColour": "&H00FFFFFF",
        "BackColour": "&H002277FF",
        "Bold": 0,
        "Italic": 0,
        "Underline": 0,
        "StrikeOut": 0,
        "ScaleX": 100.0,
        "ScaleY": 100.0,
        "Spacing": 0,
        "Angle": 0,
        "BorderStyle": 1,
        "Outline": 3.0,
        "Shadow": 0,
        "Alignment": 7,
        "MarginL": 325,
        "MarginR": 10,
        "MarginV": 1240,
        "Encoding": 1
    },
    "青柳冬弥": {
        "Name": "青柳冬弥",
        "Fontname": "思源黑体 CN Bold",
        "Fontsize": 83.0,
        "PrimaryColour": "&H00DD7700",
        "SecondaryColour": "&H000000FF",
        "OutlineColour": "&H00FFFFFF",
        "BackColour": "&H00DD7700",
        "Bold": 0,
        "Italic": 0,
        "Underline": 0,
        "StrikeOut": 0,
        "ScaleX": 100.0,
        "ScaleY": 100.0,
        "Spacing": 0,
        "Angle": 0,
        "BorderStyle": 1,
        "Outline": 3.0,
        "Shadow": 0,
        "Alignment": 7,
        "MarginL": 325,
        "MarginR": 10,
        "MarginV": 1240,
        "Encoding": 1
    },
    "天馬司": {
        "Name": "天馬司",
        "Fontname": "思源黑体 CN Bold",
        "Fontsize": 83.0,
        "PrimaryColour": "&H0000BBFF",
        "SecondaryColour": "&H000000FF",
        "OutlineColour": "&H00FFFFFF",
        "BackColour": "&H0000BBFF",
        "Bold": 0,
        "Italic": 0,
        "Underline": 0,
        "StrikeOut": 0,
        "ScaleX": 100.0,
        "ScaleY": 100.0,
        "Spacing": 0,
        "Angle": 0,
        "BorderStyle": 1,
        "Outline": 3.0,
        "Shadow": 0,
        "Alignment": 7,
        "MarginL": 325,
        "MarginR": 10,
        "MarginV": 1240,
        "Encoding": 1
    },
    "鳳えむ": {
        "Name": "鳳えむ",
        "Fontname": "思源黑体 CN Bold",
        "Fontsize": 83.0,
        "PrimaryColour": "&H00BB66FF",
        "SecondaryColour": "&H000000FF",
        "OutlineColour": "&H00FFFFFF",
        "BackColour": "&H00BB66FF",
        "Bold": 0,
        "Italic": 0,
        "Underline": 0,
        "StrikeOut": 0,
        "ScaleX": 100.0,
        "ScaleY": 100.0,
        "Spacing": 0,
        "Angle": 0,
        "BorderStyle": 1,
        "Outline": 3.0,
        "Shadow": 0,
        "Alignment": 7,
        "MarginL": 325,
        "MarginR": 10,
        "MarginV": 1240,
        "Encoding": 1
    },
    "草薙寧々": {
        "Name": "草薙寧々",
        "Fontname": "思源黑体 CN Bold",
        "Fontsize": 83.0,
        "PrimaryColour": "&H0099DD33",
        "SecondaryColour": "&H000000FF",
        "OutlineColour": "&H00FFFFFF",
        "BackColour": "&H0099DD33",
        "Bold": 0,
        "Italic": 0,
        "Underline": 0,
        "StrikeOut": 0,
        "ScaleX": 100.0,
        "ScaleY": 100.0,
        "Spacing": 0,
        "Angle": 0,
        "BorderStyle": 1,
        "Outline": 3.0,
        "Shadow": 0,
        "Alignment": 7,
        "MarginL": 325,
        "MarginR": 10,
        "MarginV": 1240,
        "Encoding": 1
    },
    "神代類": {
        "Name": "神代類",
        "Fontname": "思源黑体 CN Bold",
        "Fontsize": 83.0,
        "PrimaryColour": "&H00EE88BB",
        "SecondaryColour": "&H000000FF",
        "OutlineColour": "&H00FFFFFF",
        "BackColour": "&H00EE88BB",
        "Bold": 0,
        "Italic": 0,
        "Underline": 0,
        "StrikeOut": 0,
        "ScaleX": 100.0,
        "ScaleY": 100.0,
        "Spacing": 0,
        "Angle": 0,
        "BorderStyle": 1,
        "Outline": 3.0,
        "Shadow": 0,
        "Alignment": 7,
        "MarginL": 325,
        "MarginR": 10,
        "MarginV": 1240,
        "Encoding": 1
    },
    "宵崎奏": {
        "Name": "宵崎奏",
        "Fontname": "思源黑体 CN Bold",
        "Fontsize": 83.0,
        "PrimaryColour": "&H008866BB",
        "SecondaryColour": "&H000000FF",
        "OutlineColour": "&H00FFFFFF",
        "BackColour": "&H008866BB",
        "Bold": 0,
        "Italic": 0,
        "Underline": 0,
        "StrikeOut": 0,
        "ScaleX": 100.0,
        "ScaleY": 100.0,
        "Spacing": 0,
        "Angle": 0,
        "BorderStyle": 1,
        "Outline": 3.0,
        "Shadow": 0,
        "Alignment": 7,
        "MarginL": 325,
        "MarginR": 10,
        "MarginV": 1240,
        "Encoding": 1
    },
    "朝比奈まふゆ": {
        "Name": "朝比奈まふゆ",
        "Fontname": "思源黑体 CN Bold",
        "Fontsize": 83.0,
        "PrimaryColour": "&H00CC8888",
        "SecondaryColour": "&H000000FF",
        "OutlineColour": "&H00FFFFFF",
        "BackColour": "&H00CC8888",
        "Bold": 0,
        "Italic": 0,
        "Underline": 0,
        "StrikeOut": 0,
        "ScaleX": 100.0,
        "ScaleY": 100.0,
        "Spacing": 0,
        "Angle": 0,
        "BorderStyle": 1,
        "Outline": 3.0,
        "Shadow": 0,
        "Alignment": 7,
        "MarginL": 325,
        "MarginR": 10,
        "MarginV": 1240,
        "Encoding": 1
    },
    "東雲絵名": {
        "Name": "東雲絵名",
        "Fontname": "思源黑体 CN Bold",
        "Fontsize": 83.0,
        "PrimaryColour": "&H0088AACC",
        "SecondaryColour": "&H000000FF",
        "OutlineColour": "&H00FFFFFF",
        "BackColour": "&H0088AACC",
        "Bold": 0,
        "Italic": 0,
        "Underline": 0,
        "StrikeOut": 0,
        "ScaleX": 100.0,
        "ScaleY": 100.0,
        "Spacing": 0,
        "Angle": 0,
        "BorderStyle": 1,
        "Outline": 3.0,
        "Shadow": 0,
        "Alignment": 7,
        "MarginL": 325,
        "MarginR": 10,
        "MarginV": 1240,
        "Encoding": 1
    },
    "暁山瑞希": {
        "Name": "暁山瑞希",
        "Fontname": "思源黑体 CN Bold",
        "Fontsize": 83.0,
        "PrimaryColour": "&H00CCAADD",
        "SecondaryColour": "&H000000FF",
        "OutlineColour": "&H008866BB",
        "BackColour": "&H00CCAADD",
        "Bold": 0,
        "Italic": 0,
        "Underline": 0,
        "StrikeOut": 0,
        "ScaleX": 100.0,
        "ScaleY": 100.0,
        "Spacing": 0,
        "Angle": 0,
        "BorderStyle": 1,
        "Outline": 3.0,
        "Shadow": 0,
        "Alignment": 7,
        "MarginL": 325,
        "MarginR": 10,
        "MarginV": 1240,
        "Encoding": 1
    },
    "screen": {
        "Name": "screen",
        "Fontname": "思源黑体 CN Bold",
        "Fontsize": 90.0,
        "PrimaryColour": "&H00FFFFFF",
        "SecondaryColour": "&H000000FF",
        "OutlineColour": "&H00000000",
        "BackColour": "&H00000000",
        "Bold": 0,
        "Italic": 0,
        "Underline": 0,
        "StrikeOut": 0,
        "ScaleX": 100.0,
        "ScaleY": 100.0,
        "Spacing": 0,
        "Angle": 0,
        "BorderStyle": 1,
        "Outline": 0,
        "Shadow": 0,
        "Alignment": 7,
        "MarginL": 10,
        "MarginR": 10,
        "MarginV": 50,
        "Encoding": 1
    },
    "関連人物": {
        "Name": "関連人物",
        "Fontname": "思源黑体 CN Bold",
        "Fontsize": 83.0,
        "PrimaryColour": "&H00715659",
        "SecondaryColour": "&H000000FF",
        "OutlineColour": "&H00FFFFFF",
        "BackColour": "&H00000000",
        "Bold": 0,
        "Italic": 0,
        "Underline": 0,
        "StrikeOut": 0,
        "ScaleX": 100.0,
        "ScaleY": 100.0,
        "Spacing": 0,
        "Angle": 0,
        "BorderStyle": 1,
        "Outline": 3.0,
        "Shadow": 0,
        "Alignment": 7,
        "MarginL": 325,
        "MarginR": 10,
        "MarginV": 1240,
        "Encoding": 1
    },
    "staff": {
        "Name": "staff",
        "Fontname": "思源黑体 CN Bold",
        "Fontsize": 83.0,
        "PrimaryColour": "&H00715659",
        "SecondaryColour": "&H000000FF",
        "OutlineColour": "&H00FFFFFF",
        "BackColour": "&H00000000",
        "Bold": 0,
        "Italic": 0,
        "Underline": 0,
        "StrikeOut": 0,
        "ScaleX": 100.0,
        "ScaleY": 100.0,
        "Spacing": 0,
        "Angle": 0,
        "BorderStyle": 1,
        "Outline": 5.0,
        "Shadow": 5.0,
        "Alignment": 1,
        "MarginL": 50,
        "MarginR": 10,
        "MarginV": 30,
        "Encoding": 1
    },
    "CAUTION": {
        "Name": "CAUTION",
        "Fontname": "Calibri",
        "Fontsize": 200.0,
        "PrimaryColour": "&H0000FFFF",
        "SecondaryColour": "&H0000FFFF",
        "OutlineColour": "&H00000000",
        "BackColour": "&H0000FFFF",
        "Bold": 1,
        "Italic": 0,
        "Underline": 0,
        "StrikeOut": 0,
        "ScaleX": 100.0,
        "ScaleY": 100.0,
        "Spacing": 0,
        "Angle": 0,
        "BorderStyle": 1,
        "Outline": 20.0,
        "Shadow": 0,
        "Alignment": 5,
        "MarginL": 10,
        "MarginR": 10,
        "MarginV": 10,
        "Encoding": 1
    },
    "DELETE": {
        "Name": "DELETE",
        "Fontname": "Calibri",
        "Fontsize": 200.0,
        "PrimaryColour": "&H00FFFFFF",
        "SecondaryColour": "&H00FFFFFF",
        "OutlineColour": "&H00000000",
        "BackColour": "&H00FFFFFF",
        "Bold": 1,
        "Italic": 0,
        "Underline": 0,
        "StrikeOut": 0,
        "ScaleX": 100.0,
        "ScaleY": 100.0,
        "Spacing": 0,
        "Angle": 0,
        "BorderStyle": 1,
        "Outline": 20.0,
        "Shadow": 0,
        "Alignment": 5,
        "MarginL": 10,
        "MarginR": 10,
        "MarginV": 10,
        "Encoding": 1
    },
    "screen_address": {
        "Name": "screen_address",
        "Fontname": "思源黑体 CN",
        "Fontsize": 67.0,
        "PrimaryColour": "&H00FFFFFF",
        "SecondaryColour": "&H00FFFFFF",
        "OutlineColour": "&H00000000",
        "BackColour": "&H00FFFFFF",
        "Bold": 0,
        "Italic": 0,
        "Underline": 0,
        "StrikeOut": 0,
        "ScaleX": 100.0,
        "ScaleY": 100.0,
        "Spacing": 0,
        "Angle": 0,
        "BorderStyle": 1,
        "Outline": 0,
        "Shadow": 0,
        "Alignment": 7,
        "MarginL": 15,
        "MarginR": 15,
        "MarginV": 19,
        "Encoding": 1
    },
    "screen_dialogue": {
        "Name": "screen_dialogue",
        "Fontname": "思源黑体 CN",
        "Fontsize": 67.0,
        "PrimaryColour": "&H00FFFFFF",
        "SecondaryColour": "&H00FFFFFF",
        "OutlineColour": "&H00131314",
        "BackColour": "&H00FFFFFF",
        "Bold": 0,
        "Italic": 0,
        "Underline": 0,
        "StrikeOut": 0,
        "ScaleX": 100.0,
        "ScaleY": 100.0,
        "Spacing": 0,
        "Angle": 0,
        "BorderStyle": 1,
        "Outline": 0,
        "Shadow": 0,
        "Alignment": 7,
        "MarginL": 15,
        "MarginR": 15,
        "MarginV": 19,
        "Encoding": 1
    },
    "address": {
        "Name": "address",
        "Fontname": "思源黑体 CN Bold",
        "Fontsize": 83.0,
        "PrimaryColour": "&H00FFFFFF",
        "SecondaryColour": "&H00FFFFFF",
        "OutlineColour": "&H00000000",
        "BackColour": "&H00FFFFFF",
        "Bold": 0,
        "Italic": 0,
        "Underline": 0,
        "StrikeOut": 0,
        "ScaleX": 100.0,
        "ScaleY": 100.0,
        "Spacing": 0,
        "Angle": 0,
        "BorderStyle": 1,
        "Outline": 0,
        "Shadow": 0,
        "Alignment": 5,
        "MarginL": 15,
        "MarginR": 15,
        "MarginV": 19,
        "Encoding": 1
    }
}
DISPLAY_NAME_STYLE = {
    "ミク": "初音ミク",
    "リン": "鏡音リン",
    "レン": "鏡音レン",
    "ルカ": "巡音ルカ",
    "MEIKO": "MEIKO",
    "KAITO": "KAITO",
    "一歌": "星乃一歌",
    "咲希": "天馬咲希",
    "穂波": "望月穗波",
    "志歩": "日野森志步",
    "みのり": "花里みのり",
    "遥": "桐谷遥",
    "愛莉": "桃井愛莉",
    "雫": "日野森雫",
    "こはね": "小豆沢こはね",
    "杏": "白石杏",
    "彰人": "東雲彰人",
    "冬弥": "青柳冬弥",
    "司": "天馬司",
    "えむ": "鳳えむ",
    "寧々": "草薙寧々",
    "類": "神代類",
    "奏": "宵崎奏",
    "まふゆ": "朝比奈まふゆ",
    "絵名": "東雲絵名",
    "瑞希": "暁山瑞希",
    "ミクの声": "初音ミク",
    "リンの声": "鏡音リン",
    "レンの声": "鏡音レン",
    "ルカの声": "巡音ルカ",
    "MEIKOの声": "MEIKO",
    "KAITOの声": "KAITO",
    "一歌の声": "星乃一歌",
    "咲希の声": "天馬咲希",
    "穂波の声": "望月穗波",
    "志歩の声": "日野森志步",
    "みのりの声": "花里みのり",
    "遥の声": "桐谷遥",
    "愛莉の声": "桃井愛莉",
    "雫の声": "日野森雫",
    "こはねの声": "小豆沢こはね",
    "杏の声": "白石杏",
    "彰人の声": "東雲彰人",
    "冬弥の声": "青柳冬弥",
    "司の声": "天馬司",
    "えむの声": "鳳えむ",
    "寧々の声": "草薙寧々",
    "類の声": "神代類",
    "奏の声": "宵崎奏",
    "まふゆの声": "朝比奈まふゆ",
    "絵名の声": "東雲絵名",
    "瑞希の声": "暁山瑞希",
    "？？？": "関連人物",
    "screen": "screen"
}

characterDict = [
    {"name": "ichika",
     "name_j": "一歌"},
    {"name": "saki",
     "name_j": "咲希"},
    {"name": "honami",
     "name_j": "穂波"},
    {"name": "shiho",
     "name_j": "志歩"},
    {"name": "minori",
     "name_j": "みのり"},
    {"name": "haruka",
     "name_j": "遥"},
    {"name": "airi",
     "name_j": "愛莉"},
    {"name": "shizuku",
     "name_j": "雫"},
    {"name": "kohane",
     "name_j": "こはね"},
    {"name": "an",
     "name_j": "杏"},
    {"name": "akito",
     "name_j": "彰人"},
    {"name": "touya",
     "name_j": "冬弥"},
    {"name": "tsukasa",
     "name_j": "司"},
    {"name": "emu",
     "name_j": "えむ"},
    {"name": "nene",
     "name_j": "寧々"},
    {"name": "rui",
     "name_j": "類"},
    {"name": "kanade",
     "name_j": "奏"},
    {"name": "mafuyu",
     "name_j": "まふゆ"},
    {"name": "ena",
     "name_j": "絵名"},
    {"name": "mizuki",
     "name_j": "瑞希"},
    {"name": "miku",
     "name_j": "ミク"},
    {"name": "rin",
     "name_j": "リン"},
    {"name": "len",
     "name_j": "レン"},
    {"name": "luka",
     "name_j": "ルカ"},
    {"name": "meiko",
     "name_j": "MEIKO"},
    {"name": "kaito",
     "name_j": "KAITO"},
    {"name": "miku_band",
     "name_j": "ミク_LeoN"},
    {"name": "miku_idol",
     "name_j": "ミク_MMJ"},
    {"name": "miku_street",
     "name_j": "ミク_VBS"},
    {"name": "miku_park",
     "name_j": "ミク_WS"},
    {"name": "miku_nothing",
     "name_j": "ミク_25"}
]

areaDict = [
    "",
    u"十字路口",
    u"商业街",
    u"购物中心",
    u"音乐商店",
    u"教室的SEKAI",
    "",
    u"舞台的SEKAI",
    u"街道的SEKAI",
    u"奇幻仙境的SEKAI",
    u"空无一人的SEKAI",
    u"神山高中",
    u"凤凰仙境乐园",
    u"宫益坂女子学园"
]


def get_divider_event(string=None, slash=15):
    return [{
        "Type": "Comment",
        "Layer": 1,
        "Start": "00:00:00.00",
        "End": "00:00:00.00",
        "Style": "screen", "Name": '',
        "MarginL": 0, "MarginR": 0, "MarginV": 0,
        "Effect": '',
        "Text": "-" * slash + f"{(' ' + string + ' ') if string else ''}" + "-" * slash
    }]


asset_path = "asset"
if getattr(sys, 'frozen', False):
    asset_path = os.path.join(sys._MEIPASS, asset_path)

template_menu = cv2.imread(os.path.join(asset_path, "menu.png"), cv2.IMREAD_UNCHANGED)
template_point = cv2.imread(os.path.join(asset_path, "point.png"), cv2.IMREAD_UNCHANGED)
template_place = cv2.imread(os.path.join(asset_path, "place.png"), cv2.IMREAD_UNCHANGED)
