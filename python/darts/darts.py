import math


def score(x_cord, y_cord):
    radius = math.sqrt(x_cord*x_cord + y_cord*y_cord)

    if radius <= 1:
        return 10
    if 5 >= radius > 1:
        return 5
    if 10.0 >= radius > 5:
        return 1
    return 0
