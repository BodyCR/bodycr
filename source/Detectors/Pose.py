import cv2
import mediapipe as mp
from ..Modules.Utils import Point
from ..Detectors.landmarks import pose as PoseLandmarks

class PoseDetector:
    """
        ## BodyCR Detector
        ### The detector class to pose capture
        #### `bodycr.source.Detectors.Pose`

        ---------------

        ## Methods:
        1. `def __init__(...)` - Construct this class
        2. `def Read(...)` - Read the passed image and process it
    """

    def __init__(self,
               static_image_mode=False,
               model_complexity=1,
               smooth_landmarks=True,
               enable_segmentation=False,
               smooth_segmentation=True,
               min_detection_confidence=0.5,
               min_tracking_confidence=0.5):
        self.mp_pose = mp.solutions.pose
        self.pose = self.mp_pose.Pose(
               static_image_mode=static_image_mode,
               model_complexity=model_complexity,
               smooth_landmarks=smooth_landmarks,
               enable_segmentation=enable_segmentation,
               smooth_segmentation=smooth_segmentation,
               min_detection_confidence=min_detection_confidence,
               min_tracking_confidence=min_tracking_confidence)

    def Read(self, img):
        processResult = self.pose.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        result = processResult.pose_landmarks
        
        h, w, _ = img.shape

        pose = []

        try:
            pose = [Point(m.x * w, m.y * h) for m in result.landmark]
        except:
            pass

        return pose