import cv2
import BodyCR as cr

cap = cv2.VideoCapture(0)

capture = cr.BaseCapture.Capture(
    all=cr.Prefabs.ALL.lite,
)
draw = cr.Utils.Draw()
fps = cr.Utils.FPS()

while True:
    _, img = cap.read()
    img = cv2.flip(img, 1)

    draw.UpdateImage(img)
    capture.Read(img, cr.Prefabs.DETECT_POSE)

    for landmark in capture.pose:
        draw.PutCircle(landmark, 3, draw.FILL, draw.red, border=1, borderColor=draw.white)

    for landmark in capture.face:
        draw.PutCircle(landmark, 3, draw.FILL, draw.blue, border=1, borderColor=draw.white)

    for hand in capture.hands:
        for landmark in hand.landmarks:
            draw.PutCircle(landmark, 3, draw.FILL, draw.green, border=1, borderColor=draw.white)

    fps.Update(img)
    cv2.imshow("README Test", img)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()