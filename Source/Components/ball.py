import pygame
import sys
from config import gameWidth, gameHeight, ballHeight, ballWidth

class Ball:
    def __init__(self, posx, posy, image, speed):
        self.posx, self.posy = posx, posy
        self.speed = speed
        self.image = image
        self.offset = 0
        self.xFac, self.yFac = 1, 1

        self.ball = pygame.image.load(self.image)
    
    def display(self, screen):
        screen.blit(self.ball, (self.posx, self.posy))

    def update(self):
        self.posx += self.xFac * self.speed * self.offset
        self.posy += self.yFac * self.speed
        
        if self.posx <= 0:
            self.posx = 0
            self.xFac *= -1
        elif self.posx + ballWidth >= gameWidth:
            self.posx = gameWidth - ballWidth
            self.xFac *= -1
        if self.posy <= 0:
            self.posy = 0
            self.yFac *= -1
    
    def hit(self):
        self.yFac *= -1
   
    def hitSide(self):
        self.xFac *= -1

    def hitPlatform(self, offset):
        self.yFac *= -1
        self.offset = offset
        if(self.offset > 0 and self.xFac < 0): self.xFac *= -1
        elif(self.offset < 0): self.xFac = 1
    
    def increaseSpeed(self):
        if(self.speed < 10):
            self.speed += 1

    def getRect(self):
        return self.ball.get_rect(topleft=(self.posx, self.posy))