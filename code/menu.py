import pygame


pygame.init()
print('opening screen')
screen = pygame.display.set_mode((500,300))
running = True


# event to screen close
while running:
    #check for all event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


pygame.quit()


