#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Maksim Vasilev'


import constants
import pygame


class Player(object):

    def __init__(self):
        self.player_img = constants.GAME_PIECE
        self.position = constants.ZERO
        self.coord = (constants.ZERO, constants.ZERO)
        self.state = {'cash': constants.TWO,
                      'heart': constants.TWO,
                      'face': constants.TWO,
                      'goal': constants.FOUR
                      }
        self.round = constants.ZERO
        self.event = None

    def reposition(self):
        self.coord = constants.token_positioning[self.position]

    def advance(self, count):
        if self.position + count > constants.BOARD_SQUARES:
            self.position = self.position + count - constants.BOARD_SQUARES - 1
            self.round += 1
        else:
            self.position += count
        self.reposition()
        self.render()
        constants.SOUND_BOARD_MOVE.play()

    def change_state(self, cash=None, heart=None, face=None, goal=None):
        self.resources['cash'] = cash if cash is not None else self.resources['cash']
        self.resources['heart'] = heart if heart is not None else self.resources['heart']
        self.resources['face'] = face if face is not None else self.resources['face']
        self.resources['goal'] = goal if goal is not None else self.resources['goal']

    def render(self):
        constants.GD.blit(self.player_img, self.coord)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
