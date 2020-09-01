import pygame
import random
pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption('cube_game')


class Mob(object):
    def __init__(self, x, y, width, height, vel):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = vel


clock = pygame.time.Clock()
run = True
m = Mob(0, 100, 10, 10, 3)
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    m.x += 3
    if m.x >= 500:
        m.x = 0

    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 0, 0), (m.x, m.y, m.width, m.height))
    pygame.display.update()

clock.tick(60)
pygame.quit()
