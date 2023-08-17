import numpy as np
import math
from ..Modules.Utils import Point

class Mathb:
    @staticmethod
    def Projection(size1, size2, point) -> tuple:
        prop_x = np.divide([size1[0]], size2[0])
        prop_y = np.divide([size1[1]], size2[1])

        if prop_x > prop_y:
            prop_x = prop_y
        elif prop_y > prop_x:
            prop_y = prop_x

        return point[0] * prop_x, point[1] * prop_y

    @staticmethod
    def GetAngle(point1, point2, point3) -> float:
        vector1 = Mathb.Sub(point1, point2)
        vector2 = Mathb.Sub(point3, point2)

        # Cálculo do produto interno dos vetores
        dot_product = vector1.x * vector2.x + vector1.y * vector2.y

        # Normas dos vetores
        magnitude_vector1 = Mathb.Magnitude(vector1)
        magnitude_vector2 = Mathb.Magnitude(vector2)

        # Verifica se os vetores são linearmente dependentes (produto interno igual a 0)
        if magnitude_vector1 * magnitude_vector2 == 0:
            return 0.0

        # Cálculo do cosseno do ângulo entre os vetores usando o produto interno e as normas dos vetores
        angle_cos = dot_product / (magnitude_vector1 * magnitude_vector2)

        # Tratamento para valores fora do intervalo válido para o cosseno
        angle_cos = max(-1.0, min(angle_cos, 1.0))

        # Cálculo do ângulo em radianos
        angle_rad = math.acos(angle_cos)

        # Cálculo do ângulo em graus
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