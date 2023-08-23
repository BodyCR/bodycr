import cv2
import time

class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

class FPS:
    def __init__(self):
        self.prevTime = 0

    def Update(self, img):
        """
            Update the fps, if pass a image, print the FPS in the passed image
        """
        currentTime = time.time()
        fps = int(1/(currentTime - self.prevTime))
        self.prevTime = currentTime

        self.fps = fps

        if img is not None:
            cv2.putText(img, "FPS: "+str(fps), (50, 50), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)