import random
from random import randint


class Robot(object):

    def seed(self, seedNo):
        random.seed()

    def reset(self):
        letra1 = chr(randint(65, 90))
        letra2 = chr(randint(65, 90))
        no = randint(100, 999)
        self.name = letra1 + letra2 + str(no)

    def __init__(self):
        self.seed(1)
        self.reset()
