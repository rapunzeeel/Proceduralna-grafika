class Color(object):
    def __init__(self, r, g, b):
        self._r_color = r
        self._g_color = g
        self._b_color = b

    def __str__(self):
        return "(r,g,b) = ({}, {}, {})".format(self._r_color, self._g_color, self._b_color)

    def get_r_color(self):
        return self._r_color

    def get_g_color(self):
        return self._g_color

    def get_b_color(self):
        return self._b_color

    def set_r_color(self, r):
        self._r_color = r

    def set_g_color(self, g):
        self._g_color = g

    def set_b_color(self, b):
        self._b_color = b
