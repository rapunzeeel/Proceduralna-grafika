from GUI.WaterGUI import *
from GUI.TerrainGUI import *


class MainUserGUI(object):

    def __init__(self):
        pygame.init()
        display = (600, 200)
        screen = pygame.display.set_mode(display)
        pygame.display.set_caption("Proceduralna grafika")
        sur = pygame.image.load("Images/first.png")
        pygame.display.set_icon(sur)
        pygame.display.update()
        self.create_window(screen)
        return

    def create_window(self, screen):
        pygame.font.init()
        my_font = pygame.font.SysFont('Gabriola', 30)
        text_surface = my_font.render('Sta zelite da generisete?', True, (0, 0, 0))
        procedural_photo = pygame.image.load("Images/reka.png")
        button_terrain = pygame.Rect(140, 100, 170, 40)
        back_button1 = pygame.Rect(138, 98, 174, 44)
        font = pygame.font.SysFont('Gabriola', 35)
        terrain_text = font.render('Teren', True, (0, 0, 0))
        button_water = pygame.Rect(350, 100, 170, 40)
        back_button2 = pygame.Rect(348, 98, 174, 44)
        water_text = font.render('Voda', True, (0, 0, 0))
        while True:
            screen.fill((0, 204, 204))
            screen.blit(text_surface, (190, 30))
            screen.blit(procedural_photo, (0, 0))
            pygame.draw.rect(screen, (0, 0, 0), back_button1)
            pygame.draw.rect(screen, (0, 204, 204), button_terrain)
            screen.blit(terrain_text, (190, 110))
            pygame.draw.rect(screen, (0, 0, 0), back_button2)
            pygame.draw.rect(screen, (0, 204, 204), button_water)
            screen.blit(water_text, (402, 110))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if button_terrain.collidepoint(mouse_pos):
                        pygame.quit()
                        TerrainGUI()
                        MainUserGUI()
                        return
                    if button_water.collidepoint(mouse_pos):
                        pygame.quit()
                        WaterGUI()
                        MainUserGUI()
                        return
