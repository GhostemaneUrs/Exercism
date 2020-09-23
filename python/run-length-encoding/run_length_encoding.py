import re
from itertools import groupby


def decode(s):
    for i in re.finditer('(\\d+)(.)', s):
        num, char = i.groups(0)
        s = s.replace(num + char, int(num) * char, 1)
    return s


def encode(s):
    def pack(char, iterator):
        size = len(''.join(iterator))
        return '{:d}{:s}'.format(size, char) if size > 1 else char

    return ''.join(pack(char, grp) for char, grp in groupby(s))
