import pygame
import pygame as pg
run = True
hero = pg.image.load("zubat.png")
window = pygame.display.set_mode((1550, 800))

def img(window,picture):
    position = pygame.mouse.get_pos()
    x = position[0]
    y = position[1]
    #pygame.draw.polygon(window, coursore_color, (
   # (x + 60, y + 166), (x + 60, y + 143), (x + 77, y + 159), (x + 69, y + 164), (x + 75, y + 177), (x + 69, y + 164)),3)
    #window.fill((0, 0, 0))
    window.blit(picture,(x-50,y-50))
    pygame.display.update()


while run:
    window.fill((0, 0, 0))
    img(window,hero)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False