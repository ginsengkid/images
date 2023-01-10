from Vector import Vector


class Light:
    def __init__(self, position: Vector, intensity: int = 10000):
        self.origin = position
        self.intensity = intensity

    def getRay(self):
        o = self.origin

    def gerIrradiance(self, point: Vector, n: Vector):
        dir = self.origin - point
        dot = dir.dot(n)
        if dot < 0:  # Вектор от точки до источника и нормаль в точке смотрят в разные стороны
            return 0
        cos = dot / dir.length()  # /n.length() = 1
        r = dir.length()
        return self.intensity / r ** 2 * cos


# todo Flat Light
class FlatLight(Light):
    pass
