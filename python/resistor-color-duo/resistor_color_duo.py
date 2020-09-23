colors_code = ['black', 'brown', 'red', 'orange', 'yellow',
               'green', 'blue', 'violet', 'grey', 'white']


def value(colors):
    return int(str(colors_code.index((colors[0:1])[0])) + str(colors_code.index((colors[1:2])[0])))
