def convert(number):
    entrada = ""
    if number % 3 == 0:
        entrada += "Pling"
    if number % 5 == 0:
        entrada += "Plang"
    if number % 7 == 0:
        entrada += "Plong"
    return entrada if len(entrada) > 0 else str(number)
