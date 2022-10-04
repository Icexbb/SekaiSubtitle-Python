import datetime

import cv2
import numpy as np


def resize(target: np.ndarray, scale_percent: int):
    width = int(target.shape[1] * scale_percent / 100)
    height = int(target.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized = cv2.resize(target, dim)
    return resized


def timedelta_to_string(time: datetime.timedelta):
    ms = f"{time.microseconds // 10000:02d}"
    s = f"{time.seconds % 60:02d}"
    m = f"{time.seconds % 3600 // 60:02d}"
    h = f"{time.seconds // 3600:01d}"
    return f"{h}:{m}:{s}.{ms}"
