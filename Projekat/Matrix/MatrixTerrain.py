import copy
from GenerationHeight.CubicSpline import *
import numpy as nmp
from GenerationHeight.RadnomValue import RandomValue
from GenerationHeight.ReadHeightMap import ReadHeightMap
from Matrix.Matrix import Matrix
from GenerationColor.ReadColorFile import read_color_file, read_color_file_height_map


class MatrixTerrain(Matrix):
    def __init__(self, parameter, max_height):
        super().__init__()
        self.parameter = parameter
        self.max_height = max_height
        self.color = {}
        self.list_of_VBO_copy = []

    def check_option_generation(self):
        if self.parameter == 0:
            self.color = read_color_file_height_map()
            self.VBO_coord = super().create_matrix_height_map()
            self.add_z_coord_Height_map()
        else:
            self.color = read_color_file()
            self.VBO_coord = super().create_matrix()
            self.add_z_coord_Perlin_Noise()
        return self.VBO_coord

    def add_z_coord_Height_map(self):
        self.VBO_scale_color_value = ReadHeightMap().read_RGB_color(0)
        for j in range(len(self.VBO_scale_color_value)):
            for i in range(len(self.VBO_coord)):
                if i == j:
                    self.VBO_coord[i].set_z_coord(round(self.VBO_scale_color_value[j] * self.max_height, 2))
        for i in range(len(self.VBO_coord)):
            self.set_color_Height_map(i)

    def add_z_coord_Perlin_Noise(self):
        list_z_value = []
        for y in range(0, 40):
            for x in range(0, 40):
                list_z_value.append(RandomValue(self.max_height).add_z_value(x, y))
        for i in range(len(self.VBO_coord)):
            self.VBO_coord[i].set_z_coord(list_z_value[i])
        self.terrain_spline()
        self.create_list_unallowed()
        self.create_list_allowed()
        self.smooth_neighbour_z_coord()
        self.smooth_neighbour_z_coord()
        for i in range(len(self.VBO_coord)):
            self.set_color_Perlin_Noise(i)
        self.list_of_VBO_copy = copy.deepcopy(self.VBO_coord)
        for i in range(len(self.VBO_coord)):
            if i not in self.list_unallowed:
                self.smooth_color(i)

    def set_color_Perlin_Noise(self, index):
        for i in self.color:
            if self.VBO_coord[index].get_z_coord() > 10.99:
                self.VBO_coord[index].set_VBO_color(self.color[10.99])
            if self.VBO_coord[index].get_z_coord() < 7.01:
                self.VBO_coord[index].set_VBO_color(self.color[7.01])
            if i == round(self.VBO_coord[index].get_z_coord(), 2):
                self.VBO_coord[index].set_VBO_color(self.color[i])

    def smooth_color(self, i):
        list_neighbours = [i + 1, i - 1, i + 40, i - 40, i + 41, i - 39, i + 39, i - 41]
        self.smooth_r_color(i, list_neighbours, self.list_of_VBO_copy)
        self.smooth_g_color(i, list_neighbours, self.list_of_VBO_copy)
        self.smooth_b_color(i, list_neighbours, self.list_of_VBO_copy)

    def set_color_Height_map(self, index):
        for i in self.color:
            if self.VBO_coord[index].get_z_coord() >= (10.99 + 41.98):
                self.VBO_coord[index].set_VBO_color(self.color[10.66])
            if self.VBO_coord[index].get_z_coord() < (6 + 43):
                self.VBO_coord[index].set_VBO_color(self.color[6])
            if i + 42 == (round(self.VBO_coord[index].get_z_coord(), 2)):
                self.VBO_coord[index].set_VBO_color(self.color[i])

    def terrain_spline(self):
        map_yz_coord = self.spline_y_coord()
        map_xz_coord = self.spline_x_coord()
        for i in map_yz_coord:
            for j in map_xz_coord:
                if i == j:
                    if map_yz_coord[i] + map_xz_coord[j] > 10:
                        self.VBO_coord[i].set_z_coord((map_yz_coord[i] + map_xz_coord[j] - 5))
                    else:
                        if map_yz_coord[i] + map_xz_coord[j] < 4:
                            self.VBO_coord[i].set_z_coord((map_yz_coord[i] + map_xz_coord[j] + 6))
                        else:
                            self.VBO_coord[i].set_z_coord((map_yz_coord[i] + map_xz_coord[j] + 4))

    def spline_x_coord(self):
        map_xz_coord = {}
        for j in range(0, 40):
            x = []
            z = []
            for i in range(0, 1600, 40):
                x.append(self.VBO_coord[i + j].get_x_coord())
                z.append(self.VBO_coord[i + j].get_z_coord())
            spline = CubicSpline(x, z)
            rx = nmp.arange(-20, 19, 0.01)
            rz = []
            for i in rx:
                rz.append(spline.calculate(i))
            for i in range(0, 1600, 40):
                map_xz_coord[i + j] = rz[i]
        return map_xz_coord

    def spline_y_coord(self):
        map_yz_coord = {}
        for j in range(0, 1599, 40):
            y = []
            z = []
            for i in range(j, j + 40):
                y.append(self.VBO_coord[i].get_y_coord())
                z.append(self.VBO_coord[i].get_z_coord())
            spline = CubicSpline(y, z)
            ry = nmp.arange(-20, 19, 0.01)
            rz = []
            for i in ry:
                rz.append(spline.calculate(i))
            for i in range(0, 40):
                map_yz_coord[i + j] = rz[i]
        return map_yz_coord
