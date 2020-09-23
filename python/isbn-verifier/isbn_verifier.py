import re


def is_valid(isbn):
    isbn = isbn.replace("-", "")
    numeros = re.findall(r'[\d]*X?$', isbn)
    numeros = list(numeros[0])
    numeros = [num.replace("X", "10")for num in numeros]
    if len(numeros) != 10:
        return False
    else:
        suma = 0
        n = 10
        for i in numeros:
            suma += (n * int(i))
            n -= 1
    return (suma % 11 == 0)
