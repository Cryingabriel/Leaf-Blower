import pygame
import random
from pygame.math import Vector2
import math
from random import randrange as rr

SCREEN_SIZE = Vector2(1200, 800)
screen = pygame.display.set_mode(SCREEN_SIZE)

class gleaves:
    def __init__ (self, xpos, ypos):
        self.tempPlayerRadius = 100
        self.isAlive = True
        self.xVel: int = 0
        self.yVel: int = 0
        self.pos = pygame.Rect(xpos, ypos, 20, 20)

    def hitbox(self, screen):
        if self.isAlive == True:
            pygame.draw.rect(screen, (10, 255, 20), (self.pos))

    def draw(self):
        if self.isAlive == True:
            pygame.draw.circle(screen, (10, 255, 20), (self.pos.x, self.pos.y), 10)
    def update(self, leavesb):
        self.pos.x += self.xVel
        self.pos.y += self.yVel
        if self.pos.x > 1200 or self.pos.x < 0:
            self.dead()
            leavesb+= 1
        if self.pos.y > 800 or self.pos.y < 0:
            self.dead()
            leavesb+= 1
        return leavesb
    

    def applyphysics(self, Player: Vector2):
        leafDistance = math.sqrt((self.pos.x - Player.x) ** 2 + (self.pos.y - Player.y) ** 2)
        if leafDistance <= self.tempPlayerRadius:
            #blowDirection = ((self.pos - Player.pos).normalize() if self.pos != Player.pos else Vector2(0, 0))
            self.xVel = -1
            self.yVel = -1
        else:
            self.xVel = 0
            self.yVel = 0
    
    def dead(self):
        self.isAlive = False
        self.pos = pygame.Rect(-1000, -1000, 20, 20)
        self.xVel = 0
        self.yVel = 0

    def respawn(self):
        self.pos.x = random.randint(50, 1200-50)
        self.pos.y = random.randint(50, 800-50)
        self.xVel: int = 0
        self.yVel: int = 0


class Goldleaves(gleaves):
    def __init__(self, xpos, ypos):
        super().__init__(xpos, ypos)
    def draw(self):
        if self.isAlive == True:
            pygame.draw.circle(screen, (255, 255, 0), (self.pos.x, self.pos.y), 10)


class RainbowLeaves(gleaves):
    def __init__(self, xpos, ypos):
        super().__init__(xpos, ypos)
    def draw(self):
        if self.isAlive == True:
            pygame.draw.circle(screen, (rr(0,255), rr(0,255), rr(0,255)), (self.pos.x, self.pos.y), 10)