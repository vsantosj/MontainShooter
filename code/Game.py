import pygame

from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((600, 480))

    def run(self):
        # chamar  aa classe menu
        while True:
            menu = Menu(self.window)
            menu.run()

        #    for event in pygame.event.get():
        #        if event.type == pygame.QUIT:
    #             pygame.quit()
