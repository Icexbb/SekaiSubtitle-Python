import cv2
import loguru
import numpy


def find_dialog(target: numpy.ndarray):
    sign = cv2.imread('./img/auto_sign.png')
    sign_width = sign.shape[1]
    sign_height = sign.shape[0]
    # target = target[target.shape[1] - 200:target.shape[1], target.shape[0] - 400:target.shape[0]]
    # target = cv2.cvtColor(target, cv2.COLOR_BGR2GRAY)

    res = cv2.matchTemplate(target, sign, cv2.TM_SQDIFF_NORMED)
    cv2.normalize(res, res, 0, 1, cv2.NORM_MINMAX, -1)

    # min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    loc = numpy.where(res > 0.01)

    for res_point in zip(*loc[::-1]):
        cv2.rectangle(target, res_point, (res_point[0] + sign_width, res_point[1] + sign_height), (0, 0, 255))
    target = cv2.resize(target, None, fx=0.5, fy=0.5)
    cv2.imshow('res', target)
    cv2.waitKey(0)


if __name__ == "__main__":
    find_dialog(cv2.imread('./img/32-21_1.png'))
