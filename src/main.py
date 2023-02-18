# -*- coding: utf-8 -*-
import argparse
import sys

from gui.main import start_gui
from lib.process import SekaiJsonVideoProcess


def parse_args():
    argv = sys.argv[1:]

    parser = argparse.ArgumentParser(description='使用命令行方式选择文件进行自动化打轴')
    parser.add_argument("--video_file", "-v", type=str, help="视频文件")
    parser.add_argument("--json_file", "-j", type=str, help="json文件")
    parser.add_argument("--translate_file", "-t", type=str, help="翻译文件(Sekai Text 格式)")
    parser.add_argument("--output_file", "-o", type=str, help="输出字幕文件位置")
    parser.add_argument("--overwrite", "-f", action="store_true", help="覆盖")
    parser.add_argument("--nogui", action="store_true", help="命令行模式")

    ns = parser.parse_args(argv)
    return ns


def main():
    # if "nogui" in sys.argv:
    args = parse_args()
    if args.nogui:
        process = SekaiJsonVideoProcess(
            args.video_file, args.json_file, args.translate_file, args.output_file, None, args.overwrite)
        process.run()
    else:
        start_gui()


if __name__ == '__main__':
    main()
