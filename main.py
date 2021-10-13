import pygame
from copy import deepcopy
from random import choice, randrange
import math
import time

w, h = 10, 15
tile = 45
game_res = w * tile, h * tile
res = 750, 840

sc = pygame.display.set_mode(res)
win = pygame.Surface(game_res)
clock = pygame.time.Clock()

bg1 = pygame.image.load('bg1.png').convert()
bg2 = pygame.image.load('bg2.png').convert()

grid = [pygame.Rect(x * tile, y * tile, tile, tile) for x in range(w) for y in range(h)]

figures_pos = [[(-1, 0), (-2, 0), (0, 0), (1, 0)],
               [(0, -1), (-1, -1), (-1, 0), (0, 0)],
               [(-1, 0), (-1, 1), (0, 0), (0, -1)],
               [(0, 0), (-1, 0), (0, 1), (-1, -1)],
               [(0, 0), (0, -1), (0, 1), (-1, -1)],
               [(0, 0), (0, -1), (0, 1), (-1, -1)],
               [(0, 0), (0, -1), (0, 1), (-1, 0)]]

figures = [[pygame.Rect(x + w // 2, y + 1, 1, 1) for x, y in fig_pos] for fig_pos in figures_pos]
figure_rect = pygame.Rect(0, 0, tile - 2, tile - 2)
field = [[0 for i in range(w)] for j in range(h)]

anim_count, anim_speed, anim_limit = 0, 60, 2000
figure = deepcopy(choice(figures))

get_color = lambda: (0, randrange(30, 256), randrange(30, 256))
color = get_color()


def check_borders():
    if figure[i].x < 0 or figure[i].x > w - 1:
        return False
    elif figure[i].y > h - 1 or field[figure[i].y][figure[i].x]:
        return False
    return True


while True:

    dx, rotate = 0, False
    sc.blit(bg1, (0, 0))
    sc.blit(win, (20, 20))
    win.blit(bg2, (0, 0))
    # control
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -1
            elif event.key == pygame.K_RIGHT:
                dx = 1
            elif event.key == pygame.K_DOWN:
                anim_limit = 10
            elif event.key == pygame.K_UP:
                rotate = True
    # move x
    figure_old = deepcopy(figure)
    for i in range(4):
        figure[i].x += dx
        if not check_borders():
            figure = deepcopy(figure_old)
            break
    # move y
    anim_count += anim_speed
    if anim_count > anim_limit:
        anim_count = 0
        figure_old = deepcopy(figure)
        for i in range(4):
            figure[i].y += 1
            if not check_borders():
                for i in range(4):
                    field[figure_old[i].y][figure_old[i].x] = color
                color = get_color()
                figure = deepcopy(choice(figures))
                anim_limit = 2000
                break
    # rotate
    center = figure[0]
    figure_old = deepcopy(figure)
    if rotate:
        for i in range(4):
            x = figure[i].y - center.y
            y = figure[i].x - center.x
            figure[i].x = center.x - x
            figure[i].y = center.y + y
            if not check_borders():
                figure = deepcopy(figure_old)
                break
    # check lines
    line = h - 1
    for row in range(h - 1, -1, -1):
        count = 0
        for i in range(w):
            if field[row][i]:
                count += 1
            field[line][i] = field[row][i]
        if count < w:
            line -= 1

    # draw grid
    [pygame.draw.rect(win, (40, 40, 40), i_rect, 1) for i_rect in grid]
    # draw figure
    for i in range(4):
        figure_rect.x = figure[i].x * tile
        figure_rect.y = figure[i].y * tile
        pygame.draw.rect(win, color, figure_rect)
    # draw field
    for y, raw in enumerate(field):
        for x, col in enumerate(raw):
            if col:
                figure_rect.x, figure_rect.y = x * tile, y * tile
                pygame.draw.rect(win, col, figure_rect)
    pygame.display.update()
    clock.tick(60)

