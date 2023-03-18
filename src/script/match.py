# -*- coding: utf-8 -*-
from typing import List

import cv2
import numpy as np

from script.data import template_menu, template_point, template_place
from script.reference import get_area_mask_size, get_area_banner_mask
from script.tools import check_dark, check_img_aberration


def __scaling_ratio(h: int, w: int) -> float:
    size = int((int((h / 1080) * 136)) * (886 / 136)) if (w / h) > (16 / 9) else int((w / 1920) * 886)
    i = size / 886
    return i


def get_resized_dialog_pointer(h, w) -> np.ndarray:
    i = __scaling_ratio(h, w)
    template = cv2.cvtColor(template_point, cv2.COLOR_BGR2GRAY)
    pointer = cv2.resize(template, (int(template.shape[0] * i), int(template.shape[1] * i)))
    return pointer


def get_resized_interface_menu(h, w) -> np.ndarray:
    i = __scaling_ratio(h, w)
    template = cv2.cvtColor(template_menu, cv2.COLOR_BGR2GRAY)
    menu = cv2.resize(template, (int(template.shape[0] * i), int(template.shape[1] * i)))
    return menu


def get_resized_area_tag(h, w) -> np.ndarray:
    i = __scaling_ratio(h, w)
    place_frame = cv2.resize(
        template_place, (int(template_place.shape[1] * i), int(template_place.shape[0] * i)),
        interpolation=cv2.INTER_AREA)
    return place_frame


def get_square_mask_area(h, w) -> list[int]:
    mask = get_area_mask_size((w, h))
    mask_string = [i for i in get_area_banner_mask(mask).split(' ') if i.isdigit()]
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
        cut_down = int(height * 0.85)
        cut_left = int(width * 0)
        cut_right = int(width * 0.3)
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


def check_frame_area_mask(frame: np.ndarray, area_mask: List[int]):
    check_size_y = abs(int((area_mask[1] - area_mask[0]) / 3))
    check_size_x = abs(int((area_mask[2] - area_mask[3]) / 2))
    cut1: np.ndarray = frame[area_mask[0]:area_mask[0] + check_size_y, area_mask[2]:area_mask[2] + check_size_x]
    area_purple = [141, 137, 171]
    area_purple.reverse()

    return check_img_aberration(cut1, np.array(area_purple))


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


def check_area_tag_position(frame: np.ndarray, tag_pattern: np.ndarray, content_started=True) -> tuple[int] | None:
    if not content_started:
        return None
    cut = frame[:int(frame.shape[0] / 8), :int(frame.shape[1] / 3)]
    res = cv2.matchTemplate(cut, tag_pattern, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = divmod(np.argmax(res), res.shape[1])
    if res[loc[0], loc[1]] < threshold:
        return None
    else:
        left_top = (loc[1].item(), loc[0].item())
        return tuple([int(left_top[0] + tag_pattern.shape[1]), int(left_top[1] + tag_pattern.shape[1] / 2)])
