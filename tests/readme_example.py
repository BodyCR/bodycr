import cv2
import BodyCR as cr

cap = cv2.VideoCapture(0)

capture = cr.BaseCapture.Capture(
    pose=cr.Prefabs.POSE.lite.Mount(),
)
draw = cr.Utils.Draw()
fps = cr.Utils.FPS()

while True:
    _, img = cap.read()
    img = cv2.flip(img, 1)

    draw.UpdateImage(img)
    capture.Read(img, cr.Prefabs.DETECT_POSE)

    draw.DrawComponent(capture.pose, cr.Pose.PoseLandmarks.POSE_CONNECTIONS)

    fps.Update(img)
    cv2.imshow("README Test", img)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()