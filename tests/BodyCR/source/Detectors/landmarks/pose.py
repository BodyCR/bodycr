"""
    # BodyCR 
    ### Body Capture and Recognition
    ### Pose Landmarks
    #### An simple way to recognize poses, hands and face using Mediapipe and OpenCV, totalizing 532 landmarks recognizing in real-time

    ----------

    By convention, use cr instead of BodyCR, follow the good practice of use `import BodyCR as cr`.
    By convention, import from instead BodyCR.Modules, follow the good practice of use `from BodyCR.Modules import <Required modules>`. Or import directly of BodyCR main module

    Note: Use separate modules can be a pretty difficult, we recommend use the instead main module subdivision. You can import all submodules since Detector to Modules with an easy way, more simple than write this: `import BodyCR as cr`
"""

NOSE = 0
LEFT_EYE_INNER = 1
LEFT_EYE = 2
LEFT_EYE_OUTER = 3
RIGHT_EYE_INNER = 4
RIGHT_EYE = 5
RIGHT_EYE_OUTER = 6
LEFT_EAR = 7
RIGHT_EAR = 8
MOUTH_LEFT = 9
MOUTH_RIGHT = 10
LEFT_SHOULDER = 11
RIGHT_SHOULDER = 12
LEFT_ELBOW = 13
RIGHT_ELBOW = 14
LEFT_WRIST = 15
RIGHT_WRIST = 16
LEFT_PINKY = 17
RIGHT_PINKY = 18
LEFT_INDEX = 19
RIGHT_INDEX = 20
LEFT_THUMB = 21
RIGHT_THUMB = 22
LEFT_HIP = 23
RIGHT_HIP = 24
LEFT_KNEE = 25
RIGHT_KNEE = 26
LEFT_ANKLE = 27
RIGHT_ANKLE = 28
LEFT_HEEL = 29
RIGHT_HEEL = 30
LEFT_FOOT_INDEX = 31
RIGHT_FOOT_INDEX = 32

####  CONNECTIONS

LEFT_ARM_CONNECTIONS = frozenset([
    (20, 16),
    (16, 18),
    (18, 20),
    (16, 22),
    # Arm
    (16, 14),
    (14, 12)
])

RIGHT_ARM_CONNECTIONS = frozenset([
    (19, 17),
    (17, 15),
    (15, 19),
    (15, 21),
    # Arm
    (15, 13),
    (13, 11)
])

CHEST_CONNECTIONS = frozenset([
    (12, 11),
    (11, 23),
    (23, 24),
    (24, 12)
])

LEFT_FOOT_CONNECTIONS = frozenset([
    (30, 32),
    (32, 28),
    (28, 30),
    # Leg
    (28, 26),
    (26, 24)
])

RIGHT_FOOT_CONNECTIONS = frozenset([
    (29, 31),
    (31, 27),
    (27, 29),
    # Leg
    (27, 25),
    (25, 23)
])

FACE_CONNECTIONS = frozenset([
    (10, 9),
    (8, 5),
    (5, 0),
    (0, 2),
    (2, 7)
])

POSE_CONNECTIONS = frozenset().union(*[
    FACE_CONNECTIONS,
    CHEST_CONNECTIONS,
    LEFT_ARM_CONNECTIONS,
    RIGHT_ARM_CONNECTIONS,
    LEFT_FOOT_CONNECTIONS,
    RIGHT_FOOT_CONNECTIONS,
])