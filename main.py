import pygame

pygame.init()

screen = pygame.display.set_mode((400,500))

#loop to run the game
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.flip
