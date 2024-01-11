import pygame
from leaves import green_leaves
from player import Player
import roomba
import blower
import apple
from pygame.math import Vector2
from pygame.rect import Rect
import random


# config:
FRAMERATE = 60
SCREEN_SIZE = Vector2(1200, 800)


# pygame init:
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Leaf blower")



# definitions:

leaves = []
for i in range(1):
    leaves.append(green_leaves(random.randrange(10, 1100), random.randrange(10, 700)))

Mousepos = (0,0)
playerPos = Vector2(Mousepos[0], Mousepos[1])
player = Player(playerPos.x, playerPos.y)

def main():
    # game setup:
    clock = pygame.time.Clock()

    # main loop:
    running = True
    while running:
        delta = clock.tick(FRAMERATE) / 1000

        # input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # draw:
        screen.fill("#000000")

        pygame.display.flip()

if __name__ == "__main__":
    main()