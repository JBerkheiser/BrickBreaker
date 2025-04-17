import pygame
import sys
from config import width, height

class Ball:
    def __init__(self, posx, posy, image, speed):
        self.posx, self.posy = posx, posy
        self.speed = speed
        self.image = image
        self.xFac, self.yFac = 1, 1

        self.ball = pygame.image.load(self.image)
    
    def display(self, screen):
        screen.blit(self.ball, (self.posx, self.posy))

    def update(self):
        self.posx += self.xFac * self.speed
        self.posy += self.yFac * self.speed
        
        if self.posx <= 0 or self.posx + self.ball.get_width()>= width:
            self.xFac *= -1
        if self.posy <=0 or self.posy + self.ball.get_height() >= height:
            self.yFac *= -1

    def getRect(self):
        return self.ball.get_rect()