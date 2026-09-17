from datetime import datetime

class ActivityLogger:
    def __init__(self, filename="activity_log.txt"):
        self.filename = filename

    def save_session(
        self,
        duration,
        motion_events,
        frames_with_motion
    ):

        current_time = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        with open(self.filename, "a") as log_file:

            log_file.write(
                "\n------------------------------------------\n"
            )

            log_file.write(
                "Motion Detection Session\n"
            )

            log_file.write(
                f"Date and Time: {current_time}\n"
            )

            log_file.write(
                f"Session Duration: {duration:.2f} seconds\n"
            )

            log_file.write(
                f"Motion Events: {motion_events}\n"
            )

            log_file.write(
                f"Frames With Motion: {frames_with_motion}\n"
            )
            