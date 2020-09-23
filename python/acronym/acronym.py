import re


def abbreviate(words):
    words = re.sub(r"[^a-zA-Z' ]", " ", words.upper())
    words = words.replace("'", "")
    return ''.join([acronimo[0] for acronimo in words.split()])
