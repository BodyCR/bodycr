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
    1. BodyCR Recognize Module - Advance and intelligent recognition
    2. BodyCR Pose Module - Advance recognition of pose
    3. BodyCR Hand Module - Advance recognition of hands anda simple way to manage it
    4. BodyCR Face Module - Advance recognition of face mesh
    5. BodyCR Holistic Module - Advance recognition of pose, hands and face in real-time¹
    6. BodyCR Utils Module:
        1. Mathb (Math BodyCR) - Have static methods to easily math operations with landmarks, e.g. GetAngle, Normalize...
        2. Point - The basic thing on BodyCR, represent a point in a 2D plane
        3. Drawer - Allows an easy way to draw forms and texts in the OpenCV Mat
        4. GPU - Allows use GPU Acceleration with CUDA and Tensorflow management

    ¹ See our github page to statistics: https://github.com/LucasOliveiraaa/BodyCR#full-body-recognition
"""

from BodyCR.source.Detectors import Pose
from BodyCR.source.Detectors import Hand
from BodyCR.source.Detectors import Face
from BodyCR.source.Detectors import Holistic
from BodyCR.source.Detectors import Base as Recognize
from BodyCR.source.Detectors.configurations import Prefabs
from BodyCR.source.Modules import gpu as GPU
from BodyCR.source.Modules.Drawer import Drawer
from BodyCR.source.Modules.Mathb import Mathb
from BodyCR.source.Modules.Utils import Point
from BodyCR.source.Modules.Utils import FPS

POSE_CONNECTIONS = Pose.PoseLandmarks.POSE_CONNECTIONS
HAND_CONNECTIONS = Hand.HandLandmarks.HAND_CONNECTIONS
FACE_CONNECTIONS = Face.FaceMeshLandmarks.FACEMESH_CONNECTIONS

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

def StartRecognition(pose=Prefabs.POSE.normal.Mount(), hands=Prefabs.HANDS.normal.Mount(), face=Prefabs.FACE.normal.Mount(), all=Prefabs.ALL.normal.Mount(), gpu=Prefabs.GPU_ACELERATION.Mount(), canDraw=True):
    """
        @DEPRECATED
    """

    return Recognize.Capture(pose, hands, face, all, gpu), Drawer(canDraw), FPS()

def Reload(img, capture, drawer, fps, read=Prefabs.DETECT_ALL):
    """
        @DEPRECATED
    """

    capture.Read(img, read)
    drawer.UpdateImage(img)
    fps.Update(img)