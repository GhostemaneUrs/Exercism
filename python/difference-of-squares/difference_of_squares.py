def square_of_sum(number):
    sum_numbers = 0
    for i in range(1, number + 1):
        sum_numbers += i
    return pow(sum_numbers, 2)


def sum_of_squares(number):
    sum_squares = 0
    for i in range(1, number + 1):
        sum_squares += pow(i, 2)
    return sum_squares


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
