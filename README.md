## Body CR - Body Capture and Recognition Library
The Body CR make easy the body recognition using _OpenCv_ and _Mediapipe_, providing an easy interface to detect complete body and hands

### Usage
To use the Pose detector, just import the library with `import BodyCR as cr` and create a new instance of the Capture class using `capture = cr.Recognize()`. Now, to every frame capture, you need read all landmarks using `capture.Read(img)`, all landmarks was generated is in `capture.pose` (to pose detection), `capture.face` (to pfaceose detection) and `capture.hands` (to hand detection, in all detection, the index 0 in the right hand and 1 is left hand).

#### Full example

```python
# Importing OpenCV and BodyCR
import cv2
import BodyCR as cr

cap = cv2.VideoCapture(0) # Creating cv2 video capture

# Setting up the BodyCR Workspace

## Creating Base Capture
capture = cr.Recognize.Capture(
    pose=cr.Prefabs.POSE.normal.Mount(),
)
## Creating Drawer
draw = cr.Drawer()
## Creating the FPS Manager
fps = cr.FPS()

# Main Loop
while True:
    _, img = cap.read() # Reading the camera
    img = cv2.flip(img, 1) # Fliping the image

    draw.UpdateImage(img) # Update inset drawer image
    capture.Read(img, cr.Prefabs.DETECT_POSE) # Read the image with the BodyCR Capture

    draw.DrawComponent(capture.pose, cr.Pose.PoseLandmarks.POSE_CONNECTIONS) # Drawing the connections with Drawer

    fps.Update(img) # Update FPS Image
    cv2.imshow("README Test", img) # Show the result image

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()
```