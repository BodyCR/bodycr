## Body CR - Body Capture and Recognition Library
The Body CR make easy the body recognition using _OpenCv_ and _Mediapipe_, providing an easy interface to detect complete body and hands

### Usage
To use the Pose detector, just import the library with `from Pose import Capture` and create a new instance of the Capture class using `capture = Capture()`. Now, to every frame capture, you need read all landmarks using `capture.Read(img)`, all landmarks was generated is in `capture.pose` (to pose detection) and `capture.hands` (to hand detection).

#### Full example
```python
import cv2                           # Import the Opencv2
import time                          # Used to calcule the FPS
from BodyCR import Capture           # Import the capture
from BodyCR.Utils import Draw, Point # Import the drawer and the two-dimension Point

cap = cv2.VideoCapture(0)   # Start the video capture
capture = Capture()         # Start the pose capture

draw = Draw()               # Start the drawer

previousTime = 0            # Used to calcule the FPS

while True:
    success, img = cap.read()         # Read the video capture
    img = cv2.resize(img, (640, 480)) # Resize the image to 

    capture.Read(img, detectHands=True, detectBody=True) # Read the pose capture
    draw.UpdateImage(img)                                # Update the drawer image

    pose_landmarks = capture.pose                                # Get pose landmarks
    hands_landmarks = [hand.landmarks for hand in capture.hands] # Get hands landmarks

    for landmark in pose_landmarks: # Get each pose landmark
        draw.PutMark(landmark)      # Draw the landmark

    for hand in hands_landmarks:    # Get each hand
        for landmark in hand:       # Get each landmark of hand
            draw.PutMark(landmark)  # Draw the landmark

    currentTime = time.time()
    fps = 1/(currentTime - previousTime)
    previousTime = currentTime

    draw.PutText(fps, Point(50, 50), draw.blue) # Draw the FPS

    cv2.imshow("Pose Detector Test", img) # Show the image

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
```

### Sample project using BodyCR
Here 