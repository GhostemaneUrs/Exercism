# Score categories.
# Change the values as you see fit.
from collections import Counter


YACHT = 12
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11


def score(dice, category):
    cont = Counter(dice)
    if category < 7:
        if category not in cont:
            return 0
        else:
            return cont[category]*category

    else:
        if category == FULL_HOUSE:
            flag = 0
            for i in cont:
                if cont[i] == 3:
                    flag = 1
                else:
                    pass
            if flag == 0:
                return 0
            else:
                return sum(dice)
        elif category == FOUR_OF_A_KIND:
            flag = 0
            out = 0
            for i in cont:
                if cont[i] > 3:
                    flag = 1
                    out = 4*i
                else:
                    pass
            if flag == 0:
                return 0
            else:
                return out
        elif category == LITTLE_STRAIGHT:
            if set(dice) == set([1, 2, 3, 4, 5]):
                return 30
            else:
                return 0
        elif category == BIG_STRAIGHT:
            if set(dice) == set([2, 3, 4, 5, 6]):
                return 30
            else:
                return 0
        elif category == CHOICE:
            return sum(dice)
        else:
            flag = 0
            for i in cont:
                if cont[i] == 5:
                    flag = 1
                else:
                    pass
            if flag == 0:
                return 0
            else:
                return 50
