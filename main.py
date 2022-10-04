import time

from reference import get_point_center, get_dialog_mask, get_area_mask
from video_process import VideoProcessor

if __name__ == "__main__":
    t1 = time.time()
    v = VideoProcessor(r"./video/test.mp4", r"asset/point.png")
    v.initial()
    print(f"[Video] Total_frame: {v.frame_count} Start Process")
    frames = v.process()
    t2 = time.time()
    print(f"[Finish] Use Time: {t2 - t1:.2f}s")
    start_keyframes = [frame.frame_id for frame in frames if frame.is_start_point()]
    end_keyframes = [frame.frame_id for frame in frames if frame.is_end_point()]
    str_len = len((str(v.frame_count)))
    if len(start_keyframes) == len(end_keyframes):
        for i in range(len(start_keyframes)):
            print(
                f"[Result] Line {i + 1}: Frame {start_keyframes[i]:{str_len}} -> Frame {end_keyframes[i]:{str_len}}")
    else:
        print(f"Run Error")
    mask_start_keyframes = [frame.frame_id for frame in frames if frame.is_mask_start_point()]
    mask_end_keyframes = [frame.frame_id for frame in frames if frame.is_mask_end_point()]
    if len(mask_start_keyframes) == len(mask_end_keyframes):
        for i in range(len(mask_end_keyframes)):
            print(
                f"[Result] Mask {i + 1}: "
                f"Frame {mask_start_keyframes[i]:{str_len}} -> Frame {mask_end_keyframes[i]:{str_len}}")
    else:
        print(f"Run Error")
    area_mask_start_keyframes = [frame.frame_id for frame in frames if frame.is_area_mask_start()]
    area_mask_end_keyframes = [frame.frame_id for frame in frames if frame.is_area_mask_end()]
    if len(area_mask_end_keyframes) == len(area_mask_start_keyframes):
        for i in range(len(area_mask_end_keyframes)):
            print(
                f"[Result] Area Mask {i + 1}: "
                f"Frame {area_mask_start_keyframes[i]:{str_len}} -> Frame {area_mask_end_keyframes[i]:{str_len}}")
    else:
        print(f"Run Error")
    print(v.constant_point_center)
    print(v.pointer_size)
    screen_data = get_point_center((v.frame_width, v.frame_height), v.constant_point_center)
    pattern_coefficient = screen_data['pattern_coefficient']
    dialog_mask = get_dialog_mask(screen_data)
    area_mask = get_area_mask(screen_data)
    print(f"[Result] Dialog Mask: {dialog_mask}")
    print(f"[Result] Area Banner Mask:{area_mask}")
