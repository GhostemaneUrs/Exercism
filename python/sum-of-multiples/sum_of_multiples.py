def sum_of_multiples(limit, multiples):
    return sum(i for i in range(1, limit) if any(m != 0 and i % m == 0 for m in multiples))
