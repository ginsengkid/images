import math


# todo Модель Фонга
class OpticalProperty:
    def __init__(self):
        self.kd = 0.5  # коэф диффузного отражения
        self.kf = 0.5  # коэф фонга
        self.kbf = 0.5  # коэф блинк-фонга

    # todo Сложить
    def getRadiance(self, irradiance):
        PiIrr = 1 / math.pi * irradiance
        return self.kd * PiIrr  # + self.kf * PiIrr