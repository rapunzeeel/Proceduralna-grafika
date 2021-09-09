import copy
import time
import pygame
from OpenGL.raw.GLU import gluPerspective
from pygame.locals import *
from GUI.MatrixGUI import create_edges, create_surfaces
from GUI.MatrixTerrainGUI import keyboard_commands, mouseMove
from Matrix.MatrixWater import *
from OpenGL.GL import *


class MatrixWaterGUI(object):
    def __init__(self, amplitude):
        self.amplitude = amplitude
        self.vertex = ()
        self.list_of_point = MatrixWater(amplitude).check_option_generation()
        for i in self.list_of_point:
            self.vertex += ((i.get_x_coord(), i.get_y_coord(), i.get_z_coord()),)
        self.edges = create_edges()
        self.surfaces = create_surfaces(self.list_of_point)

    def create_vertex(self):
        glBegin(GL_TRIANGLES)
        for surface in self.surfaces:
            for vertex in surface:
                color = self.list_of_point[vertex].get_VBO_color()
                color_tuple = (color.get_r_color() / 255, color.get_g_color() / 255, color.get_b_color() / 255)
                glColor3fv(color_tuple)
                glVertex3fv(self.vertex[vertex])
        glEnd()
        glBegin(GL_LINES)
        for edge in self.edges:
            for vertex in edge:
                glVertex3fv(self.vertex[vertex])
        glEnd()

    def draw_window(self):
        pygame.init()
        display = (600, 600)
        pygame.display.set_mode(display, DOUBLEBUF | OPENGL, RESIZABLE)
        pygame.display.set_caption("Voda")
        sur = pygame.image.load("Images/sea.png")
        pygame.display.set_icon(sur)
        gluPerspective(60, (display[0] / display[1]), 0.1, 100.0)
        glTranslatef(0.0, 0.0, -21)
        glRotated(290, 9, 0, 0)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.KEYDOWN:
                    keyboard_commands(event)
                # mouseMove(event)
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            self.translate_wave()
            pygame.display.flip()
            time.sleep(0.15)
            self.vertex = ()
            for i in self.list_of_point:
                self.vertex += ((i.get_x_coord(), i.get_y_coord(), i.get_z_coord()),)

    def translate_wave(self):
        list_of_VBO_copy = copy.deepcopy(self.list_of_point)
        for i in range(40):
            self.list_of_point[i].set_z_coord(list_of_VBO_copy[i + 1560].get_z_coord())
            self.list_of_point[i].set_VBO_color(list_of_VBO_copy[i + 1560].get_VBO_color())
        for i in range(40, 1600):
            self.list_of_point[i].set_z_coord(list_of_VBO_copy[i - 40].get_z_coord())
            self.list_of_point[i].set_VBO_color(list_of_VBO_copy[i - 40].get_VBO_color())
        self.create_vertex()
