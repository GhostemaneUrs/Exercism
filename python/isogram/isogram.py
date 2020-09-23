def is_isogram(string):
    variable = string.translate(str.maketrans({' ': '', '-': ''})).lower()
    return len(set(variable)) == len(variable)
