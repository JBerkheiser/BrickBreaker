import sys
import pygame
from config import colorWhite, screenSize, gameWidth, gameHeight, brickWidth, brickHeight, platformWidth, platformHeight, ballWidth, ballHeight, levels, bottomSpace, sideSpace, livesTextLocation, levelTextLocation, scoreTextLocation, livesNumberLocation, levelNumberLocation, scoreNumberLocation, gameOverMessageLocation, gameWonMessageLocation
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
                id = "brick"
                image = "Images/BrokenBrick.gif"
                durability = 1
            if(char == '2'):
                id = "brick"
                image = "Images/Brick.gif"
                durability = 2
            if(char == '4'):
                id = "metal"
                image = "Images/MetalBrick.gif"
                durability = 100
            listOfBricks.append(Brick(id, x, y, image, durability, brickWidth, brickHeight))

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
            if(overlapBottom <= 5):
                ball.hit()
        elif minOverlap == overlapRight:
            ball.posx = brickRight
            ball.hitSide()
            if(overlapBottom <= 5):
                ball.hit()
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

    screen = pygame.display.set_mode(screenSize)
    pygame.display.set_caption("Brick Breaker")

    clock = pygame.time.Clock()
    FPS = 30

    platformXDir = 0
    level = 1
    score = 0
    lives = 3
    lastLevel = 1
    lostLife = False
    gameOver = False
    gameWon = False

    background = pygame.image.load("Images/Background.jpg")
    border = pygame.image.load("Images/Border.gif")
    ball = Ball((gameWidth / 2) - (ballWidth / 2), (gameHeight - platformHeight - ballHeight), "Images/Ball.gif", 5)
    platform = Platform((gameWidth / 2) - (platformWidth / 2), gameHeight - platformHeight, 12, "Images/Platform.gif", platformWidth, platformHeight)
    listOfBricks = populateBricks(level)

    font = pygame.font.Font('freesansbold.ttf', 32)
    livesText = font.render('Lives:', True, (0, 0, 0), None)
    livesTextRect = livesText.get_rect()
    livesTextRect.center = livesTextLocation

    levelText = font.render('Level:', True, (0, 0, 0), None)
    levelTextRect = levelText.get_rect()
    levelTextRect.center = levelTextLocation

    scoreText = font.render('Score:', True, (0, 0, 0), None)
    scoreTextRect = scoreText.get_rect()
    scoreTextRect.center = scoreTextLocation
    
    while True:
        livesNumber = font.render(str(lives), True, (0, 0, 0), None)
        livesNumberRect = livesNumber.get_rect()
        livesNumberRect.center = livesNumberLocation
        levelNumber = font.render(str(level), True, (0, 0, 0), None)
        levelNumberRect = levelNumber.get_rect()
        levelNumberRect.center = levelNumberLocation
        scoreNumber = font.render(str(score), True, (0, 0, 0), None)
        scoreNumberRect = scoreNumber.get_rect()
        scoreNumberRect.center = scoreNumberLocation

        screen.fill((255, 255, 255))
        if(gameOver):
            screen.fill((255, 255, 255))
            gameOverMessage = font.render("YOU LOSE", True, (0, 0, 0), None)
            gameOverMessageRect = gameOverMessage.get_rect()
            gameOverMessageRect.center = gameOverMessageLocation
            screen.blit(gameOverMessage, gameOverMessageRect)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            continue

        if(gameWon):
            screen.fill((255, 255, 255))
            gameWonMessage = font.render("YOU WIN", True, (0, 0, 0), None)
            gameWonMessageRect = gameWonMessage.get_rect()
            gameWonMessageRect.center = gameWonMessageLocation
            screen.blit(gameWonMessage, gameWonMessageRect)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            continue

        if(lastLevel != level):
            listOfBricks = populateBricks(level)
            lastLevel += 1
            ball = Ball((gameWidth / 2) - (ballWidth / 2), (gameHeight - platformHeight - ballHeight), "Images/Ball.gif", 5)
            platform = Platform((gameWidth / 2) - (platformWidth / 2), gameHeight - platformHeight, 12, "Images/Platform.gif", platformWidth, platformHeight)
            lives = 3
        
        if(lostLife):
            lostLife = False
            ball = Ball((gameWidth / 2) - (ballWidth / 2), (gameHeight - platformHeight - ballHeight), "Images/Ball.gif", 5)
            platform = Platform((gameWidth / 2) - (platformWidth / 2), gameHeight - platformHeight, 12, "Images/Platform.gif", platformWidth, platformHeight)

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

        if(ball.posy + ballHeight >= gameHeight):
            lives -= 1
            if(lives <= 0): gameOver = True
            else: lostLife = True
        
        numberOfRegularBricks = 0
        for brick in listOfBricks:
            if(brick.id == "brick"):
                numberOfRegularBricks += 1
            if(checkBrickCollision(brick, ball)):
                brick.hit()
                score += 5
                if brick.getDurability() <= 0:
                    listOfBricks.pop(listOfBricks.index(brick))
        if numberOfRegularBricks == 0:
            if(level == 10):
                gameWon = True
            level += 1

        screen.blit(background, (0, 0))
        screen.blit(border, (gameWidth, 0))
        screen.blit(livesText, livesTextRect)
        screen.blit(livesNumber, livesNumberRect)
        screen.blit(levelText, levelTextRect)
        screen.blit(levelNumber, levelNumberRect)
        screen.blit(scoreText, scoreTextRect)
        screen.blit(scoreNumber, scoreNumberRect)
        
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