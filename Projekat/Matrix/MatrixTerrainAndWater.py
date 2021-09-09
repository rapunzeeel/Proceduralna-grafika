import copy
from GenerationHeight.ReadHeightMap import ReadHeightMap
from Matrix.Matrix import Matrix
from GenerationColor.ReadColorFile import read_color_file_height_map, read_color_file_wave


class MatrixTerrainAndWater(Matrix):
    def __init__(self, max_height):
        super().__init__()
        self.max_height = max_height
        self.color_terrain = read_color_file_height_map()
        self.color_water = read_color_file_wave()
        self.terrain = []
        self.list_of_VBO_copy = []

    def get_list_of_point(self):
        self.VBO_coord = super().create_matrix_height_map()
        self.add_z_coord_Height_map()
        return self.VBO_coord, self.terrain

    def add_z_coord_Height_map(self):
        self.VBO_scale_color_value = ReadHeightMap().read_RGB_color(0)
        self.VBO_scale_color_value_dudv_map = ReadHeightMap().read_RGB_color(1)
        for j in range(len(self.VBO_scale_color_value)):
            for i in range(len(self.VBO_coord)):
                if i == j:
                    if round(self.VBO_scale_color_value[j] * self.max_height, 2) > 50.5:
                        self.VBO_coord[i].set_z_coord(round(self.VBO_scale_color_value[j] * self.max_height, 2))
                        self.set_color_Height_map(i)
                        self.terrain.append(i)
                    else:
                        self.VBO_coord[i].set_z_coord(round(self.VBO_scale_color_value_dudv_map[j] * 0.75 + 50, 2))
                        self.set_color_DuDv_map(i)
        self.create_list_unallowed_water()
        self.create_list_allowed_water()
        self.smooth_neighbour_water()
        self.list_of_VBO_copy = copy.deepcopy(self.VBO_coord)
        for i in range(len(self.VBO_coord) - 61):
            if i not in self.list_unallowed and i not in self.terrain:
                self.smooth_color(i)

    def set_color_Height_map(self, index):
        for i in self.color_terrain:
            if 52.98 == (round(self.VBO_coord[index].get_z_coord(), 2)):
                self.VBO_coord[index].set_VBO_color(self.color_terrain[9.98])
            if self.VBO_coord[index].get_z_coord() >= (10.99 + 42.61):
                self.VBO_coord[index].set_VBO_color(self.color_terrain[10.56])
            if i + 43 == (round(self.VBO_coord[index].get_z_coord(), 2)):
                self.VBO_coord[index].set_VBO_color(self.color_terrain[i])
            if self.VBO_coord[index].get_z_coord() < (6 + 44.05):
                self.VBO_coord[index].set_VBO_color(self.color_terrain[5])

    def set_color_DuDv_map(self, index):
        for i in self.color_water:
            if self.VBO_coord[index].get_z_coord() < 50:
                self.VBO_coord[index].set_VBO_color(self.color_water[-3])
            if round(self.VBO_coord[index].get_z_coord(), 2) == i + 52:
                self.VBO_coord[index].set_VBO_color(self.color_water[i])
            if round(self.VBO_coord[index].get_z_coord(), 2) == i + 51:
                self.VBO_coord[index].set_VBO_color(self.color_water[i])

    def smooth_color(self, i):
        list_neighbours = [i + 1, i - 1, i + 60, i - 60, i + 61, i - 59, i + 59, i - 61]
        for n in list_neighbours:
            if n in self.terrain:
                return
        self.smooth_r_color(i, list_neighbours, self.list_of_VBO_copy)
        self.smooth_g_color(i, list_neighbours, self.list_of_VBO_copy)
        self.smooth_b_color(i, list_neighbours, self.list_of_VBO_copy)
