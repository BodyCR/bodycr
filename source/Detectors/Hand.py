import cv2
import mediapipe as mp
from ..Modules.Mathb import Mathb
from ..Modules.Utils import Point
from ..Detectors.landmarks import hand as HandLandmarks

class Hand:
    UP, DOWN, RIGHT, LEFT = 1, 2, -1, -2

    landmarks = None
    position = None

    def __init__(self, landmarks: list, position: Point) -> None:
        self.landmarks = landmarks
        self.position = position

    def GetOrientation(self) -> int:
        m0x, m0y = self.landmarks[0].x, self.landmarks[0].y
        m9x, m9y = self.landmarks[9].x, self.landmarks[9].y

        m = 10e9 if abs(m9x - m0x) < 0.05 else abs((m9y - m0y) / (m9x - m0x))

        if m >= 0 and m <= 1:
            return self.RIGHT if m9x > m0x else self.LEFT
        
        if m > 1:
            return self.UP if m9y < m0y else self.DOWN
    
    def GetFinger(self, finger) -> list:
        if finger == 0:
            finger = 1
        finger_end = finger * 4
        finger_start = finger_end - (2 if finger == 1 else 3)

        finger = self.landmarks[finger_start:finger_end+1]

        return finger
    
    def GetFingers(self):
        fingers = (len(self.landmarks) - 1) // 4
        result = []

        for finger in range(1, fingers+1):
            result.append(self.GetFinger(finger))

        return result

    def GetClosedFinger(self, finger) -> bool:
        f = self.GetFinger(finger)

        sense = 135
        if finger == 1:
            angle = Mathb.GetAngle(f[0], f[1], f[2])
            return angle < sense

        top = Mathb.Distance(f[-1], self.landmarks[0])
        base = Mathb.Distance(f[0], self.landmarks[0])

        return top < base

    def GetClosedFingers(self) -> list:
        closed = []
        for finger in range(1, 6):
            closed.append(self.GetClosedFinger(finger))

        return closed
    
    def GetComposedFinger(self, landmark):
        if landmark > 1 and landmark <= 4:
            return 1
        elif landmark > 4 and landmark <= 8:
            return 2
        elif landmark > 8 and landmark <= 12:
            return 3
        elif landmark > 12 and landmark <= 16:
            return 4
        elif landmark > 16 and landmark <= 20:
            return 5
        else:
            return None
    
    @staticmethod
    def irreal():
        return Hand([], (-999, -999))

class HandDetector:
    """
        ## BodyCR Detector
        ### The detector class to hand capture
        #### `BodyCR.source.Detectors.Hand`

        ---------------

        ## Methods:
        1. `def __init__(...)` - Construct this class
        2. `def Read(...)` - Read the passed image and process it
    """

    def __init__(self,
               static_image_mode=False,
               max_num_hands=2,
               model_complexity=1,
               min_detection_confidence=0.5,
               min_tracking_confidence=0.5):
        self.mp_hands = mp.solutions.hands
        self.hand = self.mp_hands.Hands(
               static_image_mode=static_image_mode,
               max_num_hands=max_num_hands,
               model_complexity=model_complexity,
               min_detection_confidence=min_detection_confidence,
               min_tracking_confidence=min_tracking_confidence)

    def Read(self, img) -> list[Hand]:
        processResult = self.hand.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        hands = []

        h, w, _ = img.shape

        if not processResult.multi_hand_landmarks:
            return hands
        
        for hand in processResult.multi_hand_landmarks:
            hand_landmarks = [Point(m.x * w, m.y * h) for m in hand.landmark]

            (pos_x, pos_y) = Mathb.GetBarycenter(
                hand_landmarks[0],
                hand_landmarks[1],
                hand_landmarks[5],
                hand_landmarks[17]
            )

            position = Point(pos_x, pos_y)
            hand_result = Hand(hand_landmarks, position)

            hands.append(hand_result)

        return hands