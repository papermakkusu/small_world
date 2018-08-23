#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Maksim Vasilev'


import constants
import events


class Player(object):

    def __init__(self, player_hint):
        if player_hint == 'dev':
            self.player_img = constants.P_DEV
        elif player_hint == 'doc':
            self.player_img = constants.P_DOC
        else:
            self.player_img = constants.P_SALES
        self.position = constants.ZERO
        self.coord = (constants.ZERO, constants.ZERO)
        self.cash = constants.TWO
        self.heart = constants.TWO
        self.face = constants.TWO
        self.goal = constants.FOUR
        self.round = constants.ZERO
        self.event = None

    def reposition(self):
        self.coord = constants.token_positioning[self.position]

#    def set_event(self, player_position):
#
#        if player_position in constants.cell_types['piggy_bank']:
#            self.event = Event(constants.PIGGY_BANK, )
#        elif player_position in constants.cell_types['finance']:
#            self.event = Event(constants.FINANCE, )
#        elif player_position in constants.cell_types['finance']:
#            self.event = Event(constants.FINANCE, )

    def advance(self, count):
        if self.position + count > constants.BOARD_SQUARES:
            self.position = self.position + count - constants.BOARD_SQUARES - 1
            self.round += 1
        else:
            self.position += count
        self.reposition()
        self.render()

    def loose_resource(self, resource: str):
        """
        Decrease resource meter with an animation

        :param count:
        :return:
        """

    def gain_resource(self, count: str):
        """
        Increase resource meter with animation

        :param count:
        :return:
        """

    def render(self):
        constants.GD.blit(self.player_img, self.coord)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
