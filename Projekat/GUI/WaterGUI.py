import pygame
from GUI.MatrixTerrainAndWaterGUI import MatrixTerrainAndWaterGUI
from GUI.MatrixWaterGUI import MatrixWaterGUI


class WaterGUI(object):
    def __init__(self):
        self.amplitude = 3.0
        pygame.init()
        self.display = (550, 700)
        screen = pygame.display.set_mode(self.display)
        pygame.display.set_caption("Voda")
        sur = pygame.image.load("Images/sea.png")
        pygame.display.set_icon(sur)
        self.create_window(screen)
        return

    def create_window(self, screen):
        pygame.font.init()
        font = pygame.font.SysFont('Gabriola', 35)
        text_surface = font.render('Izaberite nacin odabira visine:', True, (0, 0, 0))
        sea_photo = pygame.image.load("Images/talasi.png")
        up_photo = pygame.image.load("Images/gore.png")
        down_photo = pygame.image.load("Images/dole.png")

        button_terrain_water = pygame.Rect(130, 140, 330, 45)
        back_button_terrain_water = pygame.Rect(128, 138, 334, 49)
        terrain_water_text = font.render('Generisanje terena i vode', True, (0, 0, 0))

        button_random_gen = pygame.Rect(130, 235, 330, 45)
        back_button_random_gen = pygame.Rect(128, 233, 334, 49)
        random_gen_text = font.render('Sinusno generisanje', True, (0, 0, 0))

        button_user_choose = pygame.Rect(130, 330, 330, 45)
        back_button_user_choose = pygame.Rect(128, 328, 334, 49)
        user_choose_text = font.render('Unesite vrednosti', True, (0, 0, 0))

        while True:
            screen.fill((0, 204, 204), (0, 0, screen.get_width(), screen.get_height()))
            screen.blit(text_surface, (132, 50))
            screen.blit(sea_photo, (0, 0))
            pygame.draw.rect(screen, (0, 0, 0), back_button_random_gen)
            pygame.draw.rect(screen, (0, 204, 204), button_random_gen)
            screen.blit(random_gen_text, (170, 245))
            pygame.draw.rect(screen, (0, 0, 0), back_button_user_choose)
            pygame.draw.rect(screen, (0, 204, 204), button_user_choose)
            screen.blit(user_choose_text, (190, 340))
            pygame.draw.rect(screen, (0, 0, 0), back_button_terrain_water)
            pygame.draw.rect(screen, (0, 204, 204), button_terrain_water)
            screen.blit(terrain_water_text, (142, 149))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if button_terrain_water.collidepoint(mouse_pos):
                        pygame.quit()
                        MatrixTerrainAndWaterGUI(70).draw_window()
                        WaterGUI()
                        return
                    if button_random_gen.collidepoint(mouse_pos):
                        pygame.quit()
                        MatrixWaterGUI(4).draw_window()
                        WaterGUI()
                        return

                    if button_user_choose.collidepoint(mouse_pos):
                        while True:
                            new_font = pygame.font.SysFont('Gabriola', 30)

                            back_button_choose = pygame.Rect(130, 475, 300, 40)
                            pygame.draw.rect(screen, (0, 204, 204), back_button_choose)
                            choose_text = new_font.render("Unesite amplitudu talasa", True, (0, 0, 0))
                            screen.blit(choose_text, (134, 480))

                            button_up_amplitude = pygame.Rect(423, 430, 60, 36)
                            pygame.draw.rect(screen, (0, 204, 204), button_up_amplitude)
                            screen.blit(up_photo, (423, 430))

                            button_down_amplitude = pygame.Rect(425, 510, 60, 36)
                            pygame.draw.rect(screen, (0, 204, 204), button_down_amplitude)
                            screen.blit(down_photo, (425, 510))

                            button_choose = pygame.Rect(205, 552, 115, 36)
                            back_button_choose = pygame.Rect(203, 550, 119, 40)
                            pygame.draw.rect(screen, (0, 0, 0), back_button_choose)
                            pygame.draw.rect(screen, (0, 204, 204), button_choose)
                            choose_text = font.render('Izaberi', True, (0, 0, 0))
                            screen.blit(choose_text, (222, 560))

                            pygame.display.update()

                            for e in pygame.event.get():
                                if e.type == pygame.QUIT:
                                    pygame.quit()
                                    return
                                if e.type == pygame.MOUSEBUTTONDOWN:
                                    mouse_pos = e.pos

                                    if button_terrain_water.collidepoint(mouse_pos):
                                        pygame.quit()
                                        MatrixTerrainAndWaterGUI(70).draw_window()
                                        WaterGUI()
                                        return

                                    if button_random_gen.collidepoint(mouse_pos):
                                        pygame.quit()
                                        MatrixWaterGUI(4).draw_window()
                                        WaterGUI()
                                        return

                                    if button_up_amplitude.collidepoint(mouse_pos):
                                        if self.amplitude <= 4.9:
                                            self.amplitude += 0.1
                                    if button_down_amplitude.collidepoint(mouse_pos):
                                        if self.amplitude >= 0.1:
                                            self.amplitude -= 0.1
                                    if button_choose.collidepoint(mouse_pos):
                                        pygame.quit()
                                        MatrixWaterGUI(self.amplitude).draw_window()
                                        WaterGUI()
                                        return

                            screen.fill((0, 204, 204), (434, 472, screen.get_width(), 35))
                            amplitude = font.render("{:.1f}".format(self.amplitude), True, (0, 0, 0))
                            screen.blit(amplitude, (438, 475))
