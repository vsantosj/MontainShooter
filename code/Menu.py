import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, COLOR_ORANGE, COLOR_WHITE, MENU_OPTION


class Menu:

    # construtor
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/menu.png')  # load image
        self.rect = self.surf.get_rect(left=0, top=0)  # create reactangle to get image, default 0,0,0, init top left

    def run(self):
        # load sound
        pygame.mixer.music.load('./asset/menu.mp3')
        pygame.mixer.music.play(-1)  # play sound (-1) alltime sound

        while True:
            self.window.blit(source=self.surf, dest=self.rect)  # update image method run - Draw
            self.menu_text(50, "Montain", COLOR_ORANGE, ((WIN_WIDTH / 2), 70))
            self.menu_text(50, "Shooter", COLOR_ORANGE, ((WIN_WIDTH / 2), 110))  # draw text

            for i in range(len(MENU_OPTION)):
                self.menu_text(20, MENU_OPTION[i], COLOR_WHITE, ((WIN_WIDTH / 2), 200 + 25 * i))

            pygame.display.flip()  # update window

            # Check events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # closet window
                    print('Closeting.....')
                    quit()  # end pygame

    # method text
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucid SansTypewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
