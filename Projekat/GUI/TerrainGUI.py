from GUI.MatrixTerrainGUI import *
from PIL import Image


class TerrainGUI(object):
    def __init__(self):
        self.image = Image.open("Images/planine.png")
        self.value = 40
        pygame.init()
        self.display = (800, 400)
        screen = pygame.display.set_mode(self.display)
        pygame.display.set_caption("Teren")
        sur = pygame.image.load("Images/mountain.png")
        pygame.display.set_icon(sur)
        self.create_window(screen)
        return

    def create_window(self, screen):
        pygame.font.init()
        font = pygame.font.SysFont('Gabriola', 35)
        text_surface = font.render('Izaberite nacin odabira visine:', True, (0, 0, 0))
        mountain_photo = pygame.image.load("Images/planine.png")
        up_photo = pygame.image.load("Images/gore.png")
        down_photo = pygame.image.load("Images/dole.png")
        button_height_map = pygame.Rect(75, 140, 210, 45)
        back_button_height_map = pygame.Rect(73, 138, 214, 49)
        height_map_text = font.render('Height mape', True, (0, 0, 0))
        button_random_color = pygame.Rect(75, 235, 210, 45)
        back_button_random_color = pygame.Rect(73, 233, 214, 49)
        random_color_text = font.render('Random visina', True, (0, 0, 0))
        button_random_without_color = pygame.Rect(75, 325, 210, 50)
        back_button_random_without_color = pygame.Rect(73, 323, 214, 54)
        random_without_color_text = font.render('bez boje', True, (0, 0, 0))
        button_choose_value = pygame.Rect(402, 140, 340, 45)
        back_button_choose_value = pygame.Rect(400, 138, 344, 49)
        choose_value_text = font.render('Unesite maksimalnu visinu', True, (0, 0, 0))
        while True:
            screen.fill((0, 204, 204), (0, 0, screen.get_width(), screen.get_height()))
            screen.blit(text_surface, (220, 50))
            screen.blit(mountain_photo, (0, 0))
            pygame.draw.rect(screen, (0, 0, 0), back_button_height_map)
            pygame.draw.rect(screen, (0, 204, 204), button_height_map)
            screen.blit(height_map_text, (105, 149))
            pygame.draw.rect(screen, (0, 0, 0), back_button_random_color)
            pygame.draw.rect(screen, (0, 204, 204), button_random_color)
            screen.blit(random_color_text, (90, 245))
            pygame.draw.rect(screen, (0, 0, 0), back_button_random_without_color)
            pygame.draw.rect(screen, (0, 204, 204), button_random_without_color)
            screen.blit(random_color_text, (85, 327))
            screen.blit(random_without_color_text, (125, 350))
            pygame.draw.rect(screen, (0, 0, 0), back_button_choose_value)
            pygame.draw.rect(screen, (0, 204, 204), button_choose_value)
            screen.blit(choose_value_text, (415, 152))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if button_height_map.collidepoint(mouse_pos):
                        pygame.quit()
                        MatrixTerrainGUI(0, 70).draw_window()
                        TerrainGUI()
                        return
                    if button_random_color.collidepoint(mouse_pos):
                        pygame.quit()
                        MatrixTerrainGUI(1, 70).draw_window()
                        TerrainGUI()
                        return
                    if button_random_without_color.collidepoint(mouse_pos):
                        pygame.quit()
                        MatrixTerrainGUI(2, 70).draw_window()
                        TerrainGUI()
                        return

                    if button_choose_value.collidepoint(mouse_pos):

                        while True:
                            pygame.display.flip()
                            button_up = pygame.Rect(520, 200, 60, 36)
                            pygame.draw.rect(screen, (0, 204, 204), button_up)
                            screen.blit(up_photo, (520, 200))

                            button_down = pygame.Rect(520, 270, 60, 36)
                            pygame.draw.rect(screen, (0, 204, 204), button_down)
                            screen.blit(down_photo, (520, 270))

                            button_choose = pygame.Rect(492, 330, 115, 36)
                            back_button_choose = pygame.Rect(490, 328, 119, 40)
                            choose_text = font.render('Izaberi', True, (0, 0, 0))
                            pygame.draw.rect(screen, (0, 0, 0), back_button_choose)
                            pygame.draw.rect(screen, (0, 204, 204), button_choose)
                            screen.blit(choose_text, (510, 337))
                            pygame.display.flip()
                            for e in pygame.event.get():
                                if e.type == pygame.QUIT:
                                    pygame.quit()
                                    return
                                if e.type == pygame.MOUSEBUTTONDOWN:
                                    mouse_pos = e.pos
                                    if button_height_map.collidepoint(mouse_pos):
                                        pygame.quit()
                                        MatrixTerrainGUI(0, 70).draw_window()
                                        TerrainGUI()
                                        return
                                    if button_random_color.collidepoint(mouse_pos):
                                        pygame.quit()
                                        MatrixTerrainGUI(1, 70).draw_window()
                                        TerrainGUI()
                                        return
                                    if button_random_without_color.collidepoint(mouse_pos):
                                        pygame.quit()
                                        MatrixTerrainGUI(2, 70).draw_window()
                                        TerrainGUI()
                                        return

                                    if button_up.collidepoint(mouse_pos):
                                        if self.value <= 89:
                                            self.value += 1
                                    if button_down.collidepoint(mouse_pos):
                                        if self.value >= 41:
                                            self.value -= 1
                                    if button_choose.collidepoint(mouse_pos):
                                        pygame.quit()
                                        MatrixTerrainGUI(1, self.value).draw_window()
                                        TerrainGUI()
                                        return
                            screen.fill((0, 204, 204), (530, 235, screen.get_width(), 35))
                            text_val = font.render("{0}".format(str(self.value)), True, (0, 0, 0))
                            screen.blit(text_val, (533, 237))
