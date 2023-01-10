import math


class Vector:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.coord = [x, y, z]

    def __add__(self, vector):
        return Vector(self.x + vector.x, self.y + vector.y, self.z + vector.z)

    def __sub__(self, vector):
        return Vector(self.x - vector.x, self.y - vector.y, self.z - vector.z)

    def __abs__(self):
        return Vector(abs(self.x), abs(self.y), abs(self.z))

    def length(self):
        return math.sqrt(self.dot(self))

    def dot(self, vector):
        return self.x * vector.x + self.y * vector.y + self.z * vector.z

    # todo Какая то проблема со знаками
    def cross(self, vector):
        x = self.y * vector.z - self.z * vector.y
        y = self.x * vector.z - self.z * vector.x
        z = self.x * vector.y - self.y * vector.x
        return Vector(-x, y, -z)  # Скорее всего из-за того что это левая тройка векторов

    def multiply(self, scalar):
        return Vector(scalar * self.x, scalar * self.y, scalar * self.z)

    def normalize(self):
        length = self.length()
        return Vector(self.x / length, self.y / length, self.z / length)
