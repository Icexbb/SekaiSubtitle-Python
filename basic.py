import cv2
import numpy as np


def resize(target: np.ndarray, scale_percent: int):
    width = int(target.shape[1] * scale_percent / 100)
    height = int(target.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized = cv2.resize(target, dim)
    return resized
