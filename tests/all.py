import cv2
import BodyCR as cr

cap = cv2.VideoCapture(0)

capture = cr.BaseCapture.Capture(
    all=cr.Prefabs.ALL.lite.Mount(),
)
draw = cr.Utils.Draw()
fps = cr.Utils.FPS()

while True:
    _, img = cap.read()
    img = cv2.flip(img, 1)

    draw.UpdateImage(img)
    capture.Read(img, cr.Prefabs.DETECT_ALL)

    # draw.DrawComponent(capture.face, cr.BaseCapture.)
    draw.DrawComponent(capture.pose, cr.BaseCapture.PoseLandmarks.POSE_CONNECTIONS)
    for hand in capture.hands:
        draw.DrawComponent(hand.landmarks, cr.BaseCapture.HandLandmarks.HAND_CONNECTIONS)

    fps.Update(img)
    cv2.imshow("Detect all Test", img)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()