import cv2

def preprocess_frame(frame):
    """
    Prepare a webcam frame for motion detection.

    The frame is converted to grayscale and blurred
    to reduce unnecessary image noise.
    """
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred_frame = cv2.GaussianBlur(gray_frame, (21, 21), 0)
    return blurred_frame
