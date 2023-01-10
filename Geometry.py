import math

from OpticalProperty import OpticalProperty
from Ray import Ray
from Vector import Vector


class Geometry:

    def __init__(self, opticalProperty: OpticalProperty):
        self.opticalProperty = opticalProperty

    def setOpticalProperty(self, opticalProperty: OpticalProperty):
        self.opticalProperty = opticalProperty

    def getRadiance(self, irradiance):
        return self.opticalProperty.getRadiance(irradiance)  # Вызываем получение Яркости на материале

    def rayIntersection(self, ray: Ray) -> (Vector, Vector, Vector):
        pass

    def isShading(self, shadowRay: Ray):
        pass


class Sphere(Geometry):

    def __init__(self, center: Vector, radius: float, opticalProperty: OpticalProperty = OpticalProperty()):
        super().__init__(opticalProperty)
        self.center = center
        self.radius = radius

    def rayIntersection(self, ray: Ray) -> (Vector, Vector, int):
        o = ray.origin  # начало луча
        dir = ray.direction  # направление луча
        c = self.center
        r = self.radius
        vcenter = o - c
        d = dir.dot(vcenter)
        det = d ** 2 - (vcenter.dot(vcenter) - r ** 2)
        if det < 0:
            # print('Нет решений')
            return None
        # tmin = min(-d + np.sqrt(det), -d - np.sqrt(det))
        tmin = -d - math.sqrt(det)
        if tmin > ray.tmax:
            return None

        p = o + dir.multiply(tmin)
        n = p - c
        n = (n.multiply(2) - n).normalize()  # Спросить как правильно взять нормаль у шара
        return p, n, tmin

    def isShading(self, shadowRay: Ray):
        o = shadowRay.origin  # начало луча
        dir = shadowRay.direction  # направление луча
        c = self.center
        r = self.radius
        vcenter = o - c
        d = dir.dot(vcenter)
        det = d ** 2 - (vcenter.dot(vcenter) - r ** 2)
        if det < 0:
            return False

        t = -d - math.sqrt(det)
        p = o + dir.multiply(t)
        return p


class Quadrangle(Geometry):
    def __init__(self, points: list, opticalProperty: OpticalProperty = OpticalProperty()):
        super().__init__(opticalProperty)
        self.points = points
        v1 = points[0]  # нижняя точка
        v2 = points[1]  # следующая за v1 точкой при обходе по часовой
        v3 = points[3]  # предыдущая к v1 Точка при обхолде по часовой
        vec1: Vector = v2 - v1
        vec2: Vector = v3 - v1
        n = vec1.cross(vec2)
        self.N = n.normalize()
        self.area = n.length()

    def rayIntersection(self, ray: Ray):
        t = (self.points[3] - ray.origin).dot(self.N) / ray.direction.dot(self.N)
        tmin = t
        if tmin > ray.tmax:
            return None
        p = ray.origin + ray.direction.multiply(t)
        triangleVectors = [point - p for point in self.points]
        a1 = (triangleVectors[0].cross(triangleVectors[1])).length() * 0.5
        a2 = (triangleVectors[1].cross(triangleVectors[2])).length() * 0.5
        a3 = (triangleVectors[2].cross(triangleVectors[3])).length() * 0.5
        a4 = (triangleVectors[3].cross(triangleVectors[0])).length() * 0.5
        sum = a1 + a2 + a3 + a4
        if sum - self.area > 1e-3:
            return None
        return p, self.N, tmin

    def isShading(self, shadowRay: Ray):
        o = shadowRay.origin  # начало луча
        dir = shadowRay.direction  # направление луча
        t = (self.points[3] - o).dot(self.N) / dir.dot(self.N)

        p = o + dir.multiply(t)
        triangleVectors = [point - p for point in self.points]
        a1 = (triangleVectors[0].cross(triangleVectors[1])).length() * 0.5
        a2 = (triangleVectors[1].cross(triangleVectors[2])).length() * 0.5
        a3 = (triangleVectors[2].cross(triangleVectors[3])).length() * 0.5
        a4 = (triangleVectors[3].cross(triangleVectors[0])).length() * 0.5
        sum = a1 + a2 + a3 + a4
        if sum - self.area > 1e-5:
            return False
        return p
