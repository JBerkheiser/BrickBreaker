import sys
import pygame
from config import colorWhite, size, width, height, brickWidth, brickHeight, platformWidth, platformHeight, ballWidth, ballHeight
from Components.ball import Ball
from Components.brick import Brick
from Components.platform import Platform

def populateBricks(brickWidth, brickHeight, horizontalGap, verticalGap):
    listOfBricks = []

    for i in range(0, width, brickWidth + horizontalGap):
        for j in range(0, 200, brickHeight + verticalGap):
            listOfBricks.append(Brick(i, j, "Images/Brick.gif", 1))

    return listOfBricks

def collisionCheck(rect, ball):
    if pygame.Rect.colliderect(rect, ball):
        return True
    return False

def main():
    pygame.init()

    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Brick Breaker")

    clock = pygame.time.Clock()
    FPS = 30

    ball = Ball((width / 2) - (ballWidth / 2), (height - platformHeight - ballHeight), "Images/Ball.gif", 3)

    platform = Platform((width / 2) - (platformWidth / 2), height - platformHeight, 7, "Images/Platform.gif")
    platformXDir = 0
    
    horizontalGap, verticalGap = 20, 20
    listOfBricks = populateBricks(brickWidth, brickHeight, horizontalGap, verticalGap)
    
    while True:
        screen.fill(colorWhite)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    platformXDir = -1
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    platformXDir = 1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a or event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    platformXDir = 0

        if(collisionCheck(platform.getRect(), ball.getRect())):
            ball.hit()
        for brick in listOfBricks:
            if(collisionCheck(brick.getRect(), ball.getRect())):
                ball.hit()
                brick.hit()
                if brick.getDurability() <= 0:
                    listOfBricks.pop(listOfBricks.index(brick))
        
        platform.update(platformXDir)
        ball.update()

        ball.display(screen)
        platform.display(screen)
        for brick in listOfBricks:
            brick.display(screen)

        pygame.display.update()
        clock.tick(FPS)

if __name__ == "__main__":
    main()