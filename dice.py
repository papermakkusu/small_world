#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Maksim Vasilev'


import random
import constants
import utils
from time import sleep


class Dice(object):
    def __init__(self):
        self.number = constants.ZERO
        self.roll_result = {3: constants.DICE_ROLL_FINAL_3,
                            7: constants.DICE_ROLL_FINAL_7,
                            8: constants.DICE_ROLL_FINAL_8}
        self.coord = (constants.ZERO, constants.ZERO)
        self.animation_sequence = (constants.DICE_ROLL_0,
                                   constants.DICE_ROLL_1,
                                   constants.DICE_ROLL_2,
                                   constants.DICE_ROLL_3,
                                   constants.DICE_ROLL_4,
                                   constants.DICE_ROLL_5,
                                   constants.DICE_ROLL_6,
                                   constants.DICE_ROLL_7,
                                   constants.DICE_ROLL_8,
                                   constants.DICE_ROLL_9,
                                   constants.DICE_ROLL_10,
                                   constants.DICE_ROLL_11,
                                   constants.DICE_ROLL_12,
                                   constants.DICE_ROLL_13,
                                   constants.DICE_ROLL_14,
                                   )

    def throw(self, count=None):

        self.number = count if count is not None else random.randrange(10, 11)  # broken random, always shows 10

        # TODO change dice roll result image here
        # self.image =
        constants.SOUND_DICE_ROLL.play()
        self.play_animation()
        constants.SOUND_SHOW_ROLL_RESULT.play()
        self.show(count)
        sleep(3)

    def play_animation(self):
        utils.play_animation(0.07, self.animation_sequence)

    def show(self,roll: int):
        utils.draw_sprite(self.roll_result[roll])



