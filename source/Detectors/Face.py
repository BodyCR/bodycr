"""

"""

import cv2
import mediapipe as mp
from ..Detectors.landmarks import face as FaceMeshLandmarks

class FaceMeshDetector:
    """
        ## BodyCR Detector
        ### The detector class to face mesh capture
        #### `BodyCR.source.Detectors.Face`

        ---------------

        ## Methods:
        1. `def __init__(...)` - Construct this class
        2. `def Read(...)` - Read the passed image and process it
    """

    def __init__(self,
            static_image_mode=False,
            max_num_faces=1,
            refine_landmarks=False,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5):
        self.mp_face_mesh = mp.solutions.face_mesh
        self.face_mesh = self.mp_face_mesh.FaceMesh(
            static_image_mode=static_image_mode,
            max_num_faces=max_num_faces,
            refine_landmarks=refine_landmarks,
            min_detection_confidence=min_detection_confidence,
            min_tracking_confidence=min_tracking_confidence
        )

    def Read(self, img):
        """
            @UNFINISH
        """
        result = self.face_mesh.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))