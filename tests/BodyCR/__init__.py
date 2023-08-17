"""
    # BodyCR 
    ### Body Capture Recognition

    #### An simple way to recognize poses, hands and faces using Mediapipe and OpenCV

    ----------

    By convention, use cr instead of BodyCR, follow the good practice of use `import BodyCR as cr`.
    By convention, import from instead BodyCR.Utils, follow the good practice of use `from BodyCR.Utils import <Required modules>`.

    Note: Use separate modules can be a pretty difficult, we recommend use the instead main module subdivision. You can import all submodules since Detector to Modules with an easy way, more simple than write this: `import BodyCR as cr`

    ----------

    ### Build-in Features
    1. BodyCR Base Module - Have the basic pose recognition
    2. BodyCR Hands Module - Have the structure of a hand and methods to manage it
    3. BodyCR Utils Module:
        1. Mathb (Math BodyCR) - Have static methods to easily math operations with landmarks, e.g. GetAngle, Normalize...
        2. Point - The basic thing on BodyCR, represent a point in a 2D plane
        3. Draw - Allows an easy way to draw forms and texts in the OpenCV Mat
"""

from BodyCR.source.Detectors import Pose
from BodyCR.source.Detectors import Hand
from BodyCR.source.Detectors import Face
from BodyCR.source.Detectors import Holistic
from BodyCR.source.Detectors import Base as BaseCapture
from BodyCR.source.Detectors.configurations import Prefabs
from BodyCR.source.Modules import Mathb, Utils, gpu

class Resolutions:
    """
        All resolutions of 4:3 aspect
    """

    QQVGA = (160, 120)
    QVGA = (320, 240)
    VGA = (640, 480)
    SVGA = (800, 600)
    XGA = (1024, 768)
    XGAP = (1152, 864)
    QXGA = (2048, 1536)
    QUXGA = (3200, 2400)
    HXGA = (4096, 3072)
    HUXGA = (6400, 4800)