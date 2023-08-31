"""
    # BodyCR 
    ### Body Capture Recognition
    ### Holistic Capture
    #### An simple way to recognize poses, hands and face using Mediapipe and OpenCV, totalizing 532 landmarks recognizing in real-time

    ----------

    By convention, use cr instead of BodyCR, follow the good practice of use `import BodyCR as cr`.
    By convention, import from instead BodyCR.Modules, follow the good practice of use `from BodyCR.Modules import <Required modules>`. Or import directly of BodyCR main module

    Note: Use separate modules can be a pretty difficult, we recommend use the instead main module subdivision. You can import all submodules since Detector to Modules with an easy way, more simple than write this: `import BodyCR as cr`
"""

import mediapipe as mp
import cv2
import time
from ..Detectors.Hand import Hand
from ..Modules.Utils import Point
from ..Modules.Mathb import Mathb

from ..Detectors.Pose import PoseLandmarks
from ..Detectors.Hand import HandLandmarks
from ..Detectors.Face import FaceMeshLandmarks

class HolisticDetector:
    """
        ## BodyCR Detector
        ### The detector class to holistic capture
        #### `bodycr.source.Detectors.Holistic`

        ---------------

        ## Methods:
        1. `def __init__(...)` - Construct this class
        2. `def Read(...)` - Read the passed image and process it
    """

    pose = []
    face = []
    hands = {
        "left": Hand.irreal(),
        "right": Hand.irreal(),
    }

    def __init__(self,
               static_image_mode=False,
               model_complexity=1,
               smooth_landmarks=True,
               enable_segmentation=False,
               smooth_segmentation=True,
               refine_face_landmarks=False,
               min_detection_confidence=0.5,
               min_tracking_confidence=0.5):
        self.mp_holistic = mp.solutions.holistic
        self.holistic = self.mp_holistic.Holistic(
            static_image_mode=static_image_mode,
            model_complexity=model_complexity,
            smooth_landmarks=smooth_landmarks,
            enable_segmentation=enable_segmentation,
            smooth_segmentation=smooth_segmentation,
            refine_face_landmarks=refine_face_landmarks,
            min_detection_confidence=min_detection_confidence,
            min_tracking_confidence=min_tracking_confidence)

    def Read(self, img):
        processResult = self.holistic.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

        height, width, _ = img.shape

        if processResult.pose_landmarks:
            self.pose = [Point(l.x * width, l.y * height) for l in processResult.pose_landmarks.landmark]

        if processResult.face_landmarks:
            self.face = [Point(l.x * width, l.y * height) for l in processResult.face_landmarks.landmark]

        if processResult.left_hand_landmarks:
            left_landmarks = [Point(l.x * width, l.y * height) for l in processResult.left_hand_landmarks.landmark]

            (left_x, left_y) = Mathb.GetBarycenter(
                left_landmarks[0],
                left_landmarks[1],
                left_landmarks[5],
                left_landmarks[17]
            )
            left_position = Point(left_x, left_y)
            left_hand = Hand(left_landmarks, left_position)

            self.hands["left"] = left_hand
        else:
            self.hands["left"] = Hand.irreal()

        if processResult.right_hand_landmarks:
            right_landmarks = [Point(l.x * width, l.y * height) for l in processResult.right_hand_landmarks.landmark]

            (right_x, right_y) = Mathb.GetBarycenter(
                right_landmarks[0],
                right_landmarks[1],
                right_landmarks[5],
                right_landmarks[17]
            )
            
            right_position = Point(right_x, right_y)
            right_hand = Hand(right_landmarks, right_position)

            self.hands["right"] = right_hand
        else:
            self.hands["right"] = Hand.irreal()

        return self.pose, self.hands, self.face