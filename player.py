import pygame
from Game import screen
from pygame.math import Vector2



class Player:
    def __init__(self,xpos, ypos):
        self.pos = Vector2(xpos, ypos)

    
    def draw(self):
        pygame.draw.rect(screen, (0,0,0), (self.pos.x, self.pos.y, 20, 20))