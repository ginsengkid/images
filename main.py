from matplotlib import pyplot as plt

from Camera import Camera
from Geometry import Sphere, Quadrangle
from Light import Light
from Render import Render
from Scene import Scene
from Vector import Vector

if __name__ == '__main__':
    camera = Camera([256, 256])
    sphere = Sphere(Vector(-1, 0, 10), 1)
    sphere2 = Sphere(Vector(10, 0, 10), 5)
    sphere3 = Sphere(Vector(-3, 2, 20), 5)
    light = Light(Vector(0, 0, 0), 5000)
    light2 = Light(Vector(5, 0, 0))
    light3 = Light(Vector(10, 10, 0))
    rect = Quadrangle([Vector(10, 0, 25), Vector(10, 15, 25),
                       Vector(-10, 15, 25), Vector(-10, 0, 25)])

    scene = Scene(geometry=[sphere, sphere2, sphere3],
                  light=[light, light3])
    render = Render(camera, scene)
    img = render.render()
    plt.imshow(img, cmap='gray')
    plt.show()
    for i in range(4):
        img += render.render()
        plt.imshow(img, cmap='gray')
        plt.show()
