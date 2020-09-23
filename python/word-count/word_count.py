import re
from collections import Counter


def count_words(sentence):
    condicion = r"[a-zA-Z\d]+(?:\'t)?"
    palabras = re.findall(condicion, sentence)
    return Counter(map(str.lower, palabras))
