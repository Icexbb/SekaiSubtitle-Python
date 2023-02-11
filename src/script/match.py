from typing import List

import cv2
import numpy as np

from lib.data import menu as template_menu
from lib.data import point as template_point
from lib.reference import get_area_mask_size, get_area_mask
from script.tools import check_aberration, check_dark


def get_resized_dialog_pointer(h, w) -> np.ndarray:
    size = int((int((h / 1080) * 136)) * (886 / 136)) if (w / h) > (16 / 9) else int((w / 1920) * 886)
    i = size / 886
    template = template_point
    template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    pointer = cv2.resize(template, (int(template.shape[0] * i), int(template.shape[1] * i)))
    return pointer


def get_resized_interface_menu(h, w) -> np.ndarray:
    size = int((int((h / 1080) * 136)) * (886 / 136)) if (w / h) > (16 / 9) else int((w / 1920) * 886)
    i = size / 886
    template = template_menu
    template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    menu = cv2.resize(template, (int(template.shape[0] * i), int(template.shape[1] * i)))
    return menu


def get_square_mask_area(h, w) -> list[int]:
    mask = get_area_mask_size((w, h))
    mask_string = [i for i in get_area_mask(mask).split(' ') if i.isdigit()]
    x_a = sorted(map(int, mask_string[::2]))[1:3]
    y_a = sorted(set(map(int, mask_string[1::2])))
    return y_a + x_a


def check_frame_pointer_position(
        frame: np.ndarray, pointer: np.ndarray, last_pc: list[int, int] = None) -> None | list[int, int]:
    height = frame.shape[0]  # self.frame_height
    width = frame.shape[1]
    pointer_size = pointer.shape[0]
    if last_pc:
        lft, tp = last_pc
        border = pointer_size * 0.9
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

    res = cv2.matchTemplate(cut, pointer, cv2.TM_CCOEFF_NORMED)
    threshold = 0.85

    loc = divmod(np.argmax(res), res.shape[1])
    if res[loc[0], loc[1]] < threshold:
        center = None
    else:
        left_top = (cut_left + loc[1].item(), cut_up + loc[0].item())
        center = (int(left_top[0] + (pointer_size / 2)), int(left_top[1] + (pointer_size / 2)))
    return center


def check_frame_dialog_status(frame: np.ndarray, pointer: np.ndarray, point_center: tuple[int, int] | None):
    if not point_center:
        return 0
    pointer_size = pointer.shape[0]
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

    return result


def check_frame_area_mask(frame: np.ndarray, area_mask: List[int], content_started: bool = False):
    if not content_started:
        start = check_frame_content_start(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY),
                                          get_resized_interface_menu(frame.shape[1], frame.shape[0]))
        if not start:
            return False
    check_size_y = abs(int((area_mask[1] - area_mask[0]) / 3))
    check_size_x = abs(int((area_mask[2] - area_mask[3]) / 2))
    cut1 = frame[
           area_mask[0]:area_mask[0] + check_size_y,
           area_mask[2]:area_mask[2] + check_size_x,
           ]

    area_purple = [141, 137, 171]
    area_purple.reverse()
    num = check_size_y * check_size_x
    exist = 0
    if max([(cut1[:, :, i]).var() for i in range(cut1.shape[2])]) < 100:
        for array in cut1:
            for pixel in array:
                dis = check_aberration(pixel, area_purple)
                if dis < 15:
                    exist += 1
    res = True if exist > num * 0.90 else False
    return res


def check_frame_content_start(frame: np.ndarray, menu_sign: np.ndarray) -> bool:
    menu_height: int = menu_sign.shape[1]
    menu_width: int = menu_sign.shape[0]
    cut_down = int(3 * menu_height)
    cut_left = -1 * int(3 * menu_width)
    cut = frame[:cut_down, cut_left:]
    res = cv2.matchTemplate(cut, menu_sign, cv2.TM_CCOEFF_NORMED)
    threshold = 0.70

    loc = divmod(np.argmax(res), res.shape[1])
    exist = (not (res[loc[0], loc[1]] < threshold))
    return exist
