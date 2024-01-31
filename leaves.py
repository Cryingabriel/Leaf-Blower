import pygame
from pygame.math import Vector2

SCREEN_SIZE = Vector2(1200, 800)
screen = pygame.display.set_mode(SCREEN_SIZE)

class gleaves:
    def __init__ (self, xpos, ypos):
        self.isAlive = True
        self.xVel: int = 0
        self.yVel: int = 0
        self.pos = pygame.Rect( xpos, ypos, 20, 20)

    def hitbox(self, screen):
        if self.isAlive == True:
            pygame.draw.rect(screen, (10, 255, 20), (self.pos))

    def draw(self):
        if self.isAlive == True:
            pygame.draw.circle(screen, (10, 255, 20), (self.pos.x, self.pos.y), 10)
    def movement(self):
        self.pos.x += self.xVel
        self.pos.y += self.yVel

    def collide(self):
        if self.pos.x > 1200 or self.pos.x < 0:
            self.dead()
        if self.pos.y > 800 or self.pos.y < 0:
            self.dead()
    
    def dead(self):
        self.isAlive = False
        self.xVel = 0
        self.yVel = 0


class Goldleaves(gleaves):
    def __init__(self, xpos, ypos):
        super().__init__(xpos, ypos)
    def draw(self):
        if self.isAlive == True:
            pygame.draw.circle(screen, (255, 255, 0), (self.pos.x, self.pos.y), 10)