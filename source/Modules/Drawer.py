import cv2
from ..Modules.Utils import Point
from ..Modules.Mathb import Mathb

PointToTup = Mathb.PointToTup

class Color:
    """
        Colors in BGR
    """

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

class Drawer:
    """
        Contai methods to draw in a cv2 image
    """

    FILL = -1

    def __init__(self, canDraw=True):
        self.canDraw = canDraw

    def UpdateImage(self, img):
        """
            Update the image
        """
        self.img = img

    def PutText(self,text,pos,color=(0,0,255)):
        """
            Put a text in the image inside
        """
        cv2.putText(self.img, str(text), PointToTup(pos), cv2.FONT_HERSHEY_DUPLEX, 0.5, color, 2)

    def PutLine(self,start,end,color=(0,0,255)):
        """
            Put a line in the image inside
        """
        start = (int(start.x), int(start.y))
        end = (int(end.x), int(end.y))
        cv2.line(self.img, start, end, color,2)

    def PutCircle(self,pos,radius,fill,color=(0,0,255), border=None, borderColor=(0, 0, 0)):
        """
            Put a circle in the image inside
        """
        cv2.circle(self.img, PointToTup(pos), radius, color, fill)

        if border is not None:
            cv2.circle(self.img, PointToTup(pos), radius+border, borderColor, border)

    def PutPolly(self,p1,p2,p3,color=(0,0,255)):
        """
            Put a 3vertex pollygon in the image inside
        """
        self.PutLine(p1,p2,color)
        self.PutLine(p2,p3,color)
        self.PutLine(p3,p1,color)

    def PutRect(self,pos,width,height,border=2,color=(0,0,255)):
        """
            Put a rectangle in the image inside
        """
        cv2.rectangle(self.img, (pos.x, pos.y), (pos.x + width, pos.y + height), color, border)

    def PutTextDist(self, text, font, font_size, thickness, pos, margins, text_color, rectangle_color):
        """
            Put a text inside a box in the image inside
        """
        font_scale = font_size
        font_color = text_color
        line_type = cv2.LINE_AA

        text_size = cv2.getTextSize(text, font, font_scale, thickness)[0]

        rectangle_width = text_size[0] + 2 * margins
        rectangle_height = text_size[1] + 2 * margins
        rectangle_top_left = (pos.x, pos.y)
        rectangle_bottom_right = (pos.x + rectangle_width, pos.y + rectangle_height)
        cv2.rectangle(self.img, rectangle_top_left, rectangle_bottom_right, rectangle_color, -1)

        text_x = pos.x + margins
        text_y = pos.y + margins + text_size[1]
        cv2.putText(self.img, text, (text_x, text_y), font, font_scale, font_color, thickness, line_type)

    def BoundingBox(self, boudingbox, label="", color=(0,0,255)):
        """
            Put a boudingbox in the image inside
        """
        pos = Point(boudingbox["x"], boudingbox["y"])
        width, height = boudingbox["width"], boudingbox["height"]

        self.PutRect(pos, width, height, 4, color)
        
        if label != "":
            pos.y += height
            pos.x -= 2
            self.PutTextDist(label, cv2.FONT_HERSHEY_COMPLEX, 0.75, 1, pos, 7, Color.white, color)

    ############# ADVENCE

    def DrawConnections(self, landmarks, connections):
        """
            Craw all connections in a group of landmarks
        """
        length = len(landmarks)
        for connection in connections:
            if length >= connection[0] and  length >= connection[1]:
                self.PutLine(
                    landmarks[connection[0]],
                    landmarks[connection[1]],
                    Color.white
                )

    def DrawLandmarks(self, landmarks):
        """
            Draw all landmarks
        """
        for landmark in landmarks:
            self.PutCircle(landmark, 3, self.FILL, Color.red, border=1, borderColor=Color.white)

    def DrawComponent(self, landmarks, connections):
        """
            Draw all landmarks and yours connections
        """
        self.DrawConnections(landmarks, connections)
        self.DrawLandmarks(landmarks)