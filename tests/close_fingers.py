import cv2
import BodyCR as cr

cap = cv2.VideoCapture(0)

capture = cr.BaseCapture.Capture(
    hands=cr.Prefabs.HANDS.lite,
)
draw = cr.Utils.Draw()
fps = cr.Utils.FPS()

while True:
    _, img = cap.read()
    img = cv2.flip(img, 1)

    draw.UpdateImage(img)
    capture.Read(img, cr.Prefabs.DETECT_HAND)

    for hand in capture.hands:
        for id, landmark in enumerate(hand.landmarks):
            finger = hand.GetComposedFinger(id)
            closed = hand.GetClosedFinger(finger) if finger != None else None
            draw.PutCircle(landmark, 3, draw.FILL, draw.green if closed == True else draw.red, border=1, borderColor=draw.white)

    fps.Update(img)
    cv2.imshow("Closed Fingers Test", img)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()