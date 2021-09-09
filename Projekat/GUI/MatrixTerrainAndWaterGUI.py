import pygame
from OpenGL.raw.GLU import gluPerspective
from pygame.locals import *
from GUI.MatrixGUI import create_surfaces_height_map, create_edges_height_map
from GUI.MatrixTerrainGUI import keyboard_commands, mouseMove
from Matrix.MatrixTerrainAndWater import MatrixTerrainAndWater
from OpenGL.GL import *


class MatrixTerrainAndWaterGUI(object):
    def __init__(self, max_height):
        self.max_height = max_height
        self.vertex = ()
        self.list_of_point, self.terrain = MatrixTerrainAndWater(max_height).get_list_of_point()
        for i in self.list_of_point:
            self.vertex += ((i.get_x_coord(), i.get_y_coord(), i.get_z_coord()),)
        self.edges = create_edges_height_map()
        self.surfaces = create_surfaces_height_map(self.list_of_point)

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
                if vertex in self.terrain:
                    glColor3fv((128 / 255, 142 / 255, 67 / 255))
                else:
                    glColor3fv((60 / 255, 92 / 255, 126 / 255))
                glVertex3fv(self.vertex[vertex])
        glEnd()

    def draw_window(self):
        pygame.init()
        display = (1000, 800)
        pygame.display.set_mode(display, DOUBLEBUF | OPENGL, RESIZABLE)
        pygame.display.set_caption("Teren i voda")
        sur = pygame.image.load("Images/first.png")
        pygame.display.set_icon(sur)
        gluPerspective(60, (display[0] / display[1]), 0.1, 100.0)
        glTranslatef(0, -25, -70)
        glRotated(325, 7, 0, 0)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.KEYDOWN:
                    keyboard_commands(event)
                # mouseMove(event)
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            self.create_vertex()
            pygame.display.flip()
