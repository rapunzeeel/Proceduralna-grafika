import random


class RandomValue(object):
    def __init__(self, max_terrain_height):
        self.max_terrain_height = max_terrain_height
        self.different = random.randint(0, 1000000)

    def add_z_value(self, x, y):
        return abs(self.get_smooth_Noise(x, y)) * self.max_terrain_height

    def get_smooth_Noise(self, x, y):
        corners = (self.get_noise(x - 1, y - 1) + self.get_noise(x + 1, y - 1) + self.get_noise(x - 1, y + 1) +
                   self.get_noise(x + 1, y + 1)) / 16.0
        sides = (self.get_noise(x - 1, y) + self.get_noise(x + 1, y) + self.get_noise(x, y - 1) +
                 self.get_noise(x, y + 1)) / 8.0
        center = self.get_noise(x, y) / 4.0
        return corners + sides + center

    def get_noise(self, x, y):
        random.seed(self.different + x * 50000 + y * 3500000004, 4)
        return random.uniform(-0.2, 0.2)
