import pygame
import sys

pygame.init()
size = (640, 480)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Move the Square')

square = pygame.Rect(300, 220, 40, 40)
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        square.x -= 5
    if keys[pygame.K_RIGHT]:
        square.x += 5
    if keys[pygame.K_UP]:
        square.y -= 5
    if keys[pygame.K_DOWN]:
        square.y += 5
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), square)
    pygame.display.flip()
    clock.tick(60)
