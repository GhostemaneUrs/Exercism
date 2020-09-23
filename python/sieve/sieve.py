def primes(limit):
    if limit == 1:
        return []

    values = range(2, limit + 1)
    completion_limit = limit**(1/2)

    primes = []
    while values[0] < completion_limit:
        primes.append(values[0])
        values = [val for val in values if val % values[0] != 0]

    primes += values

    return primes
