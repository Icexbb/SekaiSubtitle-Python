import datetime


def timedelta_to_string(time: datetime.timedelta):
    ms = f"{time.microseconds // 10000:02d}"
    s = f"{time.seconds % 60:02d}"
    m = f"{time.seconds % 3600 // 60:02d}"
    h = f"{time.seconds // 3600:01d}"
    return f"{h}:{m}:{s}.{ms}"


def check_distance(array_1: list | tuple, array_2: list | tuple):
    assert len(array_1) == len(array_2)
    distance = pow(sum(pow((array_1[i] - array_2[i]), 2) for i in range(len(array_1))), 1 / 2)
    return distance
