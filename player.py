import pygame
from leaves import screen
from pygame.math import Vector2


class Player:
    def __init__(self, pos: Vector2):
        self.pos = pos
        self.radius = 100

    def draw(self):
        pygame.draw.circle(screen,(0,255,0), (self.pos.x, self.pos.y), self.radius)
        pygame.draw.rect(screen, (255,0,0), (self.pos.x-10, self.pos.y, 20, 20))

    def update(self, mouse_pos: Vector2):
        self.pos = mouse_pos
    
    def collision(self):
        pass