class SpaceAge(object):
    seconds = 0

    def __init__(self, seconds):
        self.seconds = seconds

    def calcular(self, param):
        return float("{:.2f}".format(self.seconds / (31557600 * param)))

    def on_earth(self):
        return self.calcular(1)

    def on_venus(self):
        return self.calcular(0.61519726)

    def on_mercury(self):
        return self.calcular(0.2408467)

    def on_mars(self):
        return self.calcular(1.8808158)

    def on_jupiter(self):
        return self.calcular(11.862615)

    def on_saturn(self):
        return self.calcular(29.447498)

    def on_uranus(self):
        return self.calcular(84.016846)

    def on_neptune(self):
        return self.calcular(164.79132)
