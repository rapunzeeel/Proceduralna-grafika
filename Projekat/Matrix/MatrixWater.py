from Matrix.Matrix import Matrix
import math
import random
from GenerationColor.ReadColorFile import read_color_file_wave


class MatrixWater(Matrix):
    def __init__(self, amplitude):
        super().__init__()
        self.amplitude = amplitude
        self.color = read_color_file_wave()

    def check_option_generation(self):
        self.VBO_coord = super().create_matrix()
        self.add_z_coord_sin()
        self.create_list_unallowed()
        self.create_list_allowed()
        self.smooth_neighbour_z_coord()
        self.smooth_neighbour_z_coord()
        return self.VBO_coord

    def set_color(self, index):
        for i in self.color:
            if self.VBO_coord[index].get_z_coord() < -3:
                self.VBO_coord[index].set_VBO_color(self.color[-3])
            if abs(int(self.VBO_coord[index].get_z_coord())) == 0 and abs(
                    round(self.VBO_coord[index].get_z_coord(), 2)) == i:
                self.VBO_coord[index].set_VBO_color(self.color[i])
            if round(self.VBO_coord[index].get_z_coord(), 2) == i:
                self.VBO_coord[index].set_VBO_color(self.color[i])
            if self.VBO_coord[index].get_z_coord() > 2.20:
                self.VBO_coord[index].set_VBO_color(self.color[2.20])

    def add_z_coord_sin(self):
        for i in range(len(self.VBO_coord)):
            random_number = random.randint(0, 15)
            if random_number <= 3:
                self.VBO_coord[i].set_z_coord(
                    self.amplitude * math.sin(self.VBO_coord[i].get_x_coord()) / 32)
            elif 3 < random_number <= 6:
                self.VBO_coord[i].set_z_coord(
                    self.amplitude * math.sin(self.VBO_coord[i].get_x_coord()) / 8)
            elif 6 < random_number <= 9:
                self.VBO_coord[i].set_z_coord(
                    self.amplitude * math.sin(self.VBO_coord[i].get_x_coord()) / 4)
            elif 12 < random_number <= 15:
                self.VBO_coord[i].set_z_coord(
                    self.amplitude * math.sin(self.VBO_coord[i].get_x_coord()) / 2)
            else:
                self.VBO_coord[i].set_z_coord(self.amplitude * math.sin(self.VBO_coord[i].get_x_coord()))
        for i in range(len(self.VBO_coord)):
            self.set_color(i)
