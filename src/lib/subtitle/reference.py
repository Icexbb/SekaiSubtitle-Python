from typing import Union


def get_area_mask_size(frame_shape: tuple):
    height = frame_shape[1]
    width = frame_shape[0]
    size = [0, 0]
    if (width / height) > (16 / 9):
        size[1] = int((height / 1080) * 136)
        size[0] = int(size[1] * (886 / 136))
    else:
        size[0] = int((width / 1920) * 886)
        size[1] = int(size[0] * (136 / 886))
    area_mask_area = [
        width / 2 - size[0] / 2,
        height / 2 - size[1] / 2,
        width / 2 + size[0] / 2,
        height / 2 + size[1] / 2
    ]
    return {
        'area_mask_size': size,
        'area_mask_coefficient': size[0] / 886,
        'area_mask_area': area_mask_area
    }


def get_pattern_size(frame_shape: tuple):
    height = frame_shape[1]
    width = frame_shape[0]
    size = [0, 0]
    if (width / height) > (16 / 9):
        size[1] = int((height / 1080) * 317)
        size[0] = int(size[1] * (1612 / 317))
    else:
        size[0] = int((width / 1920) * 1612)
        size[1] = int(size[0] * (317 / 1612))
    return {
        'pattern_size': size,
        'pattern_coefficient': size[0] / 1612
    }


def get_point_center(frame_shape: tuple, point_center: tuple) -> dict:
    # target = cv2.imread(img)
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


class TextBox:
    def __init__(self, area: list[int, int, int, int]):
        self.left = area[0]
        self.right = area[1]
        self.upper = area[2]
        self.lower = area[3]
        self.length = self.right - self.left
        self.height = self.lower - self.upper
        self.center = [(self.left + self.right) / 2, (self.upper + self.lower) / 2]

    @property
    def string(self):
        return f'{int(self.center[0] - self.length / 2)} {int(self.center[0] + self.length / 2)} ' \
               f'{int(self.center[1] - self.height / 2)} {int(self.center[1] + self.height / 2)}'

    def move(self, offset: list[int, int]):
        self.center[0] = int(self.center[0] + offset[0])
        self.center[1] = int(self.center[1] + offset[1])

    def scale(self, coefficient: list[float, float]):
        self.length = int(self.length * coefficient[0])
        self.height = int(self.height * coefficient[1])

    def move_to(self, point: list[int, int]):
        offset = [
            int(point[0] - self.center[0]),
            int(point[1] - self.center[1]),
        ]
        self.move(offset)
