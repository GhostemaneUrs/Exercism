def factors(value):
    contador = 2
    primes = []
    while value > 1:
        if value % contador == 0:
            value /= contador
            primes.append(contador)
        else:
            contador += 1
    return primes
