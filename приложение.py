import pygame, sys, random
from pygame.math import Vector2

class SNAKE:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0, 0)
        self.new_block = False

        # Голова
        self.head_up = pygame.image.load("D:\\лабы питон\\приложение\\Graphics\\head_up.png").convert_alpha()
        self.head_down = pygame.image.load("D:\\лабы питон\\приложение\\Graphics\\head_down.png").convert_alpha()
        self.head_right = pygame.image.load("D:\\лабы питон\\приложение\\Graphics\\head_right.png").convert_alpha()
        self.head_left = pygame.image.load("D:\\лабы питон\\приложение\\Graphics\\head_left.png").convert_alpha()

        # Хвост
        self.tail_up = pygame.image.load("D:\\лабы питон\\приложение\\Graphics\\tail_up.png").convert_alpha()
        self.tail_down = pygame.image.load("D:\\лабы питон\\приложение\\Graphics\\tail_down.png").convert_alpha()
        self.tail_right = pygame.image.load("D:\\лабы питон\\приложение\\Graphics\\tail_right.png").convert_alpha()
        self.tail_left = pygame.image.load("D:\\лабы питон\\приложение\\Graphics\\tail_left.png").convert_alpha()

        # Тело
        self.body_vertical = pygame.image.load("D:\\лабы питон\\приложение\\Graphics\\body_vertical.png").convert_alpha()
        self.body_horizontal = pygame.image.load("D:\\лабы питон\\приложение\\Graphics\\body_horizontal.png").convert_alpha()

        # Повороты
        self.body_tr = pygame.image.load("D:\\лабы питон\\приложение\\Graphics\\body_tr.png").convert_alpha()
        self.body_tl = pygame.image.load("D:\\лабы питон\\приложение\\Graphics\\body_tl.png").convert_alpha()
        self.body_br = pygame.image.load("D:\\лабы питон\\приложение\\Graphics\\body_br.png").convert_alpha()
        self.body_bl = pygame.image.load("D:\\лабы питон\\приложение\\Graphics\\body_bl.png").convert_alpha()

        # Звук
        self.crunch_sound = pygame.mixer.Sound("D:\\лабы питон\\приложение\\Sound_crunch.wav")

    def play_crunch_sound(self):
        self.crunch_sound.play()

    def draw_snake(self):
        self.update_head_graphics()
        self.update_tail_graphics()
        for index, block in enumerate(self.body):#присваиваем каждому элементу индекс
            x_pos = int(block.x * cell_size) #переводим координаты в пиксели, умножим на размер одной клетки
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)#создаем прямоугольник, в котором потом будет картинка части змеи

            if index == 0:#если это голова рисуем self.head.
                screen.blit(self.head, block_rect)
            elif index == len(self.body) - 1:#если хвост — рисуем self.tail
                screen.blit(self.tail, block_rect)
            else:#обычные сегмент тела
                prev_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                if prev_block.x == next_block.x:#Если у обоих соседей одинаковая x-координата (они лежат строго над или под текущим блоком), значит текущий сегмент — вертикальный..
                    screen.blit(self.body_vertical, block_rect)
                elif prev_block.y == next_block.y:
                    screen.blit(self.body_horizontal, block_rect)
                else:
                    # угол поворота
                    if (prev_block.x, next_block.y) == (-1, -1) or (prev_block.y, next_block.x) == (-1, -1): #соседи слева + сверху
                        screen.blit(self.body_tl, block_rect)
                    elif (prev_block.x, next_block.y) == (-1, 1) or (prev_block.y, next_block.x) == (1, -1):#справа + сверху
                        screen.blit(self.body_bl, block_rect)
                    elif (prev_block.x, next_block.y) == (1, -1) or (prev_block.y, next_block.x) == (-1, 1):#слева + снизу
                        screen.blit(self.body_tr, block_rect)
                    else:
                        screen.blit(self.body_br, block_rect)#справа + снизу

    def update_head_graphics(self):#Считаем вектор между вторым сегментом (шея) и головой:
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1, 0): #этот вектор = (1, 0) значит шея находится на одну клетку правее головы.
            self.head = self.head_left
        elif head_relation == Vector2(-1, 0): #на одну клетку левее.
            self.head = self.head_right
        elif head_relation == Vector2(0, 1): #на 1 клетку вниз
            self.head = self.head_up
        elif head_relation == Vector2(0, -1): #на 1 клетку вверх.
            self.head = self.head_down

    def update_tail_graphics(self):#берём вектор от хвоста к предыдущему сегменту.Если этот вектор указывает вправо — значит шея находится вправо от хвоста, тогда хвост смотрит влево
        tail_relation = self.body[-2] - self.body[-1] #координаты шеи-координаты хвоста
        if tail_relation == Vector2(1, 0): #хвост расположен левее от шеи и смотрит влево
            self.tail = self.tail_left
        elif tail_relation == Vector2(-1, 0):#хвост расположен правее от шеи и смотрит вправо
            self.tail = self.tail_right
        elif tail_relation == Vector2(0, 1):#выше шеи и смотрит вверх
            self.tail = self.tail_up
        elif tail_relation == Vector2(0, -1):#хвост расположен ниже шеи и смотрит вниз
            self.tail = self.tail_down

    def move_snake(self):
        if self.new_block:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction) #вставить сегмент в начало списка
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]#длина остается преждней, но змейка сдвигается на новую клетку

    def add_block(self): #сигнал, что в следующий раз надо увеличить змейку
        self.new_block = True

    def reset(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0, 0)


class FRUIT:
    def __init__(self):
        self.randomize()

    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size),cell_size, cell_size)
        screen.blit(apple, fruit_rect)

    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)


class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()
            self.snake.play_crunch_sound()

        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomize()

    def check_fail(self):#поля
        head = self.snake.body[0]
        if not 0 <= head.x < cell_number or not 0 <= head.y < cell_number:
            self.game_over()
        for block in self.snake.body[1:]:#с телом
            if block == head:
                self.game_over()

    def game_over(self):
        self.snake.reset()

    def draw_grass(self):
        grass_color = (167, 209, 61)
        for row in range(cell_number):
            for col in range(cell_number):
                if (row + col) % 2 == 0:
                    grass_rect = pygame.Rect(col * cell_size,
                                             row * cell_size,
                                             cell_size, cell_size)
                    pygame.draw.rect(screen, grass_color, grass_rect)

    def draw_score(self):
        score_text = str(len(self.snake.body) - 3)#подсчет
        score_surface = game_font.render(score_text, True, (56, 74, 12))#цифра
        score_x = cell_size * cell_number - 60
        score_y = cell_size * cell_number - 40
        score_rect = score_surface.get_rect(center=(score_x, score_y))
        apple_rect = apple.get_rect(midright=(score_rect.left, score_rect.centery))
        bg_rect = pygame.Rect(apple_rect.left,
                              apple_rect.top,
                              apple_rect.width + score_rect.width + 6,
                              apple_rect.height)

        pygame.draw.rect(screen, (167, 209, 61), bg_rect)#фон
        screen.blit(score_surface, score_rect)
        screen.blit(apple, apple_rect)
        pygame.draw.rect(screen, (56, 74, 12), bg_rect, 2)#рамка



pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size,
                                  cell_number * cell_size))
clock = pygame.time.Clock()

# Яблоко и шрифт
apple = pygame.image.load("D:\\лабы питон\\приложение\\Graphics\\apple.png").convert_alpha()
game_font = pygame.font.Font("D:\\лабы питон\\приложение\\PoetsenOne-Regular.ttf", 25)


SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

main_game = MAIN()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and main_game.snake.direction.y != 1:
                main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_RIGHT and main_game.snake.direction.x != -1:
                main_game.snake.direction = Vector2(1, 0)
            if event.key == pygame.K_DOWN and main_game.snake.direction.y != -1:
                main_game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_LEFT and main_game.snake.direction.x != 1:
                main_game.snake.direction = Vector2(-1, 0)

    screen.fill((175, 215, 70))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)
