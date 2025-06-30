import pygame
import random
# --- Налаштування ---
WIDTH, HEIGHT = 300, 600
ROWS, COLS = 20, 10
BLOCK_SIZE = 30


text_color = (250, 250 ,250)
text1_color = (250, 250 ,250)
text_x = 10
text_y = 10
text1_x = 10
text1_y = 10

window_x = 1550
window_y = 800
window = pygame.display.set_mode((window_x, window_y))

# Кольори RGB
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
COLORS = [
    (0, 255, 255),    # I
    (0, 0, 255),      # J
    (255, 165, 0),    # L
    (255, 255, 0),    # O
    (0, 255, 0),      # S
    (128, 0, 128),    # T
    (255, 0, 0)       # Z
]

# Матриці фігур
SHAPES = [
    [[1, 1, 1, 1]],                             # I
    [[1, 0, 0], [1, 1, 1]],                     # J
    [[0, 0, 1], [1, 1, 1]],                     # L
    [[1, 1], [1, 1]],                           # O
    [[0, 1, 1], [1, 1, 0]],                     # S
    [[0, 1, 0], [1, 1, 1]],                     # T
    [[1, 1, 0], [0, 1, 1]],                     # Z
]

# --- Pygame ---
pygame.init()
font1 = pygame.font.SysFont('Times New Roman',26)
pygame.mixer.music.load("music.mp3")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()

# --- Ігрове поле ---
grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]

# --- Клас фігури ---
class Tetromino:
    def __init__(self):
        self.shape = random.choice(SHAPES)
        self.color = random.choice(COLORS)
        self.x = COLS // 2 - len(self.shape[0]) // 2
        self.y = 0

    def draw(self):
        for i, row in enumerate(self.shape):
            for j, val in enumerate(row):
                if val:
                    pygame.draw.rect(
                        screen, self.color,
                        ((self.x + j) * BLOCK_SIZE,
                         (self.y + i) * BLOCK_SIZE,
                         BLOCK_SIZE, BLOCK_SIZE))

    def rotate(self):
        new_shape = [list(row) for row in zip(*self.shape[::-1])]
        old_shape = self.shape
        self.shape = new_shape
        if self.collision():
            self.shape = old_shape  # Відкат, якщо обертання неможливе

    def move_down(self):
        self.y += 1
        if self.collision():
            self.y -= 1
            lock_piece(self)
            return True
        return False

    def move_side(self, dx):
        self.x += dx
        if self.collision():
            self.x -= dx

    def collision(self):
        for i, row in enumerate(self.shape):
            for j, val in enumerate(row):
                if val:
                    new_x = self.x + j
                    new_y = self.y + i
                    if new_x < 0 or new_x >= COLS or new_y >= ROWS:
                        return True
                    if new_y >= 0 and grid[new_y][new_x]:
                        return True
        return False

    def game_over(self):
        row1 = grid[-1]
        row2 = grid[0]
        row3 = grid[2]
        row4 = grid[3]
        row5 = grid[4]
        row6 = grid[5]
        row7 = grid[6]
        row8 = grid[7]
        row9 = grid[8]
        row10 = grid[9]
        row11 = grid[10]
        row12 = grid[11]
        row13 = grid[12]
        row14 = grid[13]
        row15 = grid[14]
        row16 = grid[15]
        row17 = grid[16]
        row18 = grid[17]
        row19 = grid[18]
        row20 = grid[1]
        if (any(cell != 0 for cell in row1) and any(cell != 0 for cell in row2)
                and any(cell != 0 for cell in row3) and any(cell != 0 for cell in row4)
                and any(cell != 0 for cell in row5) and any(cell != 0 for cell in row6)
                and any(cell != 0 for cell in row7) and any(cell != 0 for cell in row8)
                and any(cell != 0 for cell in row9) and any(cell != 0 for cell in row10)
                and any(cell != 0 for cell in row11) and any(cell != 0 for cell in row12)
                and any(cell != 0 for cell in row13) and any(cell != 0 for cell in row14)
                and any(cell != 0 for cell in row15) and any(cell != 0 for cell in row16)
                and any(cell != 0 for cell in row17) and any(cell != 0 for cell in row18)
                and any(cell != 0 for cell in row19) and any(cell != 0 for cell in row20)):

            return False
        else:
            return True

# --- Допоміжні функції ---
def lock_piece(piece):
    for i, row in enumerate(piece.shape):
        for j, val in enumerate(row):
            if val:
                grid[piece.y + i][piece.x + j] = piece.color
    clear_rows()
    global current_piece
    current_piece = Tetromino()

def clear_rows():
    global grid
    new_grid = [row for row in grid if any(cell == 0 for cell in row)]
    cleared = ROWS - len(new_grid)
    while len(new_grid) < ROWS:
        new_grid.insert(0, [0 for _ in range(COLS)])
    grid = new_grid

def draw_grid():
    for y in range(ROWS):
        for x in range(COLS):
            if grid[y][x]:
                pygame.draw.rect(screen, grid[y][x],
                                 (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(screen, GRAY,
                             (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)

# --- Головна гра ---
current_piece = Tetromino()
fall_time = 0
fall_speed = 400
running = True
count = 0
run = True


while running:
    pygame.mixer.music.play(-1)
    while run:


        dt = clock.tick(50)  # Обмежуємо FPS до 60 і отримуємо час з минулого кадру
        fall_time += dt  # Збільшуємо таймер
        count += 1
        if count == 4200:
            fall_speed = 200
        elif count == 3600:
            fall_speed = 250
        elif count == 2400:
            fall_speed = 300
        elif count == 1200:
            fall_speed = 350
        elif count == 600:
            fall_speed = 400

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                running = False


            # Управління клавішами
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    current_piece.move_side(-1)
                elif event.key == pygame.K_d:
                    current_piece.move_side(1)
                elif event.key == pygame.K_SPACE:
                    current_piece.move_down()
                elif event.key == pygame.K_w:
                    current_piece.rotate()

        if fall_time > fall_speed:
            current_piece.move_down()
            fall_time = 0

        run = current_piece.game_over()
        screen.fill(BLACK)
        draw_grid()
        current_piece.draw()
        pygame.display.update()


    msg1 = "ha ha loh"
    text1 = font1.render(msg1, True, text1_color)
    window.blit(text1, (text1_x, text1_y))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    pygame.quit()