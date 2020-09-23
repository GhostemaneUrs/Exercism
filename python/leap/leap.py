def leap_year(year):
    if year % 4:
        return False
    if year % 100:
        return True
    return not year % 400
