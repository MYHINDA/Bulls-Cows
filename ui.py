import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))

background = (127, 127, 0)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        print(event)

    screen.fill((255, 255, 0))
    pygame.display.update()

pygame.quit()
