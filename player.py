import pygame
from leaves import screen
from pygame.math import Vector2



class Player:
    def __init__(self, pos: Vector2):
        self.pos = pos

    def draw(self):
        pygame.draw.rect(screen, (255,0,0), (self.pos.x-10, self.pos.y, 20, 20))

    def update(self, mouse_pos: Vector2):
        self.pos = mouse_pos
    
    