import cv2
import time

from config import WINDOW_NAME
from camera import Camera
from preprocessing import preprocess_frame
from motion_detector import MotionDetector
from activity_analyzer import ActivityAnalyzer
from logger import ActivityLogger


def merge_nearby_contours(contours, distance=30):

    if not contours:
        return []

    boxes = []

    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        boxes.append([x, y, w, h])

    merged = True

    while merged:

        merged = False
        new_boxes = []

        while boxes:

            current = boxes.pop(0)
            x1, y1, w1, h1 = current

            changed = True

            while changed:

                changed = False

                for i, box in enumerate(boxes):

                    x2, y2, w2, h2 = box

                    close_x = (
                        x2 <= x1 + w1 + distance
                        and x2 + w2 >= x1 - distance
                    )

                    close_y = (
                        y2 <= y1 + h1 + distance
                        and y2 + h2 >= y1 - distance
                    )

                    if close_x and close_y:

                        new_x = min(x1, x2)
                        new_y = min(y1, y2)

                        new_right = max(
                            x1 + w1,
                            x2 + w2
                        )

                        new_bottom = max(
                            y1 + h1,
                            y2 + h2
                        )

                        x1 = new_x
                        y1 = new_y
                        w1 = new_right - new_x
                        h1 = new_bottom - new_y

                        boxes.pop(i)

                        changed = True
                        merged = True
                        break

            new_boxes.append(
                [x1, y1, w1, h1]
            )

        boxes = new_boxes

    return boxes


def main():

    camera = Camera()
    detector = MotionDetector()
    analyzer = ActivityAnalyzer()
    logger = ActivityLogger()

    if not camera.is_opened():
        print("Error: Camera could not be opened.")
        return

    start_time = time.time()

    # Keep the last detected boxes visible briefly
    last_boxes = []
    last_motion_time = 0

    DISPLAY_HOLD_TIME = 0.3

    print("Real-Time Motion Detection started.")
    print("Press Q to exit.")

    while True:

        success, frame = camera.read_frame()

        if not success:
            break

        # Mirror the camera
        frame = cv2.flip(frame, 1)

        # Preprocess frame
        processed = preprocess_frame(frame)

        # Detect motion
        motion_found, contours, threshold = (
            detector.detect_motion(processed)
        )

        # Analyze activity
        activity = analyzer.analyze(contours)

        # Merge nearby motion regions
        current_boxes = merge_nearby_contours(
            contours,
            distance=30
        )

        # Save latest motion boxes
        if motion_found:

            last_boxes = current_boxes
            last_motion_time = time.time()

        # Keep boxes visible briefly
        if time.time() - last_motion_time <= DISPLAY_HOLD_TIME:
            display_boxes = last_boxes
        else:
            display_boxes = []

        # Draw bounding boxes
        for x, y, w, h in display_boxes:

            # Center coordinates
            center_x = x + w // 2
            center_y = y + h // 2

            # Motion area
            area = w * h

            # Bounding box
            cv2.rectangle(
                frame,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                2
            )

            # Center point
            cv2.circle(
                frame,
                (center_x, center_y),
                4,
                (0, 0, 255),
                -1
            )

            # Position
            cv2.putText(
                frame,
                f"Position: ({center_x}, {center_y})",
                (x, y + h + 20),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (255, 255, 255),
                1
            )

            # Area
            cv2.putText(
                frame,
                f"Area: {area} px",
                (x, y + h + 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (255, 255, 255),
                1
            )

        # Motion status
        cv2.putText(
            frame,
            activity["status"],
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0) if motion_found else (255, 255, 255),
            2
        )

        # Motion events
        cv2.putText(
            frame,
            f"Motion Events: {activity['motion_events']}",
            (20, 75),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (255, 255, 255),
            2
        )

        # Session time
        duration = time.time() - start_time

        cv2.putText(
            frame,
            f"Time: {duration:.1f}s",
            (20, 110),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (255, 255, 255),
            2
        )

        # Display frame
        cv2.imshow(
            WINDOW_NAME,
            frame
        )

        # Press Q to exit
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # Save session information
    duration = time.time() - start_time

    logger.save_session(
        duration,
        analyzer.motion_events,
        analyzer.frames_with_motion
    )

    camera.release()
    cv2.destroyAllWindows()

    print("\nSession completed.")
    print("Activity saved to activity_log.txt")


if __name__ == "__main__":
    main()
    