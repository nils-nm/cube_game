import pygame
pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption('cube_game')

x = 0
y = 0
width = 40
height = 60
vel = 5

run = True

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_d]:
        x -= vel
    if keys[pygame.K_a]:
        x += vel
    if keys[pygame.K_w]:
        y -= vel
    if keys[pygame.K_s]:
        y += vel

    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height), 1)
    pygame.display.update()

pygame.quit()