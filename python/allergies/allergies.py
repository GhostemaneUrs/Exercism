from math import log


class Allergies(object):
    diccio = {"eggs": 1, "peanuts": 2, "shellfish": 4, "strawberries": 8,
                "tomatoes": 16, "chocolate": 32, "pollen": 64, "cats": 128}

    def __init__(self, score):
        self._lst = []
        s = bin(score)[2:]
        s = s[::-1] + ("0" * 8)
        self._s = s
        self.getAllAllergens()

    def allergic_to(self, item):
        return item in self._lst

    def check_allergen(self, item):
        idx = int(log(Allergies.diccio[item], 2))
        return self._s[idx] == "1"

    def getAllAllergens(self):
        for allergen in self.diccio.keys():
            if self.check_allergen(allergen):
                self._lst.append(allergen)

    @property
    def lst(self):
        return self._lst
