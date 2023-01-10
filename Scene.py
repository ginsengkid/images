class Scene:
    geometry = []
    light = []
    defaultRadiance = 1

    def __init__(self, **kwargs):
        self.geometry.extend(kwargs.get('geometry'))
        self.light.extend(kwargs.get('light'))

    def addGeometry(self, *args):
        self.geometry.extend(args)

    def addLight(self, *args):
        self.light = args[0]

    def getDefaultBackground(self):
        return self.defaultRadiance
