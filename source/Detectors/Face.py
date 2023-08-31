"""

"""

import cv2
import mediapipe as mp
from ..Detectors.landmarks import face as FaceMeshLandmarks
from ..Modules.Utils import Point
from ..Modules.Mathb import Mathb

class Face:
    position = Point(-999, -999)
    landmarks = []

    def __init__(self, landmarks, position):
        self.position = position
        self.landmarks = landmarks

class FaceMeshDetector:
    """
        ## BodyCR Detector
        ### The detector class to face mesh capture
        #### `bodycr.source.Detectors.Face`

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
        processResult = self.face_mesh.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        faces = []

        h, w, _ = img.shape

        if not processResult.multi_face_landmarks:
            return faces
        
        for face in processResult.multi_face_landmarks:
            face_landmarks = [Point(m.x * w, m.y * h) for m in face.landmark]

            position = face_landmarks[164]
            face_result = Face(face_landmarks, position)

            faces.append(face_result)

        return faces