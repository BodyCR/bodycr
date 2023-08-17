import cv2
import BodyCR as cr

cap = cv2.VideoCapture(0)

gpu_aceleration = cr.Prefabs.GPU_ACELERATION.Set("enable", True)

capture = cr.BaseCapture.Capture(
    all=cr.Prefabs.ALL.lite.Mount(),
    gpu=gpu_aceleration.Mount()
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

    fps.Update(img)
    cv2.imshow("README Test", img)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()