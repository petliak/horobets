import pygame
import random
run = True
blue=(100, 100, 100)
window = pygame.display.set_mode((1550 , 800))
def coloru():
    a = random.randint(0,255)
    s = random.randint(0, 255)
    d = random.randint(0, 255)
    return(a, s, d)
def coursore(size, window):
    coursore_color = coloru()
    position = pygame.mouse.get_pos()
    x = position[0]
    y = position[1]
    pygame.draw.polygon(window, coursore_color, ((x+60 , y+166),(x+60 , y+143),(x+77 , y+159),(x+69 , y+164),(x+75 , y+177),(x+69 , y+164)), 3)

    pygame.display.update()

while run:
    window.fill((0, 0, 0))

    coursore(50,window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
