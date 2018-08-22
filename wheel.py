import random
import mglobals
import utils
from time import sleep
import pygame


class Wheel(object):
    def __init__(self):
        self.number = mglobals.ZERO
        self.image = None
        self.coord = (mglobals.ZERO, mglobals.ZERO)

    def spin(self):
        self.number = random.randrange(10, 11)      # broken random, always shows 10
        self.play_animation()
        self.show()

    def play_animation(self):
        mglobals.GD.blit(mglobals.WHEEL_ANIMATION_1, self.coord)
        pygame.display.update()
        sleep(0.3)
        mglobals.GD.blit(mglobals.WHEEL_ANIMATION_2, self.coord)
        pygame.display.update()
        sleep(0.3)
        mglobals.GD.blit(mglobals.WHEEL_ANIMATION_3, self.coord)
        pygame.display.update()
        sleep(0.3)

    def show(self):
        mglobals.GD.blit(mglobals.WHEEL_10, self.coord)
        pygame.display.update()
        sleep(1)

