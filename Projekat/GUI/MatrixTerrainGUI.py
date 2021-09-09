import math
import pygame
from OpenGL.raw.GLU import gluPerspective
from pygame.locals import *
from GUI.MatrixGUI import create_edges, create_surfaces, create_edges_height_map, create_surfaces_height_map
from Matrix.MatrixTerrain import *
from OpenGL.GL import *

lastPosX = 0
lastPosY = 0
zoomScale = 1.0
dataL = 0
xRot = 0
yRot = 0
zRot = 0


class MatrixTerrainGUI(object):
    def __init__(self, parameter, max_height):
        self.parameter = parameter
        self.list_of_point = MatrixTerrain(parameter, max_height).check_option_generation()
        self.vertex = ()
        if parameter == 0:
            self.edges = create_edges_height_map()
            for i in self.list_of_point:
                self.vertex += ((i.get_x_coord(), i.get_y_coord(), i.get_z_coord()),)
            self.surfaces = create_surfaces_height_map(self.list_of_point)
        else:
            self.edges = create_edges()
            for i in self.list_of_point:
                self.vertex += ((i.get_x_coord(), i.get_y_coord(), i.get_z_coord()),)
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
                glColor3fv((128 / 255, 142 / 255, 67 / 255))
                glVertex3fv(self.vertex[vertex])
        glEnd()

    def create_terrain_without_color(self):
        glBegin(GL_LINES)
        for edge in self.edges:
            for vertex in edge:
                glVertex3fv(self.vertex[vertex])
        glEnd()

    def draw_window(self):
        pygame.init()
        display = (1000, 800)
        pygame.display.set_mode(display, DOUBLEBUF | OPENGL, RESIZABLE)
        pygame.display.set_caption("Teren")
        sur = pygame.image.load("Images/mountain.png")
        pygame.display.set_icon(sur)

        if self.parameter == 0:
            gluPerspective(60, (display[0] / display[1]), 0.1, 100.0)
            glTranslatef(0, -25, -70)
            glRotated(327, 7, 0, 0)
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return
                    if event.type == pygame.KEYDOWN:
                        keyboard_commands(event)
                glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
                self.create_vertex()
                pygame.display.flip()
        else:
            gluPerspective(60, (display[0] / display[1]), 0.1, 100.0)
            glTranslatef(0.0, 0.0, -40)
            glRotated(330, 7, 0, 0)
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return
                    if event.type == pygame.KEYDOWN:
                        keyboard_commands(event)
                    # mouseMove(event)
                glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
                if self.parameter == 1:
                    self.create_vertex()
                else:
                    self.create_terrain_without_color()
                pygame.display.flip()


def mouseMove(event):
    global lastPosX, lastPosY, zoomScale, xRot, yRot, zRot

    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 4:  # mis ka dole
        glScaled(1.05, 1.05, 1.05)
    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 5:  # mis ka gore
        glScaled(0.95, 0.95, 0.95)

    if event.type == pygame.MOUSEMOTION:
        x, y = event.pos
        dx = x - lastPosX
        dy = y - lastPosY

        mouseState = pygame.mouse.get_pressed()
        if mouseState[0]:
            modelView = (GLfloat * 900)()
            mvm = glGetFloatv(GL_MODELVIEW_MATRIX, modelView)
            temp = (GLfloat * 3)()
            temp[0] = modelView[0] * dy + modelView[1] * dx
            temp[1] = modelView[4] * dy + modelView[5] * dx
            temp[2] = modelView[8] * dy + modelView[9] * dx
            norm_xy = math.sqrt(temp[0] * temp[0] + temp[1] * temp[1] + temp[2] * temp[2])
            glRotatef(math.sqrt(dx * dx + dy * dy), temp[0] / norm_xy, temp[1] / norm_xy, temp[2] / norm_xy)

        lastPosX = x
        lastPosY = y


def keyboard_commands(event):
    if event.key == pygame.K_LEFT:
        glTranslatef(-1, 0, 0)
    if event.key == pygame.K_RIGHT:
        glTranslatef(1, 0, 0)
    if event.key == pygame.K_UP:
        glTranslatef(0, 1, 0)
    if event.key == pygame.K_DOWN:
        glTranslatef(0, -1, 0)
    if event.key == pygame.K_s:  # priblizava
        glTranslatef(0, 0, 1)
    if event.key == pygame.K_w:  # odaljava
        glTranslatef(0, 0, -1)
    if event.key == pygame.K_a:  # rotiranje ulevo
        glRotated(5, 0, 0, 1)
    if event.key == pygame.K_d:  # rotiranje udesno
        glRotated(5, 0, 0, -1)
    if event.key == pygame.K_r:  # rotiranje ka gore
        glRotated(2, 1, 0, 0)
    if event.key == pygame.K_f:  # rotiranje ka dole
        glRotated(2, -1, 0, 0)
