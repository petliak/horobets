import pygame
import random
import pygame as pg

run = True
runig = True
window_x = 1550
window_y = 800

window = pygame.display.set_mode((window_x, window_y))
background = pg.image.load("images/background.png")
diamond1 = pg.image.load("images/9.png")
diamond2 = pg.image.load("images/8.png")
diamond3 = pg.image.load("images/7.png")
pygame.font.init()
font = pygame.font.SysFont('Times New Roman',26)
text_color = (0, 0 ,0)
back_color = (100, 0 , 100)
hero = pg.image.load("images/bym.png")
hero_x = 500
hero_y = 380
text_x = 10
text_y = 10

font1 = pygame.font.SysFont('Times New Roman',70)
text1_color = (0, 0 ,0)
text1_x = 550
text1_y = 380


def draw_back(window, picture):
    window.blit(picture, (0,0))

class wizard:
    speed = 10
    x = 10
    y =600
    width=138
    height = 150
    main_pic = pg.image.load("images/1_IDLE_000.png")
    left_pic = pg.image.load("images/3_RUN_000_l.png")
    right_pic = pg.image.load("images/3_RUN_001.png")
    def stand(self,window):
        window.blit(self.main_pic, (self.x, self.y))
    def move_left(self):
        if self.x - self.speed >= 0:
            self.x = self.x - self.speed
        else:
            self.x = 0
        window.blit(self.left_pic, (self.x, self.y))
    def move_right(self,width):
        if self.x + self.speed <= width - self.width :
            self.x = self.x + self.speed
        else:
            self.x = width - self.width
        self.x = self.x + self.speed
        window.blit(self.right_pic, (self.x, self.y))
    def jump_u(self,window):
        self.y= self.y-50
        window.blit(self.main_pic, (self.x, self.y))
    def jump_d(self,window):
        self.y= self.y+50
        window.blit(self.main_pic, (self.x, self.y))
    def wiz_poz(self):
        return (self.x, self.y)

    def wiz_size(self):
        return (self.width, self.height)

class copy_wizard(wizard):
    width = 120
    height = 145
    main_pic = pg.image.load("images/b1.png")
    left_pic = pg.image.load("images/bl.png")
    right_pic = pg.image.load("images/br.png")
    jump_pic = pg.image.load("images/bu.png")
    def jump_new (self,window):
        window.blit(self.jump_pic, (self.x, self.y-100))




class diamond:
    x = 0
    y = 0
    picture = 0
    speed = 0
    def __init__(self,picture):
        self.x = random.randint(0, 1500)
        self.speed = random.randint(4,7 )
        self.picture = picture
    def show(self,window):
        window.blit(self.picture,(self.x,self.y))
    def fall(self):
        self.y = self.y + self.speed
    def dim_poz(self):
        return (self.x,self.y)

class diamonds:
    diamonds_images = [pg.image.load("images/9.png"), pg.image.load("images/8.png"), pg.image.load("images/7.png"),pg.image.load("images/11.png"), pg.image.load("images/12.png")]
    diamonds_list = []
    def __init__(self):
        pass
    def add(self):
        self.diamonds_list.append(diamond(self.diamonds_images[random.randint(0,4)]))
    def draw(self,window):
        for x in self.diamonds_list:
            x.show(window)
    def fall(self):
        for x in self.diamonds_list:
            x.fall()
    def delete(self,x ,y,hight,width):
        count1 = 0
        count2 = 0
        count3 = 0
        for element in self.diamonds_list:
            position = element.dim_poz()
            dx = position[0]
            dy = position[1]
            if dx >x and dx<x+width and dy>y and dy<y+hight:
                del self.diamonds_list[count3]
                count1 +=1
            elif position[1] > 800:
                del self.diamonds_list[count3]
                count2 +=1
        count3 +=1
        return (count1,count2)

class bom:
    x = 0
    y = 0
    picture = 0
    speed = 0
    def __init__(self,picture):
        self.x = random.randint(0, 1500)
        self.speed = random.randint(3,5 )
        self.picture = picture
    def show(self,window):
        window.blit(self.picture,(self.x,self.y))
    def fall(self):
        self.y = self.y + self.speed
    def dim_poz(self):
        return (self.x,self.y)

class bomb:
    bomb_images = [pg.image.load("images/666.png"), pg.image.load("images/666.png")]
    bomb_list = []

    def __init__(self):
        pass
    def add(self):
        self.bomb_list.append(diamond(self.bomb_images[random.randint(0,1)]))
    def draw(self,window):
        for x in self.bomb_list:
            x.show(window)
    def fall(self):
        for x in self.bomb_list:
            x.fall()
    def delete(self,x ,y,hight,width,hero_x,hero_y):
        count1 = 0
        count2 = 0
        count3 = 0

        for element in self.bomb_list:
            position = element.dim_poz()
            dx = position[0]
            dy = position[1]
            if dx >x and dx<x+width and dy>y and dy<y+hight:
                del self.bomb_list[count3]
                window.blit(hero, (hero_x,hero_y))
                run = False
                return run
            elif position[1] > 800:
                del self.bomb_list[count3]
                count2 -=1
        count3 +=1
        return (count1,count2)

#diamo1 = diamond(diamond1)
#diamo2 = diamond(diamond2)
#diamo3 = diamond(diamond3)
hero_direction = 'stop'
wizard1 = wizard()
copy_wizard1 = copy_wizard()
diamonds_in_game = diamonds()
diamonds_in_game.add()

bomb_in_game = bomb()
bomb_in_game.add()

count_diamond = 0
count_bomb = 0
count1 = 0
count2 = 0
while run:
    while runig:

        if count_diamond == 50:
            diamonds_in_game.add()
            count_diamond = 0

        if count_bomb == 50:
            bomb_in_game.add()
            count_bomb = 0

        draw_back(window,background)
        diamonds_in_game.draw(window)
        bomb_in_game.draw(window)
        #diamo1.show(window)
        #diamo2.show(window)
        #diamo3.show(window)
       # wizard1.stand(window)
        #pg.display.update()4

        msg = "Результат: "+str(count1) +"/" + str(count2)
        text = font.render(msg,True,text_color,back_color)
        window.blit(text,(text_x,text_y))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                runig = False
                break
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                #wizard1.move_left()
                hero_direction = 'left'
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                #wizard1.move_right(window_x)
                hero_direction = 'right'
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                copy_wizard1.jump_u(window)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                copy_wizard1.jump_d(window)
            elif event.type == pygame.KEYUP:
                hero_direction = 'stop'
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                hero_direction = 'up'
        if hero_direction == 'left':
            copy_wizard1.move_left()
        elif hero_direction == 'right':
            copy_wizard1.move_right(window_x)
        elif hero_direction == 'up':
            copy_wizard1.jump_new(window)
        else:
            copy_wizard1.stand(window)
        pg.display.update()
        count_diamond+=1
        wizpoz = copy_wizard1.wiz_poz()
        wizsize = copy_wizard1.wiz_size()

        rezult = diamonds_in_game.delete(wizpoz[0],wizpoz[1],wizsize[0],wizsize[1])
        rez = bomb_in_game.delete(wizpoz[0],wizpoz[1],wizsize[0],wizsize[1],hero_x,hero_y)
        pg.display.update()

        count1 = count1 + rezult[0] + rez[0]
        count2 = count2 + rezult[1] + rez[1]
        diamonds_in_game.fall()
        bomb_in_game.fall()
        if count2 == 15:
            runig = False
    pg.display.update()
    msg1 = "ha ha loh"
    text1 = font1.render(msg1, True, text1_color)
    window.blit(text1, (text1_x, text1_y))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


        #diamo1.fall()
        #diamo2.fall()
        #diamo3.fall()
