def is_armstrong_number(number):
    arms_num = sum([int(x)**int(len(str(number))) for x in str(number)])
    return True if arms_num == number else False
