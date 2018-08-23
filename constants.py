#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Maksim Vasilev'


import pygame


DISPLAY_W, DISPLAY_H = 720, 720
BOARD_WIDTH = 720
ZERO = 0
BOARD_SQUARES = 27
WHITE = (255, 255, 255)

ZERO = 0
ONE = 1
TWO = 2
THREE = 3
FOUR = 4

SPRITE_DRAW_TICK = 30

WHEEL_ANIMATION_1 = None
WHEEL_ANIMATION_2 = None
WHEEL_ANIMATION_3 = None
WHEEL_10 = None

GD = None
CLK = None

PLAYER = None

DOC_YES = None
DEV_YES = None
SALES_YES = None

BOARD = None

P_DOC = None
P_DEV = None
P_SALES = None

METER_GOAL_100 = None

METER_HAPPINESS_000 = None
METER_HAPPINESS_025 = None
METER_HAPPINESS_050 = None
METER_HAPPINESS_075 = None
METER_HAPPINESS_100 = None

METER_FINANCE_000 = None
METER_FINANCE_025 = None
METER_FINANCE_050 = None
METER_FINANCE_075 = None
METER_FINANCE_100 = None

METER_HEALTH_000 = None
METER_HEALTH_025 = None
METER_HEALTH_050 = None
METER_HEALTH_075 = None
METER_HEALTH_100 = None

DIALOGUE_SEQUENCE_101 = None
DIALOGUE_SEQUENCE_102 = None
DIALOGUE_SEQUENCE_103 = None
DIALOGUE_SEQUENCE_104 = None

PIGGY_BANK = None
FINANCE = None
THANK_YOU = None

cell_types = {
    'market': (3, 8, 15, 24, ),
    'career': (1, 10, 13, 23, ),
    'family': (0, 4, 18, ),
    'leisure': (2, 19, 26, ),
    'quiz': (5, 12, 16, ),
    'home': (6, 25, ),
    'medical': (7, 14, 21, ),
    'transportation': (9, 22, ),
    'time_travel': (11, 17, ),
    'education': (20, 27, ),
}

token_positioning = {
    0: (0, 0),
    1: (0, -95),
    2: (0, -188),
    3: (0, -275),
    4: (0, -360),
    5: (0, -447),
    6: (0, -537),
    7: (0, -637),
    8: (95, -637),
    9: (185, -637),
    10: (275, -637),
    11: (360, -637),
    12: (447, -637),
    13: (537, -637),
    14: (637, -637),
    15: (637, -537),
    16: (637, -447),
    17: (637, -360),
    18: (637, -275),
    19: (637, -188),
    20: (637, -95),
    21: (637, 0),
    22: (537, 0),
    23: (447, 0),
    24: (360, 0),
    25: (275, 0),
    26: (185, 0),
    27: (95, 0),
}


def load_imgs():
    global BOARD, \
        P_DOC, \
        P_DEV, \
        P_SALES, \
        WHEEL_ANIMATION_1, \
        WHEEL_ANIMATION_2, \
        WHEEL_ANIMATION_3, \
        WHEEL_10, \
        METER_HAPPINESS_000, \
        METER_HAPPINESS_025, \
        METER_HAPPINESS_050, \
        METER_HAPPINESS_075, \
        METER_HAPPINESS_100, \
        METER_FINANCE_000, \
        METER_FINANCE_025, \
        METER_FINANCE_050, \
        METER_FINANCE_075, \
        METER_FINANCE_100, \
        METER_HEALTH_000, \
        METER_HEALTH_025, \
        METER_HEALTH_050, \
        METER_HEALTH_075, \
        METER_HEALTH_100, \
        METER_GOAL_100, \
        PIGGY_BANK, \
        FINANCE, \
        THANK_YOU, \
        DIALOGUE_SEQUENCE_101, \
        DIALOGUE_SEQUENCE_102, \
        DIALOGUE_SEQUENCE_103, \
        DIALOGUE_SEQUENCE_104

    BOARD = pygame.image.load('assets/BOARD.png')

    P_DOC = pygame.image.load('assets/p_doc.png')
    P_DEV = pygame.image.load('assets/p_dev.png')
    P_SALES = pygame.image.load('assets/p_sales.png')

    WHEEL_ANIMATION_1 = pygame.image.load('assets/wheel_spin_1.png')
    WHEEL_ANIMATION_2 = pygame.image.load('assets/wheel_spin_2.png')
    WHEEL_ANIMATION_3 = pygame.image.load('assets/wheel_spin_3.png')
    WHEEL_10 = pygame.image.load('assets/wheel_10.png')

#   #PIGGY_BANK = pygame.image.load('assets/piggy_bank.png')
    #FINANCE = pygame.image.load('assets/finance.png')
    #THANK_YOU = pygame.image.load('assets/thank_you.png')

    METER_HAPPINESS_000 = pygame.image.load('assets/METER_HAPPINESS_000.png')
    METER_HAPPINESS_025 = pygame.image.load('assets/METER_HAPPINESS_025.png')
    METER_HAPPINESS_050 = pygame.image.load('assets/METER_HAPPINESS_050.png')
    METER_HAPPINESS_075 = pygame.image.load('assets/METER_HAPPINESS_075.png')
    METER_HAPPINESS_100 = pygame.image.load('assets/METER_HAPPINESS_100.png')

    METER_FINANCE_000 = pygame.image.load('assets/METER_FINANCE_000.png')
    METER_FINANCE_025 = pygame.image.load('assets/METER_FINANCE_025.png')
    METER_FINANCE_050 = pygame.image.load('assets/METER_FINANCE_050.png')
    METER_FINANCE_075 = pygame.image.load('assets/METER_FINANCE_075.png')
    METER_FINANCE_100 = pygame.image.load('assets/METER_FINANCE_100.png')

    METER_HEALTH_000 = pygame.image.load('assets/METER_HEALTH_000.png')
    METER_HEALTH_025 = pygame.image.load('assets/METER_HEALTH_025.png')
    METER_HEALTH_050 = pygame.image.load('assets/METER_HEALTH_050.png')
    METER_HEALTH_075 = pygame.image.load('assets/METER_HEALTH_075.png')
    METER_HEALTH_100 = pygame.image.load('assets/METER_HEALTH_100.png')

    METER_GOAL_100 = pygame.image.load('assets/METER_GOAL_100.png')

    #DIALOGUE_SEQUENCE_101 = pygame.image.load('assets/DIALOGUE_SEQIENCE_101.png')
    #DIALOGUE_SEQUENCE_102 = pygame.image.load('assets/DIALOGUE_SEQIENCE_102.png')
    #DIALOGUE_SEQUENCE_103 = pygame.image.load('assets/DIALOGUE_SEQIENCE_103.png')
    #DIALOGUE_SEQUENCE_104 = pygame.image.load('assets/DIALOGUE_SEQIENCE_104.png')


def init_pygame():
    global GD, CLK, PLAYER, DISPLAY_W, DISPLAY_H
    pygame.init()
    GD = pygame.display.set_mode((DISPLAY_W, DISPLAY_H))
    pygame.display.set_caption("It's a small world!")
    CLK = pygame.time.Clock()
    pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN, pygame.KEYUP])
    PLAYER = {}


def init():
    init_pygame()
    load_imgs()