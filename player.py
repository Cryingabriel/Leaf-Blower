import pygame
from leaves import screen
from pygame.math import Vector2
from random import randrange as rr


class Player:
    def __init__(self, pos: Vector2):
        self.pos = pos
        self.radius = 100

    def draw(self):
        pygame.draw.circle(screen,(rr(0,255), rr(0,255), rr(0,255)), (self.pos.x, self.pos.y), self.radius)
        pygame.draw.rect(screen, (rr(0,255), rr(0,255), rr(0,255)), (self.pos.x-10, self.pos.y-10, 20, 20))

    def update(self, mouse_pos: Vector2):
        self.pos = mouse_pos
