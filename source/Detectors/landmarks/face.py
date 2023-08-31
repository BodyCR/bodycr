"""
    # BodyCR 
    ### Body Capture and Recognition
    ### Face Landmarks
    #### An simple way to recognize poses, hands and face using Mediapipe and OpenCV, totalizing 532 landmarks recognizing in real-time

    ----------

    # WARN
    ## THE FACE MESH AND FACE DETECTION DON'T HAVE LANDMARK NAMES, JUST YOUR'S CONNECTIONS

    ----------

    By convention, use cr instead of BodyCR, follow the good practice of use `import BodyCR as cr`.
    By convention, import from instead BodyCR.Modules, follow the good practice of use `from BodyCR.Modules import <Required modules>`. Or import directly of BodyCR main module

    Note: Use separate modules can be a pretty difficult, we recommend use the instead main module subdivision. You can import all submodules since Detector to Modules with an easy way, more simple than write this: `import BodyCR as cr`
"""

OUTER_LIP_CONNECTIONS = frozenset([
    (0, 267),
    (267, 269),
    (269, 270),
    (270, 409),
    (409, 291),
    (291, 375),
    (375, 321),
    (321, 405),
    (405, 314),
    (314, 17),
    (17, 84),
    (84, 181),
    (181, 91),
    (91, 146),
    (146, 61),
    (61, 185),
    (185, 40),
    (40, 39),
    (39, 37),
    (37, 0)
])

INNER_LIP_CONNECTIONS = frozenset([
    (13, 312),
    (312, 311),
    (311, 310),
    (310, 415),
    (415, 308),
    (308, 324),
    (324, 318),
    (318, 402),
    (402, 317),
    (317, 14),
    (14, 87),
    (87, 178),
    (178, 88),
    (88, 95),
    (95, 78),
    (78, 191),
    (191, 80),
    (80, 81),
    (81, 82),
    (82, 13)
])

LIP_CONNECTIONS = frozenset().union(*[
    INNER_LIP_CONNECTIONS,
    OUTER_LIP_CONNECTIONS
])

LEFT_EYE_CONNECTIONS = frozenset([
    (33, 246),
    (246, 161),
    (161, 160),
    (160, 159),
    (159, 158),
    (158, 157),
    (157, 173),
    (173, 133),
    (133, 155),
    (155, 154),
    (154, 153),
    (153, 145),
    (145, 144),
    (144, 163),
    (163, 7),
    (7, 33)
])

LEFT_EYEBROW = frozenset([
    (107, 66),
    (66, 105),
    (105, 63),
    (63, 70),
    (70, 156),
    (156, 124),
    (124, 46),
    (46, 53),
    (53, 52),
    (52, 65),
    (65, 55),
    (55, 107),
])

RIGHT_EYE_CONNECTIONS = frozenset([
    (263, 466),
    (466, 388),
    (388, 387),
    (387, 386),
    (386, 385),
    (385, 384),
    (384, 398),
    (398, 362),
    (362, 382),
    (382, 381),
    (381, 380),
    (380, 374),
    (374, 373),
    (373, 390),
    (390, 249),
    (249, 263)
])

RIGHT_EYEBROW = frozenset([
    (336, 296),
    (296, 334),
    (334, 293),
    (293, 300),
    (300, 383),
    (383, 353),
    (353, 276),
    (276, 283),
    (283, 282),
    (282, 295),
    (295, 285),
    (285, 336),
])

EYES_CONNECTIONS = frozenset().union(*[
    LEFT_EYE_CONNECTIONS,
    LEFT_EYEBROW,
    RIGHT_EYE_CONNECTIONS,
    RIGHT_EYEBROW
])

CONTOUR = frozenset([
    (10, 338),
    (338, 297),
    (297, 332),
    (332, 284),
    (284, 251),
    (251, 389),
    (389, 356),
    (356, 454),
    (454, 323),
    (323, 361),
    (361, 288),
    (288, 397),
    (397, 365),
    (365, 379),
    (379, 378),
    (378, 400),
    (400, 377),
    (377, 152),
    (152, 148),
    (148, 176),
    (176, 149),
    (149, 150),
    (150, 136),
    (136, 172),
    (172, 58),
    (58, 132),
    (132, 93),
    (93, 234),
    (234, 127),
    (127, 162),
    (162, 21),
    (21, 54),
    (54, 103),
    (103, 67),
    (67, 109),
    (109, 10),
])

FACEMESH_CONNECTIONS = frozenset().union(*[
    LIP_CONNECTIONS,
    EYES_CONNECTIONS,
    CONTOUR
])