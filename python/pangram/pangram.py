import string


def is_pangram(sentence):
    alphabet = set(string.ascii_lowercase)
    if set(sentence.lower()) >= alphabet:
        return True
    return False
