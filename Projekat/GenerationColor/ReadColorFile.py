from Matrix.Color import Color


def read_color_file():
    color = dict()
    file = open("GenerationColor/colorAndHeightRandom", 'r')
    lines = file.readlines()
    for line in lines:
        tokens = line.split("|")
        color[float(tokens[0])] = Color(int(tokens[1]), int(tokens[2]), int(tokens[3]))

    return color


def read_color_file_height_map():
    color = dict()
    file = open("GenerationColor/colorAndHeight", 'r')
    lines = file.readlines()
    for line in lines:
        tokens = line.split("|")
        color[float(tokens[0])] = Color(int(tokens[1]), int(tokens[2]), int(tokens[3]))

    return color


def read_color_file_wave():
    color = dict()
    file = open("GenerationColor/colorAndWave", 'r')
    lines = file.readlines()
    for line in lines:
        tokens = line.split("|")
        color[float(tokens[0])] = Color(int(tokens[1]), int(tokens[2]), int(tokens[3]))

    return color
