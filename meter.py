#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Maksim Vasilev'


import constants
import utils


class Meter(object):
    def __init__(self):
        self.coord = (constants.ZERO, constants.ZERO)
        self.animation_sequence_0 = (constants.CHEAT_METER_0,
                                     constants.CHEAT_METER_0_1,
                                     constants.CHEAT_METER_0_2,
                                     constants.CHEAT_METER_0_3,
                                     constants.CHEAT_METER_0_4,
                                     constants.CHEAT_METER_0_5,
                                     constants.CHEAT_METER_1,
                                     )
        self.animation_sequence_1 = (constants.CHEAT_METER_1,
                                     constants.CHEAT_METER_1_1,
                                     constants.CHEAT_METER_1_2,
                                     constants.CHEAT_METER_1_3,
                                     constants.CHEAT_METER_1_4,
                                     constants.CHEAT_METER_1_5,
                                     constants.CHEAT_METER_2,
                                     )
        self.animation_sequence_2 = (constants.CHEAT_METER_2,
                                     constants.CHEAT_METER_2_1,
                                     constants.CHEAT_METER_2_2,
                                     constants.CHEAT_METER_2_3,
                                     constants.CHEAT_METER_2_4,
                                     constants.CHEAT_METER_2_5,
                                     constants.CHEAT_METER_3,
                                     )

    def play_animation(self, number):
        if number == 0:
            utils.play_animation(0.05, self.animation_sequence_0)
            utils.draw_sprite(self.animation_sequence_0[-1])
        if number == 1:
            utils.play_animation(0.05, self.animation_sequence_1)
            utils.draw_sprite(self.animation_sequence_1[-1])
        if number == 2:
            utils.play_animation(0.05, self.animation_sequence_2)
            utils.draw_sprite(self.animation_sequence_2[-1])



