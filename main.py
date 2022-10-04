import argparse
import os
import time

from lib.json_process import Episode
from lib.reference import get_point_center
from lib.video_process import VideoProcessor


def process(video: str, json: str, output: str = None):
    if output:
        output += ".ass" if not output.lower().endswith(".ass") else ""
    output = os.path.realpath(output or os.path.splitext(video)[0] + ".ass")
    # ===== Analyze Video =====

    v = VideoProcessor(video)
    v.initial()

    print(f"[Video] Total frame: {v.frame_count} Video length:{v.second_count}s")
    t1 = time.time()
    frames = v.process()
    t2 = time.time()
    print(f"[Finish] Use Time: {t2 - t1:.2f}s Process Rate:{v.second_count / (t2 - t1):.2f}")

    screen_data = get_point_center((v.frame_width, v.frame_height), v.constant_point_center)

    # ===== Generate Subtitle =====
    episode = Episode(
        video, json, output,
        frames, screen_data, v.constant_point_center, v.pointer_size,
        (v.frame_width, v.frame_height)
    )
    episode.save_ass()


parser = argparse.ArgumentParser(usage='%(prog)s [options]')
parser.add_argument("-v", "--video", help="视频文件地址")
parser.add_argument("-j", "--json", help="剧情数据文件地址")
parser.add_argument("-o", "--output", help="输出文件地址")

if __name__ == "__main__":
    args = parser.parse_args()
    video_path = args.video
    json_path = args.json
    if not video_path or not json_path:
        parser.print_help()
        exit(1)
    output_path = args.output
    process(video_path, json_path,output_path)
