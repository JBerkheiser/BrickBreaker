import pygame
import sys
from config import width, height, brickRectOffset

class Brick:
    def __init__(self, posx, posy, image, durability, width, height):
        self.posx, self.posy = posx, posy
        self.durability = durability
        self.image = image
        self.width = width
        self.height = height

        self.brick = pygame.image.load(self.image)
    
    def display(self, screen):
        if self.durability > 0:
            screen.blit(self.brick, (self.posx, self.posy))

    def hit(self):
        self.durability -= 1
        if(self.durability == 2):
            self.image = "Images/Brick.gif"
        if(self.durability == 1):
            self.image = "Images/BrokenBrick.gif"

    def getRect(self):
        brickRect = self.brick.get_rect(topleft=(self.posx, self.posy))
        brickRect.height -= brickRectOffset
        return brickRect
    
    def getDurability(self):
        return self.durability