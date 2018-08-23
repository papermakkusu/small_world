#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Maksim Vasilev'


import random
import constants
import utils


class Dice(object):
    def __init__(self):
        self.number = constants.ZERO
        self.image = constants.WHEEL_10
        self.coord = (constants.ZERO, constants.ZERO)
        self.animation_sequence = (constants.WHEEL_ANIMATION_1,
                                   constants.WHEEL_ANIMATION_2,
                                   constants.WHEEL_ANIMATION_3)

    def throw(self, count=None):

        self.number = count if count is not None else random.randrange(10, 11)  # broken random, always shows 10

        # TODO change dice roll result image here
        # self.image =
        self.play_animation()
        self.show()

    def play_animation(self):
        utils.play_animation(0.3, 1, self.animation_sequence)

    def show(self):
        utils.draw_sprite(self.image)



