from Vector import Vector


class Ray:
    def __init__(self, origin: Vector, direction: Vector):
        self.tmin = 0
        self.tmax = 10000
        self.origin = origin
        self.direction = direction

    @staticmethod
    def buildRay(startPoint: Vector, endPoint: Vector):
        direction = (endPoint - startPoint).normalize()
        return Ray(startPoint, direction)

# class ShadowRay(Ray):
#     def __init__(self, origin: Vector, direction: Vector):
#         super().__init__(origin, direction)
