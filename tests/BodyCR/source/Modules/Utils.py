import cv2
import time

def ToPoint(tuple):
    return Point(tuple[0], tuple[1])

class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def ToTup(self, toInt=True) -> tuple:
        return (int(self.x), int(self.y)) if toInt else (self.x, self.y)

class Draw:
    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (0, 0, 255)
    green = (0, 255, 0)
    blue = (255, 0, 0)
    yellow = (0, 255, 255)
    cyan = (255, 255, 0)
    magenta = (255, 0, 255)
    maroon = (128, 0, 0)
    olive = (0, 128, 0)
    navy = (0, 0, 128)
    olive_green = (128, 128, 0)
    teal = (0, 128, 128)
    purple = (128, 0, 128)
    orange = (0, 165, 255)
    pink = (203, 192, 255)
    saddle_brown = (19, 69, 139)
    gray = (128, 128, 128)

    FILL = -1

    def __init__(self, canDraw=True):
        self.canDraw = canDraw

    def UpdateImage(self, img):
        self.img = img

    def PutMark(self,pos,color=(0,0,255)):
        self.PutCircle(pos,15,-1, color)
        self.PutCircle(pos,20,2, color)

    def PutText(self,text,pos,color=(0,0,255)):
        cv2.putText(self.img, str(text), pos.ToTup(), cv2.FONT_HERSHEY_PLAIN, 5, color, 5)

    def PutLine(self,start,end,color=(0,0,255),thickness=2):
        start = (int(start.x), int(start.y))
        end = (int(end.x), int(end.y))
        cv2.line(self.img, start, end, color,thickness)

    def PutCircle(self,pos,radius,fill,color=(0,0,255), border=None, borderColor=(0, 0, 0)):
        cv2.circle(self.img, pos.ToTup(), radius, color, fill)

        if border is not None:
            cv2.circle(self.img, pos.ToTup(), radius+border, borderColor, border)

    def PutPolly(self,p1,p2,p3,color=(0,0,255)):
        self.PutLine(p1,p2,color)
        self.PutLine(p2,p3,color)
        self.PutLine(p3,p1,color)

    ############# ADVENCE

    def DrawConnections(self, landmarks, connections):
        length = len(landmarks)
        for connection in connections:
            if length >= connection[0] and  length >= connection[1]:
                self.PutLine(
                    landmarks[connection[0]],
                    landmarks[connection[1]],
                    self.white,
                    1
                )

    def DrawLandmarks(self, landmarks):
        for landmark in landmarks:
            self.PutCircle(landmark, 3, self.FILL, self.red, border=1, borderColor=self.white)

    def DrawComponent(self, landmarks, connections):
        self.DrawConnections(landmarks, connections)
        self.DrawLandmarks(landmarks)

class FPS:
    def __init__(self):
        self.prevTime = 0

    def Update(self, img):
        currentTime = time.time()
        fps = int(1/(currentTime - self.prevTime))
        self.prevTime = currentTime

        if img is not None:
            cv2.putText(img, "FPS: "+str(fps), (50, 50), cv2.FONT_HERSHEY_PLAIN, 2, Draw.blue, 2)