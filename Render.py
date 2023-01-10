import numpy as np

from Camera import Camera
from Ray import Ray


class Render:
    def __init__(self,
                 camera=Camera([128, 128]),
                 scene=None):
        self.camera = camera
        self.scene = scene

    def render(self):
        img = np.zeros((self.camera.res[0], self.camera.res[1]))
        for i in range(self.camera.res[0]):
            for j in range(self.camera.res[1]):
                img[i][j] = self.scene.getDefaultBackground()
                ray = self.camera.getRay(j, i)
                for geom in self.scene.geometry:
                    ans = geom.rayIntersection(ray)
                    if ans:
                        p, n, rayLimit = ans
                        ray.tmax = rayLimit
                        img[i][j] = 0  # Скидываем фоновую яркость +
                        # Если объект ближе предыдущего надо сбросить яркость в этом пикселе
                    else:
                        continue
                    for light in self.scene.light:
                        dist = (light.origin - p).length()
                        for barrier in self.scene.geometry:
                            if barrier == geom:
                                continue
                            shadowRay = Ray.buildRay(light.origin, p)
                            answ = barrier.isShading(shadowRay)
                            if answ and dist > (answ - light.origin).length():
                                break
                        else:
                            E = light.gerIrradiance(p, n)
                            L = geom.getRadiance(E)
                            img[i][j] += L
        return img

    # def reflections(self, p, n, geom):
