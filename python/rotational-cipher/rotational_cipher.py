from string import ascii_uppercase
from string import ascii_lowercase


def rotate(words, num):
    ciphers = converter(num)
    return words if num == 0 else "".join([ciphers[letter] if letter.isalpha() else letter for letter in words])


def converter(num):
    ciphers = {ascii_lowercase[i]: ascii_lowercase[(i + num) % 26] for i in range(26)}
    uppercase_ciphers = {ascii_uppercase[i]: ascii_uppercase[(i + num) % 26] for i in range(26)}
    ciphers.update(uppercase_ciphers)
    return ciphers
