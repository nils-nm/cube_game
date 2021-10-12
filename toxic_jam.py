import random
import pygame
pygame.init()


def creatArray(x, y):
    return [[random.randint(0, 3) for i in range(x)] for j in range(y)]


def drawPlayer(pl, x_pl, y_pl):
    sc.blit(pl, (x_pl, y_pl))


def map_tiles(lis):
    for i in lis:
        for j in i:
            if j == 0:
                pass


tile = 16
w = 10
h = 10
x, y = 100, 100
sc = pygame.display.set_mode((w*tile, h*tile))
player = pygame.image.load('toxic_jam_player.png')
run = True
map_tiles(creatArray(w, h))

while run:
    sc.fill((25, 200, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    drawPlayer(player, x, y)

    pygame.display.update()


