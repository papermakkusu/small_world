#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Maksim Vasilev'


import pygame
import constants
from time import sleep


def draw_board():
    constants.GD.fill(constants.WHITE)
    constants.GD.blit(constants.BOARD, (0, 0))


#def draw_start_menu(start, quit):
#    constants.GD.fill(constants.WHITE)
#    constants.GD.blit(constants.START_IMG, constants.START_IMG.get_rect())
#    draw_sprite(start)#
#    draw_sprite(quit)
#
#
def draw_player_menu(*args):
    constants.GD.fill(constants.WHITE)
    constants.GD.blit(constants.BG_IMG, constants.BG_IMG.get_rect())

    draw_sprite(args[0])


def play_animation(interval: float, repeat: int, resources: list):
    for _ in range(repeat):
        for __ in resources:
            constants.GD.blit(__, __.get_rect())
            pygame.display.update()
            sleep(interval)


def draw_sprite(sprite):
    constants.GD.blit(sprite, sprite.get_rect())
    pygame.display.update()
    constants.CLK.tick(30)



