import pygame
import sys
from config import gameWidth, platformWidth, platformHeight

class Platform:
    def __init__(self, posx, posy, speed, image, width, height):
        self.posx, self.posy = posx, posy
        self.speed = speed
        self.image = image
        self.width = width
        self.height = height

        self.platformRect = pygame.Rect(self.posx, self.posy, platformWidth, platformHeight)
        self.platform = pygame.image.load(self.image)

    def update(self, xDir):
        self.posx += self.speed * xDir
        if self.posx <= 0:
            self.posx = 0
        elif self.posx + platformWidth >= gameWidth:
            self.posx = gameWidth - platformWidth
        self.platformRect = pygame.Rect(self.posx, self.posy, platformWidth, platformHeight)
    
    def display(self, screen):
        screen.blit(self.platform, (self.posx, self.posy))

    def getRect(self):
        return self.platform.get_rect(topleft=(self.posx, self.posy))