from lib.process import SekaiJsonVideoProcess


def run(video_file: str):
    processor = SekaiJsonVideoProcess(video_file)
    processor.run()
