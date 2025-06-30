import pygame
import random
import pygame as pg

run = True
window = pygame.display.set_mode((1530, 780))
cursor_picture = pg.image.load("images\pokemon_ball.png")
black = (0, 0, 0)
white = (255, 255, 255)
pokemon = pg.image.load("images\jigglypuff.png")
pokemon_x = 10
pokemon_y = 200
pokemony = pg.image.load("images\pokecoin.png")
pokemony_x = 100
pokemony_y = 600
ct = pg.image.load("images\zubat.png")
ct_x = 20
ct_y = 100
fon = pg.image.load("images\zubat.png")
iteration_count = 0
iteration_count1 = 0
iteration_count2 = 0
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 26)
hit = 0
lost = 0

def cursor_draw(window, picture):
    position = pygame.mouse.get_pos()
    x = position[0]
    y = position[1]
    pygame.mouse.set_visible(False)
    window.blit(picture, (x - 40, y - 40))

while run:
    iteration_count += 1
    iteration_count1 += 1
    iteration_count2 += 1
    massage = "Score: " + str(hit) + " / " + str(lost)
    text = my_font.render(massage, True, white)
    if iteration_count == 1300:
        pokemon_x = random.randint(0, 520)
        pokemon_y = random.randint(0, 520)
        iteration_count = 0
        lost += 1
    if iteration_count1 == 1100:
        pokemony_x = random.randint(0, 520)
        pokemony_y = random.randint(0, 520)
        iteration_count1 = 0
        lost += 1
    if iteration_count2 == 1500:
        ct_x = random.randint(0, 520)
        ct_y = random.randint(0, 520)
        iteration_count2 = 0


    window.fill(black)
    window.blit(text, (10, 550))
    window.blit(pokemon, (pokemon_x, pokemon_y))
    window.blit(pokemony, (pokemony_x, pokemony_y))
    window.blit(ct, (ct_x, ct_y))
    cursor_draw(window, cursor_picture)
    pg.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            Pos = pygame.mouse.get_pos()
            xPos = Pos[0]
            yPos = Pos[1]
            if (xPos > pokemon_x) and (xPos < pokemon_x + 70) and (yPos > pokemon_y) and (yPos < pokemon_y + 70):
                pokemon_x = random.randint(0,1520)
                pokemon_y = random.randint(0,520)
                iteration_count = 0
                hit += 1
            if (xPos > pokemony_x) and (xPos < pokemony_x + 70) and (yPos > pokemony_y) and (yPos < pokemony_y + 70):
                pokemony_x = random.randint(0,1520)
                pokemony_y = random.randint(0,800)
                iteration_count = 0
                hit += 2
            if (xPos > ct_x) and (xPos < ct_x + 100) and (yPos > ct_y ) and (yPos < ct_y + 100):
                ct_x = random.randint(0,1520)
                ct_y = random.randint(0,800)
                iteration_count = 0
                hit -= 2