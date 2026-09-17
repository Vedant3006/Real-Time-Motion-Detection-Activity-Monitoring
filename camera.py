import cv2
from config import CAMERA_ID

class Camera:
    def __init__(self):
        self.camera = cv2.VideoCapture(CAMERA_ID)

    def is_opened(self):
        return self.camera.isOpened()

    def read_frame(self):
        success, frame = self.camera.read()
        return success, frame

    def release(self):
        self.camera.release()


        