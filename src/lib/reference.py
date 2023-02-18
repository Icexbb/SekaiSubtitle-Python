# -*- coding: utf-8 -*-
from lib.subtitle import AssDraw


def get_area_mask_size(frame_shape: tuple):
    height = frame_shape[1]
    width = frame_shape[0]
    area_mask_size = [0, 0]
    if (width / height) > (16 / 9):
        area_mask_size[1] = int((height / 1080) * 136)
        area_mask_size[0] = int(area_mask_size[1] * (886 / 136))
    else:
        area_mask_size[0] = int((width / 1920) * 886)
        area_mask_size[1] = int(area_mask_size[0] * (136 / 886))
    area_mask_area = [
        width / 2 - area_mask_size[0] / 2,
        height / 2 - area_mask_size[1] / 2,
        width / 2 + area_mask_size[0] / 2,
        height / 2 + area_mask_size[1] / 2
    ]
    return {
        'area_mask_size': area_mask_size,
        'area_mask_coefficient': area_mask_size[0] / 886,
        'area_mask_area': area_mask_area
    }


def get_pattern_size(frame_shape: tuple):
    height = frame_shape[1]
    width = frame_shape[0]
    pattern_size = [0, 0]
    if (width / height) > (16 / 9):
        pattern_size[1] = int((height / 1080) * 317)
        pattern_size[0] = int(pattern_size[1] * (1612 / 317))
    else:
        pattern_size[0] = int((width / 1920) * 1612)
        pattern_size[1] = int(pattern_size[0] * (317 / 1612))
    return {
        'pattern_size': pattern_size,
        'pattern_coefficient': pattern_size[0] / 1612
    }


def get_frame_data(frame_shape: tuple, point_center: tuple | list) -> dict:
    height = frame_shape[1]
    width = frame_shape[0]

    dialog_size = get_pattern_size(frame_shape)
    area_mask_size = get_area_mask_size(frame_shape)
    dialog_coefficient = dialog_size['pattern_coefficient']

    start_point = [point_center[0] - 110 * dialog_coefficient,
                   point_center[1] - 42 * dialog_coefficient]
    pattern_area = start_point + [start_point[0] + dialog_size['pattern_size'][0],
                                  start_point[1] + dialog_size['pattern_size'][1]]
    area_mask_area = [
        width / 2 - area_mask_size['area_mask_size'][0] / 2,
        height / 2 - area_mask_size['area_mask_size'][1] / 2,
        width / 2 + area_mask_size['area_mask_size'][0] / 2,
        height / 2 + area_mask_size['area_mask_size'][1] / 2
    ]
    return {
        'pattern_size': dialog_size['pattern_size'],
        'pattern_coefficient': dialog_size['pattern_coefficient'],

        'pattern_area': pattern_area,
        'pattern_center': [(pattern_area[0] + pattern_area[2]) / 2,
                           (pattern_area[1] + pattern_area[3]) / 2],

        'area_mask_size': area_mask_size['area_mask_size'],
        'area_mask_coefficient': area_mask_size['area_mask_coefficient'],

        'area_mask_center': list(map(lambda x: int(x / 2), frame_shape)),
        'area_mask_area': area_mask_area
    }


def get_dialog_mask(screen_data: dict, move: list[int, int] = None) -> str:
    origin_mask = 'm 232 785 ' \
                  'b 232 785 232 785 232 785 ' \
                  'b 137 836 137 964 232 1015 ' \
                  'b 244 1021 259 1025 272 1027 ' \
                  'l 1646 1027 ' \
                  'l 1687 1015 ' \
                  'b 1783 964 1783 836 1687 785 ' \
                  'l 1645 772 ' \
                  'l 889 772 ' \
                  'b 889 786 874 797 860 797 ' \
                  'l 254 798 ' \
                  'b 249 798 232 791 232 785'
    mask = AssDraw(origin_mask)
    mask.move([-154, -717])
    if move:
        mask.move(move)
    mask.scale(screen_data['pattern_coefficient'])
    mask.move(screen_data['pattern_area'][:2])
    return r"{\p1\pos(0,0)\c&HFFFFFF&}" + mask.string()


def get_area_mask(screen_data: dict) -> str:
    origin_mask = 'm 566 472 ' \
                  'l 517 608 ' \
                  'l 1354 608 ' \
                  'l 1403 472'
    mask = AssDraw(origin_mask)
    mask.move([-517, -472])
    mask.scale(screen_data['area_mask_coefficient'])
    mask.move(screen_data['area_mask_area'][:2])
    return r"{\an7\p1\c&HB68B89&\pos(0,0)\fad(100,100)}" + mask.string()
