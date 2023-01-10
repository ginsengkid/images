import random

from Ray import Ray
from Vector import Vector
import numpy as np


class Camera:
    ulPoint = Vector(-5, 5, 0)  # левый верхний угол

    def __init__(self, res):
        self.res = np.array(res)  # разрешение
        self.position = Vector(0, 0, -10)
        self.dx = 2 * -self.ulPoint.x / self.res[1]
        self.dy = 2 * self.ulPoint.y / self.res[0]

    def getRay(self, x, y) -> Ray:
        direction = self.calc_direction(x, y)
        return Ray(self.position, direction)

    def calc_direction(self, x, y) -> Vector:
        # xs = self.ulPoint.x + self.dx / 2
        # ys = self.ulPoint.y - self.dy / 2
        xs = self.ulPoint.x + random.uniform(0, self.dx)
        ys = self.ulPoint.y - random.uniform(0, self.dy)
        p = Vector(x * self.dx + xs, -y * self.dy + ys, 0)
        v: Vector = (p - self.position).normalize()
        return v

    def matrixSize(self):
        return np.array([2 * self.ulPoint.x() / self.res[0], 2 * self.ulPoint.y() / self.res[1], ])

    def lookDirection(self, xi, yi):
        size = self.matrixSize()

        matrixPoint = Vector(xi * size[0] - self.ulPoint.x(), -yi * size[1] + self.ulPoint.y(), -self.obsZ)
        len = matrixPoint.length()

        return matrixPoint.multiply(1 / len)
