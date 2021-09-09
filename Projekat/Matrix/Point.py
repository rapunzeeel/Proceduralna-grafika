class Point(object):
    def __init__(self, x, y, z):
        self._x_coord = x
        self._y_coord = y
        self._z_coord = z
        self._VBO_color = ()

    def __str__(self):
        return "(x,y,z) = ({}, {}, {})".format(self._x_coord, self._y_coord, self._z_coord)

    def get_x_coord(self):
        return self._x_coord

    def get_y_coord(self):
        return self._y_coord

    def get_z_coord(self):
        return self._z_coord

    def get_VBO_color(self):
        return self._VBO_color

    def set_x_coord(self, x):
        self._x_coord = x

    def set_y_coord(self, y):
        self._y_coord = y

    def set_z_coord(self, z):
        self._z_coord = z

    def set_VBO_color(self, color):
        self._VBO_color = color
