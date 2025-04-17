import sys
import pygame
from config import colorWhite, size, width, height, brickWidth, brickHeight
from Components.ball import Ball
from Components.brick import Brick

def populateBricks(brickWidth, brickHeight, horizontalGap, verticalGap):
    listOfBricks = []

    for i in range(0, width, brickWidth + horizontalGap):
        for j in range(0, 200, brickHeight + verticalGap):
            listOfBricks.append(Brick(i, j, "Images/Brick.gif", 1))

    return listOfBricks

def main():
    pygame.init()

    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Brick Breaker")

    clock = pygame.time.Clock()
    FPS = 30
    ball = Ball(300, 450, "Images/Ball.gif", 3)

    horizontalGap, verticalGap = 20, 20
    listOfBricks = populateBricks(brickWidth, brickHeight, horizontalGap, verticalGap)
    while True:
        screen.fill(colorWhite)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()


        ball.update()

        for brick in listOfBricks:
            if brick.getDurability() <= 0:
                listOfBricks.pop(listOfBricks.index(brick))

        ball.display(screen)
        for brick in listOfBricks:
            brick.display(screen)

        pygame.display.update()
        clock.tick(FPS)

if __name__ == "__main__":
    main()