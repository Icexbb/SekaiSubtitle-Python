from video_process import Frame


class TalkEvent:
    def __init__(self, frames: list[Frame]):
        self.frames = frames
        self.start = self.frames[0].timestamp
        self.end = self.frames[-1].timestamp
