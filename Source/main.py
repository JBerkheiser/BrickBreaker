import sys
import pygame
from config import colorWhite, size
from Components.ball import Ball


pygame.init()

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Brick Breaker")

clock = pygame.time.Clock()
FPS = 30
ball = Ball(100, 100, "Images/Ball.gif", 3)
while True:
    screen.fill(colorWhite)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    ball.update()
    ball.display(screen)

    pygame.display.update()
    clock.tick(FPS)