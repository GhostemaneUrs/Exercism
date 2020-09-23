def flatten(iterable):
    vect = []
    if hasattr(iterable, '__iter__') and not isinstance(iterable, str):
        for item in iterable:
            for i in flatten(item):
                vect.append(i)
    else:
        if iterable != None:
            vect.append(iterable)
    return vect
