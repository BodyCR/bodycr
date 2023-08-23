import numpy as np
import math
from ..Modules.Utils import Point

class Mathb:
    @staticmethod
    def TupToPoint(tuple):
        return Point(tuple[0], tuple[1])

    @staticmethod
    def PointToTup(point, toInt=True):
        return (int(point.x), int(point.y)) if toInt else (point.x, point.y)

    @staticmethod
    def Projection(size1, size2, point) -> tuple:
        """
            Project a point in the size 1 to the size 2
        """
        prop_x = size1[0] / size2[0]
        prop_y = size1[1] / size2[1]

        if prop_x > prop_y:
            prop_x = prop_y
        elif prop_y > prop_x:
            prop_y = prop_x

        return point[0] * prop_x, point[1] * prop_y

    @staticmethod
    def GetAngle(point1, point2, point3) -> float:
        vector1 = Mathb.Sub(point1, point2)
        vector2 = Mathb.Sub(point3, point2)

        dot_product = vector1.x * vector2.x + vector1.y * vector2.y

        magnitude_vector1 = Mathb.Magnitude(vector1)
        magnitude_vector2 = Mathb.Magnitude(vector2)

        if magnitude_vector1 * magnitude_vector2 == 0:
            return 0.0

        angle_cos = dot_product / (magnitude_vector1 * magnitude_vector2)
        angle_cos = max(-1.0, min(angle_cos, 1.0))
        angle_rad = math.acos(angle_cos)
        angle_deg = math.degrees(angle_rad)

        return round(angle_deg, 2)
    
    @staticmethod
    def GetBarycenter(*points) -> tuple:
        x = [p.x for p in points]
        y = [p.y for p in points]
        barycenter_X = np.sum(x) / len(points)
        barycenter_Y = np.sum(y) / len(points)

        return round(barycenter_X,2), round(barycenter_Y,2)
    
    ### Vetorial Methods

    @staticmethod
    def Sum(point1, point2):
        return Point(point1.x + point2.x, point1.y + point2.y)
    
    @staticmethod
    def Sub(point1, point2):
        return Point(point1.x - point2.x, point1.y - point2.y)
    
    @staticmethod
    def Mul(point1, point2):
        return Point(point1.x * point2.x, point1.y * point2.y)

    @staticmethod
    def Div(point1, point2):
        return Point(point1.x / point2.x, point1.y / point2.y)

    @staticmethod
    def Magnitude(point) -> float:
        return math.sqrt(point.x**2 + point.y**2)

    @staticmethod
    def Normalize(point):
        mag = Mathb.Magnitude(point)
        x_norm = point.x / mag
        y_norm = point.y / mag

        return Point(x_norm, y_norm)

    @staticmethod
    def Dot(point1, point2):
        mul = Mathb.Mul(point1, point2)
        return mul.x + mul.y
    
    @staticmethod
    def Projection( point1, point2):
        norm = Mathb.Normalize(point2)

        return Mathb.Mul(Mathb.Mul(point1, norm), norm)
    
    @staticmethod
    def Distance(a, b):
        return np.sqrt((b.x - a.x)**2 + (b.y - a.y)**2)
    
    @staticmethod
    def BoudingBox(landmarks):
        if len(landmarks) == 0:
            return {
                "width": 0,
                "height": 0,
                "x": -999,
                "y": -999
            }
    
        min_x = min(landmarks, key=lambda point: point.x).x
        max_x = max(landmarks, key=lambda point: point.x).x
        min_y = min(landmarks, key=lambda point: point.y).y
        max_y = max(landmarks, key=lambda point: point.y).y

        width = int(max_x - min_x)
        height = int(max_y - min_y)

        return {
            "width": width,
            "height": height,
            "x": int(min_x),
            "y": int(min_y)
        }