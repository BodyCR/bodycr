"""
    # BodyCR 
    ### Body Capture and Recognition
    ### Hand Landmarks
    #### An simple way to recognize poses, hands and face using Mediapipe and OpenCV, totalizing 532 landmarks recognizing in real-time

    ----------

    By convention, use cr instead of BodyCR, follow the good practice of use `import BodyCR as cr`.
    By convention, import from instead BodyCR.Modules, follow the good practice of use `from BodyCR.Modules import <Required modules>`. Or import directly of BodyCR main module

    Note: Use separate modules can be a pretty difficult, we recommend use the instead main module subdivision. You can import all submodules since Detector to Modules with an easy way, more simple than write this: `import BodyCR as cr`
"""

WRIST = 0
THUMB_CMC = 1
THUMB_MCP = 2
THUMB_IP = 3
THUMB_TIP = 4
INDEX_FINGER_MCP = 5
INDEX_FINGER_PIP = 6
INDEX_FINGER_DIP = 7
INDEX_FINGER_TIP = 8
MIDDLE_FINGER_MCP = 9
MIDDLE_FINGER_PIP = 10
MIDDLE_FINGER_DIP = 11
MIDDLE_FINGER_TIP = 12
RING_FINGER_MCP = 13
RING_FINGER_PIP = 14
RING_FINGER_DIP = 15
RING_FINGER_TIP = 16
PINKY_MCP = 17
PINKY_PIP = 18
PINKY_DIP = 19
PINKY_TIP = 20

### CONNECTIONS

WRIST_CONNECTIONS = frozenset([
    (0, 1),
    (0, 5),
    (0, 17)
])

THUMB_CONNECTIONS = frozenset([
    (1, 2),
    (2, 3),
    (3, 4),
])

INDEX_CONNECTIONS = frozenset([
    (5, 6),
    (6, 7),
    (7, 8),
])

MIDDLE_CONNECTIONS = frozenset([
    (9, 10),
    (10, 11),
    (11, 12),
])

RING_CONNECTIONS = frozenset([
    (13, 14),
    (14, 15),
    (15, 16),
])

PINKY_CONNECTIONS = frozenset([
    (17, 18),
    (18, 19),
    (19, 20),
])

INTER_CONNECTIONS = frozenset([
    (5, 9),
    (9, 13),
    (13, 17),
])

HAND_CONNECTIONS = frozenset().union(*[
    WRIST_CONNECTIONS,
    THUMB_CONNECTIONS,
    INDEX_CONNECTIONS,
    MIDDLE_CONNECTIONS,
    RING_CONNECTIONS,
    PINKY_CONNECTIONS,
    INTER_CONNECTIONS
])