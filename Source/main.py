import sys
import pygame
from config import colorWhite, size, width, height, brickWidth, brickHeight, platformWidth, platformHeight, ballWidth, ballHeight, levels, bottomSpace, sideSpace
from Components.ball import Ball
from Components.brick import Brick
from Components.platform import Platform

def populateBricks(level):
    listOfBricks = []
    levelMap = levels[level]
    image = ""
    durability = 0

    for index, row in enumerate(levelMap):
        for colIndex, char in enumerate(row):
            if(char == '0'): continue
            x = sideSpace + (colIndex * brickWidth)
            y = index * brickHeight
            if(char == '1'):
                image = "Images/BrokenBrick.gif"
                durability = 1
            if(char == '2'):
                image = "Images/Brick.gif"
                durability = 2
            listOfBricks.append(Brick(x, y, image, durability, brickWidth, brickHeight))

    return listOfBricks

def checkPlatformCollision(platform, ball):
    ballLeft = ball.posx
    ballRight = ball.posx + ballWidth
    ballBottom = ball.posy + ballHeight
    platformLeft = platform.posx
    platformRight = platform.posx + platform.width
    platformTop = platform.posy

    if (ballRight >= platformLeft and ballLeft <= platformRight and ballBottom >= platformTop):
        ball.posy = platformTop - ballHeight
        platformCenter = platform.posx + (platformWidth / 2)
        ballsCenter = ball.posx + (ballWidth / 2)

        offset = (ballsCenter - platformCenter) / (platformWidth / 3)

        ball.hitPlatform(offset)
        ball.increaseSpeed()

def checkBrickCollision(brick, ball):
    ballLeft = ball.posx
    ballRight = ball.posx + ballWidth
    ballTop = ball.posy
    ballBottom = ball.posy + ballHeight
    brickLeft = brick.posx
    brickRight = brick.posx + brick.width
    brickTop = brick.posy
    brickBottom = brick.posy + brick.height

    if (ballRight >= brickLeft and ballLeft <= brickRight and ballBottom >= brickTop and ballTop <= brickBottom):
        overlapLeft = ballRight - brickLeft
        overlapRight = brickRight - ballLeft
        overlapTop = ballBottom - brickTop
        overlapBottom = brickBottom - ballTop
        minOverlap = min(overlapTop, overlapBottom, overlapLeft, overlapRight)
        if minOverlap == overlapLeft:
            ball.posx = brickLeft - ballWidth
            ball.hitSide()
        elif minOverlap == overlapRight:
            ball.posx = brickRight
            ball.hitSide()
        elif minOverlap == overlapTop:
            ball.posy = brickTop - ballHeight
            ball.hit()
        elif minOverlap == overlapBottom:
            ball.posy = brickBottom
            ball.hit()
        return True
    return False

def main():
    pygame.init()

    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Brick Breaker")

    clock = pygame.time.Clock()
    FPS = 30

    ball = Ball((width / 2) - (ballWidth / 2), (height - platformHeight - ballHeight), "Images/Ball.gif", 5)

    platform = Platform((width / 2) - (platformWidth / 2), height - platformHeight, 12, "Images/Platform.gif", platformWidth, platformHeight)
    platformXDir = 0
    level = 0
    lastLevel = 0
    listOfBricks = populateBricks(level)
    
    while True:
        if(lastLevel != level):
            listOfBricks = populateBricks(level)
            lastLevel += 1
            ball = Ball((width / 2) - (ballWidth / 2), (height - platformHeight - ballHeight), "Images/Ball.gif", 5)
            platform = Platform((width / 2) - (platformWidth / 2), height - platformHeight, 12, "Images/Platform.gif", platformWidth, platformHeight)

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

        checkPlatformCollision(platform, ball)
        for brick in listOfBricks:
            if(checkBrickCollision(brick, ball)):
                brick.hit()
                if brick.getDurability() <= 0:
                    listOfBricks.pop(listOfBricks.index(brick))
                if len(listOfBricks) <= 0:
                    level += 1
        
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