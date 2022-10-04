import os

import cv2
import numpy as np
from tqdm import tqdm


# from tqdm import tqdm


def check_distance(array_1: list | tuple, array_2: list | tuple):
    assert len(array_1) == len(array_2)
    distance = pow(sum(pow((array_1[i] - array_2[i]), 2) for i in range(len(array_1))), 1 / 2)
    return distance


def check_similar_color(image: np.ndarray, color: tuple):
    exist = False
    for array in image:
        for pixel in array:
            distance = check_distance(pixel, color)
            if distance < 25:
                exist = True
                break
    return exist


def check_dark(image: np.ndarray, color: int):
    return True if image.min(initial=None) < color else False


class VideoProcessor:

    def __init__(self, video_path, point_pattern_path):
        self.area_mask = None
        self.frame_gray = None
        self.frame = None
        self.initialed = False
        self.video = None
        self.pointer_size = None
        self.frame_height = None
        self.frame_width = None
        self.constant_point_center = None
        self.pointer = None
        self.frame_count = None
        self.done: bool = False
        self.point_pattern_path: str = point_pattern_path
        self.video_path: str = video_path

    def initial(self):
        assert os.path.exists(self.video_path), "Video Not Exists"
        assert os.path.exists(self.point_pattern_path), "Pattern Not Exists"
        self.video: cv2.VideoCapture = cv2.VideoCapture(self.video_path)
        self.frame_count: int = int(self.video.get(7))
        self.pointer: np.ndarray = self.get_pointer()
        self.pointer_size: int = self.pointer.shape[0]

        self.constant_point_center: tuple[int, int] | None = None
        self.frame_height = int(self.video.get(4))
        self.frame_width = int(self.video.get(3))
        self.check_area_mask()
        self.initialed = True

    def check_area_mask(self):
        from reference import get_area_mask_size, get_area_mask
        mask = get_area_mask_size((self.frame_width, self.frame_height))
        mask_string = [i for i in get_area_mask(mask).split(' ') if i.isdigit()]
        x_a = sorted(map(int, mask_string[::2]))[1:3]
        y_a = sorted(set(map(int, mask_string[1::2])))
        self.area_mask = y_a + x_a

    def get_pointer(self) -> np.ndarray:
        height, width = (self.video.get(4), self.video.get(3))
        if (width / height) > (16 / 9):
            size = int((int((height / 1080) * 136)) * (886 / 136))
        else:
            size = int((width / 1920) * 886)
        template = cv2.imread(self.point_pattern_path, 0)
        i = size / 886
        pointer = cv2.resize(template, (int(template.shape[0] * i), int(template.shape[1] * i)))
        return pointer

    def get_frame_pointer_position(self, frame: np.ndarray):
        height = self.frame_height
        width = self.frame_width
        if self.constant_point_center:
            lft, tp = self.constant_point_center
            border = self.pointer_size * 0.9
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

        res = cv2.matchTemplate(cut, self.pointer, cv2.TM_CCOEFF_NORMED)
        threshold = 0.85

        loc = divmod(np.argmax(res), res.shape[1])
        if res[loc[0], loc[1]] < threshold:
            center = None
        else:
            left_top = (cut_left + loc[1].item(), cut_up + loc[0].item())
            center = (int(left_top[0] + (self.pointer_size / 2)), int(left_top[1] + (self.pointer_size / 2)))
        return center

    def check_frame_dialog_status(self, frame: np.ndarray, center: tuple[int, int] | None):
        point_center = center
        if not point_center:
            return 0
        size = self.pointer_size
        left = int(point_center[0] - size / 2)
        top = int(point_center[1] - size / 2)
        right = int(point_center[0] + size / 2)
        bottom = int(point_center[1] + size / 2)
        top = int(top + 0.9 * size + size)
        bottom = int(bottom + 0.9 * size + size)
        color = 128  # (106, 75, 78)
        cut = frame[top:bottom, left:right]
        first_exist = check_dark(cut, color)
        left = int(left + 0.15 * size + size)
        right = int(right + 0.15 * size + size)
        cut = frame[top:bottom, left:right]
        second_exist = check_dark(cut, color)
        result = int(first_exist + second_exist)
        if result and not self.constant_point_center:
            self.constant_point_center = point_center
        return result

    def check_frame_area_mask(self, frame: np.ndarray):
        cut1 = frame[
               self.area_mask[0]:self.area_mask[0] + self.pointer_size,
               self.area_mask[2]:self.area_mask[2] + self.pointer_size
               ]
        exist = False
        for array in cut1:
            for pixel in array:
                dis = check_distance(pixel, (178, 145, 139))
                if dis < 25:
                    exist = True
                    break
        return exist

    def process(self):

        status_chain = [0]
        point_chain = []
        timestamp_chain = []
        mask_chain = [0]
        result = []
        process = tqdm(range(self.frame_count))
        process.set_description("[Opencv] Progressing")

        for _ in process:
            ret, frame = self.video.read()
            if not ret:
                break
            else:
                current_timestamp = self.video.get(0)
                timestamp_chain.append(current_timestamp)
                gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                center = self.get_frame_pointer_position(gray_frame)
                point_chain.append(center)
                res = self.check_frame_dialog_status(gray_frame, center)
                status_chain.append(res)
                result.append(res)
                sta = int(self.check_frame_area_mask(frame) if not res else False)
                mask_chain.append(sta)
        status_chain.append(0)
        frame_chain = []
        ps = [point_chain[i] for i in range(len(point_chain)) if status_chain[i + 1] == 2]
        constant_point = max(ps, key=ps.count)

        for i in range(len(status_chain) - 2):
            f = Frame(i, status_chain[i:][:3], point_chain, constant_point, timestamp_chain[i], tuple(mask_chain[i-1:i+2]))
            frame_chain.append(f)
        chain = []
        for frame in frame_chain:
            if chain:
                i = chain[-1]
                if frame.is_start_point():
                    i += 1
                elif frame.is_end_point():
                    i -= 1
                chain.append(i)
            else:
                chain.append(1 if frame.is_start_point() else 0)
        return frame_chain


class Frame:
    def __init__(
            self, frame_id: int, status: list[int], points: list[tuple | None], constant_point, timestamp: float,
            mask_status: tuple):
        self.timestamp = timestamp
        self.frame_id = frame_id
        self.point = points[frame_id]
        self.points = points
        self.status = status
        self.constant_point = constant_point
        self.mask_status = mask_status

    def is_area_mask_start(self):
        if self.mask_status[:3] == (0, 1, 1):
            return True
        return False

    def is_area_mask_end(self):
        if self.mask_status[:3] == (1, 1, 0):
            return True
        return False

    def is_constant(self, point=None):
        point = point if point else self.point
        if point:
            if check_distance(point, self.constant_point) <= pow(200, 0.5):
                return True
        return False

    def is_start_point(self):
        if self.status[1] == 1 and self.is_constant():
            if self.status[0] == 0:
                return True
            elif self.status[0] == 2:
                return True
        return False

    def is_end_point(self):
        if self.status[1] == 2:
            if self.status[2] == 0:
                return True
            elif self.status[2] == 1:
                return True
            else:
                if self.is_constant() and not self.is_constant(self.points[self.frame_id + 1]):
                    return True
        return False

    def is_mask_start_point(self):
        if self.status[1] == 1:
            if self.status[0] == 0:
                return True
        return False

    def is_mask_end_point(self):
        if self.status[1] == 2:
            if self.status[2] == 0:
                return True
        return False
