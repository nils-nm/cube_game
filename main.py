import pygame
import random

pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption('cube_game')


class Mob(object):
    def __init__(self, x, y, width, height, vel, radius):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = vel
        self.radius = radius


clock = pygame.time.Clock()
run = True
NoRot = True
GoDown = False
m = Mob(0, 100, 10, 10, 3, 10)
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if NoRot is True:
        m.x += 1
    if GoDown is True:
        m.y += 1
    if m.y == 505:
        m.x = -5
        m.y = 100
        NoRot = True
        GoDown = False
    if m.x >= 100:
        NoRot = False
        GoDown = True

    win.fill((0, 0, 0))
    pygame.draw.circle(win, (255, 0, 0), (m.x, m.y), m.radius)
    pygame.display.update()

clock.tick(40)
pygame.quit()
