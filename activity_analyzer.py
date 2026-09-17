class ActivityAnalyzer:
    def __init__(self):
        self.motion_events = 0
        self.frames_with_motion = 0
        self.previous_motion = False

    def analyze(self, motion_contours):

        motion_found = len(motion_contours) > 0

        if motion_found:
            self.frames_with_motion += 1

        if motion_found and not self.previous_motion:
            self.motion_events += 1

        self.previous_motion = motion_found

        if motion_found:
            status = "MOTION DETECTED"
        else:
            status = "NO MOTION"

        return {
            "status": status,
            "motion_regions": len(motion_contours),
            "motion_events": self.motion_events,
            "frames_with_motion": self.frames_with_motion
        }
    