import cv2
from config import MOTION_THRESHOLD, MIN_CONTOUR_AREA


class MotionDetector:
    def __init__(self):
        self.previous_frame = None

    def detect_motion(self, current_frame):

        if self.previous_frame is None:
            self.previous_frame = current_frame.copy()
            return False, [], None

        frame_difference = cv2.absdiff(
            self.previous_frame,
            current_frame
        )

        _, threshold_frame = cv2.threshold(
            frame_difference,
            MOTION_THRESHOLD,
            255,
            cv2.THRESH_BINARY
        )

        threshold_frame = cv2.dilate(
            threshold_frame,
            None,
            iterations=2
        )

        contours, _ = cv2.findContours(
            threshold_frame,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE
        )

        motion_contours = []

        for contour in contours:

            if cv2.contourArea(contour) >= MIN_CONTOUR_AREA:
                motion_contours.append(contour)

        self.previous_frame = current_frame.copy()

        motion_found = len(motion_contours) > 0

        return (
            motion_found,
            motion_contours,
            threshold_frame
        )
    