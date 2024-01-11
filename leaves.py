import pygame
from Game import screen
from Game import playerPos
from pygame.math import Vector2

class green_leaves:
    def __init__ (self, xpos, ypos):
        self.isAlive = False
        self.xVel: int = 0
        self.yVel: int = 0
        self.pos = pygame.Rect(xpos, ypos, 20, 20)


    def hitbox(self, screen):
        if self.isAlive == True:
            pygame.draw.rect(screen, (10, 255, 20), (self.pos))

    def draw(self, screen):
        if self.isAlive == True:
            pygame.draw.circle(screen, (10, 255, 20), (self.pos.x, self.pos.y), 10)
    def movement(self):
        self.pos.x += self.xVel
        self.pos.y += self.yVel

    def collide(self, playerPos):
        pass
        
    
    def dead(self):
        self.isAlive = False
        self.xVel = 0
        self.yVel = 0

class Golden_Leaves(green_leaves):
    def __init__(self, xpos, ypos):
        super().__init__(xpos, ypos)