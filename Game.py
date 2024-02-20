import pygame
from leaves import gleaves
from leaves import Goldleaves
from player import Player
from leaves import screen
from leaves import SCREEN_SIZE
import roomba
import blower
import apple
from pygame.math import Vector2
from pygame.rect import Rect
import random
from leaves import RainbowLeaves
from random import randrange as rr

# config:
FRAMERATE = 60

# pygame init:
pygame.init()
pygame.display.set_caption("Leaf blower")
my_font = pygame.font.SysFont('Comic Sans MS', 30)


leavesbag = 0


# definitions:


def main():
    # game setup:
    clock = pygame.time.Clock()


    leaves = []
    for i in range(30):
        leaves.append(gleaves(random.randrange(10, 1100), random.randrange(10, 700)))
        leaves.append(Goldleaves(random.randrange(10, 1100), random.randrange(10, 700)))
        leaves.append(RainbowLeaves(random.randrange(10, 1100), random.randrange(10, 700)))

    player = Player(Vector2(0, 0))

    # main loop:
    running = True
    while running:
        delta = clock.tick(FRAMERATE) / 1000

        # input:
        mouse_pos = Vector2(pygame.mouse.get_pos())
        player.update(mouse_pos)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for j in range(len(leaves)):
            leaves[j].update(leavesbag)
            leaves[j].applyphysics(mouse_pos)

        # draw:
        screen.fill("#000000")
        
        player.draw()
        for i in range (len(leaves)):
            leaves[i].draw()

        text_surface1 = my_font.render(str(leavesbag), 1 ,(rr(0,255), rr(0,255), rr(0,255)))

        screen.blit(text_surface1, (0,0))

        pygame.display.flip()


if __name__ == "__main__":
    main()