import cv2


class Dialog:
    def __init__(self):
        self.start = None
        self.end = None
        self.speaker: str = ""
        self.sentence: str = ""


class Paragraph:
    def __init__(self):
        self.start = None
        self.end = None
        self.dialog: list[Dialog] = []


class Video:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.cv = cv2.VideoCapture(self.file_path)
        self.frame_count: int = self.cv.get(7)
        self.frame_height: int = self.cv.get(4)
        self.frame_width: int = self.cv.get(3)
        self.paragraphs: list[Paragraph] = []
