from numpy import linalg
import numpy as nmp


class CubicSpline:

    def __init__(self, list_of_first_coord, list_of_second_coord):
        self.list_of_first_coord = list_of_first_coord
        self.list_of_second_coord = list_of_second_coord
        self.b, self.c, self.d = [], [], []
        self.set_values()

    def set_values(self):
        ones = nmp.diff(self.list_of_first_coord)
        A = self.calculate_matrix_A(ones)
        b = self.calculate_list_b(ones)
        self.c = linalg.solve(A, b)
        i = 0
        while i < (len(self.list_of_first_coord) - 1):
            self.d.append((self.c[i + 1] - self.c[i]) / (3.0 * ones[i]))
            self.b.append((self.list_of_second_coord[i + 1] - self.list_of_second_coord[i]) / ones[i] - ones[i] * \
                          (self.c[i + 1] + 2.0 * self.c[i]) / 3.0)
            i += 1

    def calculate(self, value):
        if value < self.list_of_first_coord[0] or value > self.list_of_first_coord[-1]:
            return None
        i = self.list_of_first_coord.index(int(value))
        dx = value - self.list_of_first_coord[i]
        result = self.list_of_second_coord[i] + self.b[i] * dx + self.c[i] * dx ** 2.0 + self.d[i] * dx ** 3.0
        return result

    def calculate_matrix_A(self, ones):
        A = nmp.zeros((len(self.list_of_first_coord), len(self.list_of_first_coord)))
        A[0, 0] = 1.0
        i = 0
        while i < (len(self.list_of_first_coord) - 1):
            if i != (len(self.list_of_first_coord) - 2):
                A[i + 1, i + 1] = 2.0 * (ones[i] + ones[i + 1])
            A[i + 1, i] = ones[i]
            A[i, i + 1] = ones[i]
            i += 1
        A[0, 1] = 0.0
        A[len(self.list_of_first_coord) - 1, len(self.list_of_first_coord) - 2] = 0.0
        A[len(self.list_of_first_coord) - 1, len(self.list_of_first_coord) - 1] = 1.0
        return A

    def calculate_list_b(self, ones):
        b = nmp.zeros(len(self.list_of_first_coord))
        for i in range(len(self.list_of_first_coord) - 2):
            b[i + 1] = 3.0 * (self.list_of_second_coord[i + 2] - self.list_of_second_coord[i + 1]) / \
                       ones[i + 1] - 3.0 * (self.list_of_second_coord[i + 1] - self.list_of_second_coord[i]) / ones[i]
        return b
