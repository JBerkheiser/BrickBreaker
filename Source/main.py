import sys, pygame

pygame.init()

size = width, height = 600, 500
speed = [2, 2]
colorBlack = (0, 0, 0)
colorWhite = (255, 255, 255)
colorRed = (0, 255, 0)
colorGreen = (255, 0, 0)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Brick Breaker")

clock = pygame.time.Clock()
FPS = 30

ball = pygame.image.load("Images/Ball.gif")
ballrect = ball.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(colorWhite)
    screen.blit(ball, ballrect)
    pygame.display.flip()