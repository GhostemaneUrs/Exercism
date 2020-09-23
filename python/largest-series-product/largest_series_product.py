from operator import mul
from functools import reduce
from sys import argv


def largest_product(series, size):
    if size == 0:
        return 1
    if size < 0 or len(series) < size:
        raise ValueError("Invalid size")
    return max(reduce(mul, map(int, series[i:i+size]))
               for i in range(len(series)-size+1))
    if __name__ == "__main__":
        print(largest_product(argv[1], int(argv[2])))
