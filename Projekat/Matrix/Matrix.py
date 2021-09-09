from Matrix.Color import Color
from Matrix.Point import Point

HEIGHT = 600
WIDTH = 600


class Matrix(object):
    def __init__(self):
        self.point = None
        self.VBO_coord = []
        self.VBO_scale_color_value = []
        self.list_unallowed = []
        self.list_allowed_horizontal_down = []
        self.list_allowed_horizontal_up = []
        self.list_allowed_vertical_left = []
        self.list_allowed_vertical_right = []
        self.list_unallowed_water = []
        self.list_allowed_horizontal_down_water = []
        self.list_allowed_horizontal_up_water = []
        self.list_allowed_vertical_left_water = []
        self.list_allowed_vertical_right_water = []

    def create_matrix(self):
        for i in range(-int(WIDTH / 30), int(WIDTH / 30)):
            for j in range(-int(HEIGHT / 30), int(HEIGHT / 30)):
                self.point = Point(i, j, 0)
                self.point.set_VBO_color(Color(0, 0, 0))
                self.VBO_coord.append(self.point)
        return self.VBO_coord

    def create_matrix_height_map(self):
        i = -int(WIDTH / 20) / 2
        while i < int(WIDTH / 20) / 2:
            j = -int(HEIGHT / 20) / 2
            while j < int(HEIGHT / 20) / 2:
                self.point = Point(i, j, 0)
                self.point.set_VBO_color(Color(0, 0, 0))
                self.VBO_coord.append(self.point)
                j += 0.5
            i += 0.5
        return self.VBO_coord

    def smooth_neighbour_z_coord(self):
        for i in range(len(self.VBO_coord)):
            if i not in self.list_unallowed:
                self.smooth_four_neighbour(i)
            else:
                if i in [0, 39, 1560, 1599]:
                    self.smooth_corners(i)
                    self.smooth_corners(i)
                else:
                    self.smooth_edges(i)

    def smooth_four_neighbour(self, i):
        list_neighbours = [i + 1, i - 1, i + 40, i - 40, i + 41, i - 39, i + 39, i - 41]
        corners = (self.VBO_coord[list_neighbours[7]].get_z_coord() + self.VBO_coord[
            list_neighbours[6]].get_z_coord() + self.VBO_coord[list_neighbours[5]].get_z_coord() +
                   self.VBO_coord[
                       list_neighbours[4]].get_z_coord()) / 16.0
        sides = (self.VBO_coord[list_neighbours[0]].get_z_coord() + self.VBO_coord[
            list_neighbours[1]].get_z_coord() +
                 self.VBO_coord[list_neighbours[2]].get_z_coord() + self.VBO_coord[
                     list_neighbours[3]].get_z_coord()) / 8.0
        center = self.VBO_coord[i].get_z_coord() / 4.0
        self.VBO_coord[i].set_z_coord(corners + sides + center)

    def smooth_edges(self, i):
        list_neighbours = []
        if i in self.list_allowed_horizontal_down:
            list_neighbours = [i + 40, i - 40, i + 1, i - 39, i + 41]  # donja horizontalna
        elif i in self.list_allowed_horizontal_up:
            list_neighbours = [i + 40, i - 40, i - 1, i + 39, i - 41]  # gornja horizontalna
        elif i in self.list_allowed_vertical_left:
            list_neighbours = [i + 1, i - 1, i + 40, i + 39, i + 41]  # leva vertikalna
        elif i in self.list_allowed_vertical_right:
            list_neighbours = [i + 1, i - 1, i - 40, i - 39, i - 41]  # desna vertikalna
        sides = (self.VBO_coord[list_neighbours[0]].get_z_coord() + self.VBO_coord[
            list_neighbours[1]].get_z_coord() + self.VBO_coord[list_neighbours[2]].get_z_coord()) / 6.0
        corners = (self.VBO_coord[list_neighbours[3]].get_z_coord() + self.VBO_coord[
            list_neighbours[4]].get_z_coord()) / 8.0
        center = self.VBO_coord[i].get_z_coord() / 4.0
        self.VBO_coord[i].set_z_coord(sides + center + corners)

    def smooth_corners(self, i):
        list_neighbours = []
        if i == 0:
            list_neighbours = [i + 1, i + 40, i + 41]
        elif i == 39:
            list_neighbours = [i - 1, i + 40, i + 39]
        elif i == 1560:
            list_neighbours = [i + 1, i - 40, i - 39]
        elif i == 1599:
            list_neighbours = [i - 1, i - 40, i - 41]
        sides = (self.VBO_coord[list_neighbours[0]].get_z_coord() + self.VBO_coord[
            list_neighbours[1]].get_z_coord()) / 8.0
        corner = self.VBO_coord[list_neighbours[2]].get_z_coord() / 4.0
        center = self.VBO_coord[i].get_z_coord() / 2.0
        self.VBO_coord[i].set_z_coord(sides + center + corner)

    def create_list_unallowed(self):
        for i in range(0, 40, 1):
            self.list_unallowed.append(i)
        for i in range(0, 1600, 40):
            self.list_unallowed.append(i)
        for i in range(39, 1600, 40):
            self.list_unallowed.append(i)
        for i in range(1599, 1558, -1):
            self.list_unallowed.append(i)

    def create_list_allowed(self):
        for i in range(40, 1600, 40):
            self.list_allowed_horizontal_down.append(i)
        for i in range(79, 1600, 40):
            self.list_allowed_horizontal_up.append(i)
        for i in range(1599, 1558, -1):
            self.list_allowed_vertical_right.append(i)
        for i in range(0, 40):
            self.list_allowed_vertical_left.append(i)

    def smooth_neighbour_water(self):
        for i in range(len(self.VBO_coord)):
            if i not in self.list_unallowed_water:
                self.smooth_four_neighbour_water(i)
            else:
                if i in [0, 59, 3540, 3599]:
                    self.smooth_corners_water(i)
                    self.smooth_corners_water(i)
                else:
                    self.smooth_edges_water(i)

    def smooth_four_neighbour_water(self, i):
        list_neighbours = [i + 1, i - 1, i + 60, i - 60, i + 61, i - 59, i + 59, i - 61]
        corners = (self.VBO_coord[list_neighbours[7]].get_z_coord() + self.VBO_coord[
            list_neighbours[6]].get_z_coord() + self.VBO_coord[list_neighbours[5]].get_z_coord() +
                   self.VBO_coord[
                       list_neighbours[4]].get_z_coord()) / 16.0
        sides = (self.VBO_coord[list_neighbours[0]].get_z_coord() + self.VBO_coord[
            list_neighbours[1]].get_z_coord() +
                 self.VBO_coord[list_neighbours[2]].get_z_coord() + self.VBO_coord[
                     list_neighbours[3]].get_z_coord()) / 8.0
        center = self.VBO_coord[i].get_z_coord() / 4.0
        self.VBO_coord[i].set_z_coord(corners + sides + center)

    def smooth_edges_water(self, i):
        list_neighbours = []
        if i in self.list_allowed_horizontal_down_water:
            list_neighbours = [i + 60, i - 60, i + 1, i - 59, i + 61]  # donja horizontalna
        elif i in self.list_allowed_horizontal_up_water:
            list_neighbours = [i + 60, i - 60, i - 1, i + 59, i - 61]  # gornja horizontalna
        elif i in self.list_allowed_vertical_left_water:
            list_neighbours = [i + 1, i - 1, i + 60, i + 59, i + 61]  # leva vertikalna
        elif i in self.list_allowed_vertical_right_water:
            list_neighbours = [i + 1, i - 1, i - 60, i - 59, i - 61]  # desna vertikalna
        sides = (self.VBO_coord[list_neighbours[0]].get_z_coord() + self.VBO_coord[
            list_neighbours[1]].get_z_coord() + self.VBO_coord[list_neighbours[2]].get_z_coord()) / 6.0
        corners = (self.VBO_coord[list_neighbours[3]].get_z_coord() + self.VBO_coord[
            list_neighbours[4]].get_z_coord()) / 8.0
        center = self.VBO_coord[i].get_z_coord() / 4.0
        self.VBO_coord[i].set_z_coord(sides + center + corners)

    def smooth_corners_water(self, i):
        list_neighbours = []
        if i == 0:
            list_neighbours = [i + 1, i + 60, i + 61]
        elif i == 59:
            list_neighbours = [i - 1, i + 60, i + 59]
        elif i == 3540:
            list_neighbours = [i + 1, i - 60, i - 59]
        elif i == 3599:
            list_neighbours = [i - 1, i - 60, i - 61]
        sides = (self.VBO_coord[list_neighbours[0]].get_z_coord() + self.VBO_coord[
            list_neighbours[1]].get_z_coord()) / 8.0
        corner = self.VBO_coord[list_neighbours[2]].get_z_coord() / 4.0
        center = self.VBO_coord[i].get_z_coord() / 2.0
        self.VBO_coord[i].set_z_coord(sides + center + corner)

    def create_list_unallowed_water(self):
        for i in range(0, 60, 1):
            self.list_unallowed_water.append(i)
        for i in range(0, 3600, 60):
            self.list_unallowed_water.append(i)
        for i in range(59, 3600, 60):
            self.list_unallowed_water.append(i)
        for i in range(3599, 3538, -1):
            self.list_unallowed_water.append(i)

    def create_list_allowed_water(self):
        for i in range(60, 3600, 60):
            self.list_allowed_horizontal_down_water.append(i)
        for i in range(119, 3600, 60):
            self.list_allowed_horizontal_up_water.append(i)
        for i in range(3599, 3538, -1):
            self.list_allowed_vertical_right_water.append(i)
        for i in range(0, 60):
            self.list_allowed_vertical_left_water.append(i)

    def smooth_b_color(self, i, list_neighbours, list_of_VBO_copy):
        corners = (list_of_VBO_copy[list_neighbours[7]].get_VBO_color().get_b_color() + list_of_VBO_copy[
            list_neighbours[6]].get_VBO_color().get_b_color() + list_of_VBO_copy[
                       list_neighbours[5]].get_VBO_color().get_b_color() +
                   list_of_VBO_copy[list_neighbours[4]].get_VBO_color().get_b_color()) / 16.0
        sides = (list_of_VBO_copy[list_neighbours[0]].get_VBO_color().get_b_color() + list_of_VBO_copy[
            list_neighbours[1]].get_VBO_color().get_b_color() +
                 list_of_VBO_copy[list_neighbours[2]].get_VBO_color().get_b_color() + list_of_VBO_copy[
                     list_neighbours[3]].get_VBO_color().get_b_color()) / 8.0
        center = list_of_VBO_copy[i].get_VBO_color().get_b_color() / 4.0
        self.VBO_coord[i].get_VBO_color().set_b_color(corners + sides + center)

    def smooth_g_color(self, i, list_neighbours, list_of_VBO_copy):
        corners = (list_of_VBO_copy[list_neighbours[7]].get_VBO_color().get_g_color() + list_of_VBO_copy[
            list_neighbours[6]].get_VBO_color().get_g_color() + list_of_VBO_copy[
                       list_neighbours[5]].get_VBO_color().get_g_color() +
                   list_of_VBO_copy[list_neighbours[4]].get_VBO_color().get_g_color()) / 16.0
        sides = (list_of_VBO_copy[list_neighbours[0]].get_VBO_color().get_g_color() + list_of_VBO_copy[
            list_neighbours[1]].get_VBO_color().get_g_color() +
                 list_of_VBO_copy[list_neighbours[2]].get_VBO_color().get_g_color() + list_of_VBO_copy[
                     list_neighbours[3]].get_VBO_color().get_g_color()) / 8.0
        center = list_of_VBO_copy[i].get_VBO_color().get_g_color() / 4.0
        self.VBO_coord[i].get_VBO_color().set_g_color(corners + sides + center)

    def smooth_r_color(self, i, list_neighbours, list_of_VBO_copy):
        corners = (list_of_VBO_copy[list_neighbours[7]].get_VBO_color().get_r_color() + list_of_VBO_copy[
            list_neighbours[6]].get_VBO_color().get_r_color() + list_of_VBO_copy[
                       list_neighbours[5]].get_VBO_color().get_r_color() +
                   list_of_VBO_copy[list_neighbours[4]].get_VBO_color().get_r_color()) / 16.0
        sides = (list_of_VBO_copy[list_neighbours[0]].get_VBO_color().get_r_color() + list_of_VBO_copy[
            list_neighbours[1]].get_VBO_color().get_r_color() +
                 list_of_VBO_copy[list_neighbours[2]].get_VBO_color().get_r_color() + list_of_VBO_copy[
                     list_neighbours[3]].get_VBO_color().get_r_color()) / 8.0
        center = list_of_VBO_copy[i].get_VBO_color().get_r_color() / 4.0
        self.VBO_coord[i].get_VBO_color().set_r_color(corners + sides + center)
