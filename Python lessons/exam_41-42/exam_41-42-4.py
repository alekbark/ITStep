import pygame
import random

# Инициализация
pygame.init()

WIDTH, HEIGHT = 600, 400
CELL = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")

clock = pygame.time.Clock()

# Цвета
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLACK = (0, 0, 0)

# Змейка
snake = [(100, 100), (80, 100), (60, 100)]
direction = (20, 0)

# Еда
food = (random.randrange(0, WIDTH, CELL), random.randrange(0, HEIGHT, CELL))


def draw():
    screen.fill(BLACK)

    # змейка
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, CELL, CELL))

    # еда
    pygame.draw.rect(screen, RED, (*food, CELL, CELL))

    pygame.display.flip()


def move_snake():
    global food

    head = snake[0]
    new_head = (head[0] + direction[0], head[1] + direction[1])

    snake.insert(0, new_head)

    if new_head == food:
        food = (random.randrange(0, WIDTH, CELL), random.randrange(0, HEIGHT, CELL))
    else:
        snake.pop()


def check_collision():
    head = snake[0]

    # стены
    if head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT:
        return True

    # сама в себя
    if head in snake[1:]:
        return True

    return False


# Игровой цикл
running = True

while running:
    clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction = (0, -CELL)
            elif event.key == pygame.K_DOWN:
                direction = (0, CELL)
            elif event.key == pygame.K_LEFT:
                direction = (-CELL, 0)
            elif event.key == pygame.K_RIGHT:
                direction = (CELL, 0)

    move_snake()

    if check_collision():
        print("Game Over")
        running = False

    draw()

pygame.quit()


