import pygame

pygame.init()

window = pygame.display.set_mode((500,400))

while True:
    pygame.draw.rect(window, (255,0,0), (100,100,50,50))
    pygame.draw.rect(window, (0,255,0), (150,100,50,50))
    pygame.draw.rect(window, (0,0,255), (200,100,50,50))
    pygame.draw.circle(window, (255, 255, 0), (250,200), 20, 0)
    pygame.draw.ellipse(window, (0,0,255), (100, 200, 75, 100))
    pygame.display.update()