"""
    # BodyCR 
    ### Body Capture Recognition

    #### An simple way to recognize poses and hands using Mediapipe and OpenCV

    ----------

    By convention, use cr instead of BodyCR, follow the good practice of use `import BodyCR as cr`.
    By convention, import from instead BodyCR.Utils, follow the good practice of use `from BodyCR.Utils import <Required modules>`.

    Note: Use separate modules can be a pretty difficult, we recommend use the instead main module subdivision. You can import all submodules since Detector to Modules with an easy way, more simple than write this: `import BodyCR as cr`

    ----------

    ### Build-in Features
    1. BodyCR Base Module - Have the basic pose recognition
    2. BodyCR Hands Module - Have the structure of a hand and methods to manage it
    2. BodyCR FaceMesh Module - Have the basic face mesh recognition
    3. BodyCR Utils Module:
        1. Mathb (Math BodyCR) - Have static methods to easily math operations with landmarks, e.g. GetAngle, Normalize...
        2. Point - The basic thing on BodyCR, represent a point in a 2D plane
        3. Draw - Allows an easy way to draw forms and texts in the OpenCV Mat
"""

from ..Detectors.configurations import Prefabs
from ..Modules.gpu import ConfigureGPUs
from ..Detectors.Pose import PoseDetector, PoseLandmarks
from ..Detectors.Hand import HandDetector, HandLandmarks
from ..Detectors.Face import FaceMeshDetector, FaceMeshLandmarks
from ..Detectors.Holistic import HolisticDetector

class Capture:
    """
        ## BodyCR Detector
        ### The detector class to hand capture
        #### `BodyCR.source.Detectors.Hand`

        ---------------

        ## Methods:
        1. `def __init__(...)` - Construct this class
        2. `def Read(...)` - Read the passed image and process it
    """

    pose = []
    hands = []
    face = []

    def __init__(self, pose=Prefabs.POSE.normal.Mount(), hands=Prefabs.HANDS.normal.Mount(), face=Prefabs.FACE.normal.Mount(), all=Prefabs.ALL.normal.Mount(), gpu=Prefabs.GPU_ACELERATION.Mount()) -> None:
        """
            ## Capture
            The constructor of Capture class

            ##### `Capture.__init__(pose: PoseConfiguration, hands: HandsConfiguration, face: FaceConfiguration, holistic: HolisticConfiguration, gpu: GPUAceleration) -> None`

            -----------

            ### Parameters:
            `pose: PoseConfiguration = Prefabs.POSE.normal` - Describe how the Mediapipe Pose Solution will be instancied
            `hands: HandsConfiguration = Prefabs.HANDS.normal` - Describe how the Mediapipe Hands Solution will be instancied
            `face: FaceConfiguration = Prefabs.FACE.normal` - Describe how the Mediapipe FaceMesh Solution will be instancied
            `all: HolisticConfiguration = Prefabs.ALL.normal` - Describe how the Mediapipe Holistic Solution will be instancied
            `gpu: GPUAceleration = Prefabs.GPU_ACELERATION_NORMAL` - Describe how the GPU aceleration will be used and started                               | None                        |

            ### Important Notes
            1. Use more of one mode (Pose, Hands, Face and Holistic) is not recommended, this can crash your computer if selected a high configuration or can make low FPS in the run, prefer use just one of those options, if you need to use more of one of them, use only the holistic mode.
        """

        if gpu["enable"]:
            ConfigureGPUs(gpu["memory_limit"], gpu["gpu_indices"], gpu["allow_growth"], gpu["per_process_gpu_memory_fraction"])

        self.__pose = PoseDetector(
            static_image_mode=pose["static_image_mode"],
            model_complexity=pose["model_complexity"],
            smooth_landmarks=pose["smooth_landmarks"],
            enable_segmentation=pose["enable_segmentation"],
            smooth_segmentation=pose["smooth_segmentation"],
            min_detection_confidence=pose["min_detection_confidence"],
            min_tracking_confidence=pose["min_tracking_confidence"]
        )

        self.__hand = HandDetector(
            static_image_mode=hands["static_image_mode"],
            max_num_hands=hands["max_num_hands"],
            model_complexity=hands["model_complexity"],
            min_detection_confidence=hands["min_detection_confidence"],
            min_tracking_confidence=hands["min_tracking_confidence"]
        )

        self.__face = FaceMeshDetector(
            static_image_mode=face["static_image_mode"],
            max_num_faces=face["max_num_faces"],
            refine_landmarks=face["refine_landmarks"],
            min_detection_confidence=face["min_detection_confidence"],
            min_tracking_confidence=face["min_tracking_confidence"]
        )

        self.__holistic = HolisticDetector(
            static_image_mode=all["static_image_mode"],
            model_complexity=all["model_complexity"],
            smooth_landmarks=all["smooth_landmarks"],
            enable_segmentation=all["enable_segmentation"],
            smooth_segmentation=all["smooth_segmentation"],
            refine_face_landmarks=all["refine_face_landmarks"],
            min_detection_confidence=all["min_detection_confidence"],
            min_tracking_confidence=all["min_tracking_confidence"]
        )
    
    def Read(self, img, indentifier=Prefabs.DETECT_ALL) -> None:
        """
            ## Capture
            Read the passed image using the identifier

            ##### `Capture.Read(img: opencv2.Mat, idenfitier: DetectionIdentifier) -> None`

            -----------

            ### Parameters:
                `img: Mat` - The OpenCV Image
                `identifier: DetectionIdentifier = Prefabs.DETECT_HOLISTIC` - Especifies the mode of recognition
        """

        pose, hand, face = (int(i)==1 for i in indentifier)

        if pose == True and hand == True and face == True:
            self.pose, hands, self.face = self.__holistic.Read(img)
            self.hands = [hands["left"], hands["right"]]
            return
        
        if hand:
            self.hands = self.__hand.Read(img)
        
        if pose:
            self.pose = self.__pose.Read(img)
        
        if face:
            self.face = self.__face.Read(img)