import pygame
import sys
from config import width, height, brickRectOffset

class Brick:
    def __init__(self, posx, posy, image, durability):
        self.posx, self.posy = posx, posy
        self.durability = durability
        self.image = image

        self.brick = pygame.image.load(self.image)
    
    def display(self, screen):
        if self.durability > 0:
            screen.blit(self.brick, (self.posx, self.posy))

    def hit(self):
        self.durability -= 1

    def getRect(self):
        brickRect = self.brick.get_rect(topleft=(self.posx, self.posy))
        brickRect.height -= brickRectOffset
        return brickRect
    
    def getDurability(self):
        return self.durability