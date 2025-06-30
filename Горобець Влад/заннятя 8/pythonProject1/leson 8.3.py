import pygame
import pygame as pg
pygame.init()
window=pygame.display.set_mode((1200,770))
green=(0,255,0)
yellow=(255, 255, 0)
magenta=(140,0,255)
black=(0,0,0)
hero = pg.image.load("images/1.png")
crown = pg.image.load("images/crown.png")
pok = pg.image.load("images/pok.png")
egg= pg.image.load("images/egg.png")
run = True
while run:
    window.fill(magenta)
    line = pygame.draw.line(window, black, (250, 100), (300, 300),(10))
    line = pygame.draw.line(window, black, (300, 300), (550, 300), (10))
    line = pygame.draw.line(window, black, (550, 300), (350, 500), (10))
    line = pygame.draw.line(window, black, (350, 500), (200, 650), (10))
    line = pygame.draw.line(window, black, (200, 650), (400, 700), (10))
    line = pygame.draw.line(window, black, (400, 700), (600, 670), (10))
    line = pygame.draw.line(window, black, (600, 670), (800, 720), (10))
    line = pygame.draw.line(window, black, (800, 720), (970, 670), (10))
    line = pygame.draw.line(window, black, (970, 670), (1150, 550), (10))
    line = pygame.draw.line(window, black, (1150, 550), (900, 480), (10))
    Circle = pygame.draw.circle(window,yellow, (250, 100), 30)
    Circle = pygame.draw.circle(window, yellow, (300, 300), 30)
    Circle = pygame.draw.circle(window, yellow, (550, 300), 30)
    Circle = pygame.draw.circle(window, yellow, (350, 500), 30)
    Circle = pygame.draw.circle(window, yellow, (200, 650), 30)
    Circle = pygame.draw.circle(window, yellow, (400, 700), 30)
    Circle = pygame.draw.circle(window, yellow, (600, 670), 30)
    Circle = pygame.draw.circle(window, yellow, (800, 720), 30)
    Circle = pygame.draw.circle(window, yellow, (970, 670), 30)
    Circle = pygame.draw.circle(window, yellow, (1150, 550), 30)
    Circle = pygame.draw.circle(window, yellow, (900, 480), 30)


    window.blit(hero,(230,50))
    window.blit(crown, (870, 460))
    window.blit(egg, (370, 680))
    window.blit(pok, (320, 480))
    window.blit(pok, (940, 650))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           run = False



