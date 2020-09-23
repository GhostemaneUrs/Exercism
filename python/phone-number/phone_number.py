from re import sub


class PhoneNumber(object):
    def __init__(self, number):
        self.number = sub("[^0-9]", "", number)
        longitud = len(self.number)
        if longitud < 10 or longitud > 11:
            raise ValueError("numero equivocado")
        elif longitud == 11:
            if self.number[0] != '1':
                raise ValueError("codigo de pais equivocad0")
            self.number = self.number[1:]
        if int(self.number[0]) < 2 or int(self.number[3]) < 2:
            raise ValueError("Area incorrecta")
        self.area_code = self.number[:3]
        self.exchange_code = self.number[3:6]

    def pretty(self):
         return f"({self.area_code}) {self.exchange_code}-{self.number[6:]}"
