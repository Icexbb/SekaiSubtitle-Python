# -*- coding: utf-8 -*-
import datetime
import json
import os

import numpy as np


def read_json(path, alt=None):
    if alt is None:
        alt = {}

    if os.path.exists(path):
        try:
            data = json.load(open(path, 'r', encoding="utf8"))
        except:
            data = alt
        return data
    else:
        return alt


def save_json(path, data):
    return json.dump(data, open(path, 'w', encoding="utf8"), ensure_ascii=False, indent=4)


def merge_dict(*args):
    res = {}
    for data in args:
        data: dict
        for key, value in data.items():
            key: str
            if key.startswith("m_"):
                continue
            if key in res.keys():
                try:
                    res[key] += value
                except:
                    pass
            else:
                res[key] = value
    return res


def timedelta_to_string(time: datetime.timedelta):
    ms = f"{time.microseconds // 10000:02d}"
    s = f"{time.seconds % 60:02d}"
    m = f"{time.seconds % 3600 // 60:02d}"
    h = f"{time.seconds // 3600:01d}"
    return f"{h}:{m}:{s}.{ms}"


def timedelta_to_string_short(time: datetime.timedelta):
    ms = f"{time.microseconds // 10000:02d}"
    s = f"{time.seconds % 60:02d}"
    m = f"{time.seconds % 3600 // 60:02d}"
    h = f"{time.seconds // 3600:01d}"
    if int(h):
        return f"{h}:{m}:{s}.{ms}"
    elif int(m):
        return f"{m}:{s}.{ms}"
    else:
        return f"{s}.{ms}"


def check_distance(array_1: list | tuple, array_2: list | tuple):
    """
    获得两个向量的距离
    :param array_1: 向量1
    :param array_2: 向量2 长度需要和向量1一致
    :return: 距离
    """
    assert len(array_1) == len(array_2), "Array Length Not Same"
    distance = pow(sum(pow((array_1[i] - array_2[i]), 2) for i in range(len(array_1))), 1 / 2)
    return distance


def check_img_aberration(img: np.ndarray, target: np.ndarray):
    p = (np.abs(img - target)).reshape((img.shape[0] * img.shape[1], 3))
    return sum([x < 18 for x in p.max(axis=1)]) > (img.shape[0] * img.shape[1] * 0.9)


def check_dark(image: np.ndarray, color: int):
    return True if image.min(initial=None) < color else False


def dec_to_ass_hex(num: int):
    return f"&H{(hex(num)[2:]).upper()}&"
