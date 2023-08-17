"""
    # BodyCR Detectors
    ### Body Capture Recognition

    #### Disponibilizes the Pose, Hands, Face, Holistic and Base Detectors

    ----------

    By convention, use cr instead of BodyCR, follow the good practice of use `import BodyCR as cr`.
    By convention, import from instead BodyCR.Utils, follow the good practice of use `from BodyCR.Utils import <Required modules>`.

    Note: Use separate modules can be a pretty difficult, we recommend use the instead main module subdivision. You can import all submodules since Detector to Modules with an easy way, more simple than write this: `import BodyCR as cr`

    ----------

    ### Build-in Features
    1. Mathb (Math BodyCR) - Have static methods to easily math operations with landmarks, e.g. GetAngle, Normalize...
    2. Point - The basic thing on BodyCR, represent a point in a 2D plane
    3. Draw - Allows an easy way to draw forms and texts in the OpenCV Mat
    3. BuildDrawer - Allows an easy way to draw preformated shapes of landmarks like pose, hand and face detectors
"""

from ..Detectors import Base
from ..Detectors import Pose
from ..Detectors import Hand
from ..Detectors import Face
from ..Detectors import Holistic