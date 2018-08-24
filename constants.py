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

DICE_ROLL_0 = None
DICE_ROLL_1 = None
DICE_ROLL_2 = None
DICE_ROLL_3 = None
DICE_ROLL_4 = None
DICE_ROLL_5 = None
DICE_ROLL_6 = None
DICE_ROLL_7 = None
DICE_ROLL_8 = None
DICE_ROLL_9 = None
DICE_ROLL_10 = None
DICE_ROLL_11 = None
DICE_ROLL_12 = None
DICE_ROLL_13 = None
DICE_ROLL_14 = None
DICE_ROLL_FINAL_3 = None
DICE_ROLL_FINAL_7 = None
DICE_ROLL_FINAL_8 = None

GD = None
CLK = None
FPS = 30

DOC_YES = None
DEV_YES = None
SALES_YES = None

BOARD = None

GAME_PIECE = None

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

CHEAT_METER_0 = None
CHEAT_METER_0_1 = None
CHEAT_METER_0_2 = None
CHEAT_METER_0_3 = None
CHEAT_METER_0_4 = None
CHEAT_METER_0_5 = None
CHEAT_METER_1 = None
CHEAT_METER_1_1 = None
CHEAT_METER_1_2 = None
CHEAT_METER_1_3 = None
CHEAT_METER_1_4 = None
CHEAT_METER_1_5 = None
CHEAT_METER_2 = None
CHEAT_METER_2_1 = None
CHEAT_METER_2_2 = None
CHEAT_METER_2_3 = None
CHEAT_METER_2_4 = None
CHEAT_METER_2_5 = None
CHEAT_METER_3 = None

MARKET_EVENT_SEQUENCE_0 = None
MARKET_EVENT_SEQUENCE_1 = None
MARKET_EVENT_SEQUENCE_2 = None

CAREER_EVENT_SEQUENCE_0 = None
CAREER_EVENT_SEQUENCE_1 = None
CAREER_EVENT_SEQUENCE_2 = None
CAREER_EVENT_SEQUENCE_3_BUTTON_1 = None
CAREER_EVENT_SEQUENCE_3_BUTTON_2 = None
CAREER_EVENT_SEQUENCE_3_BUTTON_3 = None
CAREER_EVENT_SEQUENCE_3_BUTTON_4 = None
CAREER_EVENT_SEQUENCE_4 = None

FAMILY_EVENT_SEQUENCE_0 = None
FAMILY_EVENT_SEQUENCE_1 = None
FAMILY_EVENT_SEQUENCE_2 = None

PIGGY_BANK = None
FINANCE = None
THANK_YOU = None

SOUND_BOARD_MOVE = None
SOUND_DICE_ROLL = None
SOUND_SHOW_ROLL_RESULT = None
SOUND_EVENT_DISAPPEAR = None
SOUND_HAPPY_EVENT_APPEAR = None
SOUND_SAD_EVENT_APPEAR = None
SOUND_MENU_SELECTION = None


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
        MARKET_EVENT_SEQUENCE_0, \
        MARKET_EVENT_SEQUENCE_1, \
        MARKET_EVENT_SEQUENCE_2, \
        CAREER_EVENT_SEQUENCE_0, \
        CAREER_EVENT_SEQUENCE_1, \
        CAREER_EVENT_SEQUENCE_2, \
        CAREER_EVENT_SEQUENCE_3_BUTTON_1, \
        CAREER_EVENT_SEQUENCE_3_BUTTON_2, \
        CAREER_EVENT_SEQUENCE_3_BUTTON_3, \
        CAREER_EVENT_SEQUENCE_3_BUTTON_4, \
        CAREER_EVENT_SEQUENCE_4, \
        FAMILY_EVENT_SEQUENCE_0, \
        FAMILY_EVENT_SEQUENCE_1, \
        FAMILY_EVENT_SEQUENCE_2, \
        CHEAT_METER_0, \
        CHEAT_METER_0_1, \
        CHEAT_METER_0_2, \
        CHEAT_METER_0_3, \
        CHEAT_METER_0_4, \
        CHEAT_METER_0_5, \
        CHEAT_METER_1, \
        CHEAT_METER_1_1, \
        CHEAT_METER_1_2, \
        CHEAT_METER_1_3, \
        CHEAT_METER_1_4, \
        CHEAT_METER_1_5, \
        CHEAT_METER_2, \
        CHEAT_METER_2_1, \
        CHEAT_METER_2_2, \
        CHEAT_METER_2_3, \
        CHEAT_METER_2_4, \
        CHEAT_METER_2_5, \
        CHEAT_METER_3, \
        DICE_ROLL_0, \
        DICE_ROLL_1, \
        DICE_ROLL_2, \
        DICE_ROLL_3, \
        DICE_ROLL_4, \
        DICE_ROLL_5, \
        DICE_ROLL_6, \
        DICE_ROLL_7, \
        DICE_ROLL_8, \
        DICE_ROLL_9, \
        DICE_ROLL_10, \
        DICE_ROLL_11, \
        DICE_ROLL_12, \
        DICE_ROLL_13, \
        DICE_ROLL_14, \
        DICE_ROLL_FINAL_3, \
        DICE_ROLL_FINAL_7, \
        DICE_ROLL_FINAL_8, \
        GAME_PIECE,\
        SOUND_BOARD_MOVE,\
        SOUND_DICE_ROLL, \
        SOUND_SHOW_ROLL_RESULT, \
        SOUND_EVENT_DISAPPEAR,\
        SOUND_HAPPY_EVENT_APPEAR,\
        SOUND_SAD_EVENT_APPEAR,\
        SOUND_MENU_SELECTION

    BOARD = pygame.image.load('assets/BOARD.png')
    GAME_PIECE = pygame.image.load('assets/player-game-piece.png')

    DICE_ROLL_0 = pygame.image.load('assets/dice-roll-1.png')
    DICE_ROLL_1 = pygame.image.load('assets/dice-roll-2.png')
    DICE_ROLL_2 = pygame.image.load('assets/dice-roll-3.png')
    DICE_ROLL_3 = pygame.image.load('assets/dice-roll-4.png')
    DICE_ROLL_4 = pygame.image.load('assets/dice-roll-5.png')
    DICE_ROLL_5 = pygame.image.load('assets/dice-roll-6.png')
    DICE_ROLL_6 = pygame.image.load('assets/dice-roll-7.png')
    DICE_ROLL_7 = pygame.image.load('assets/dice-roll-8.png')
    DICE_ROLL_8 = pygame.image.load('assets/dice-roll-9.png')
    DICE_ROLL_9 = pygame.image.load('assets/dice-roll-10.png')
    DICE_ROLL_10 = pygame.image.load('assets/dice-roll-11.png')
    DICE_ROLL_11 = pygame.image.load('assets/dice-roll-12.png')
    DICE_ROLL_12 = pygame.image.load('assets/dice-roll-13.png')
    DICE_ROLL_13 = pygame.image.load('assets/dice-roll-14.png')
    DICE_ROLL_14 = pygame.image.load('assets/dice-roll-15.png')
    DICE_ROLL_FINAL_3 = pygame.image.load('assets/dice-roll-final-3.png')
    DICE_ROLL_FINAL_7 = pygame.image.load('assets/dice-roll-final-7.png')
    DICE_ROLL_FINAL_8 = pygame.image.load('assets/dice-roll-final-8.png')

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

    MARKET_EVENT_SEQUENCE_0 = pygame.image.load('assets/scene-market-720x720.png')
    MARKET_EVENT_SEQUENCE_1 = pygame.image.load('assets/scene-market-speech1-720x720.png')
    MARKET_EVENT_SEQUENCE_2 = pygame.image.load('assets/scene-market-speech1-720x720.png')

    CAREER_EVENT_SEQUENCE_0 = pygame.image.load('assets/scene-career-720x720.png')
    CAREER_EVENT_SEQUENCE_1 = pygame.image.load('assets/scene-career-speech1-720x720.png')
    CAREER_EVENT_SEQUENCE_2 = pygame.image.load('assets/scene-career-speech2-720x720.png')
    CAREER_EVENT_SEQUENCE_3_BUTTON_1 = pygame.image.load('assets/scene-career-speech4a-720x720.png')
    CAREER_EVENT_SEQUENCE_3_BUTTON_2 = pygame.image.load('assets/scene-career-speech4b-720x720.png')
    CAREER_EVENT_SEQUENCE_3_BUTTON_3 = pygame.image.load('assets/scene-career-speech4c-720x720.png')
    CAREER_EVENT_SEQUENCE_3_BUTTON_4 = pygame.image.load('assets/scene-career-speech4d-720x720.png')
    CAREER_EVENT_SEQUENCE_4 = pygame.image.load('assets/scene-career-speech5-720x720.png')

    FAMILY_EVENT_SEQUENCE_0 = pygame.image.load('assets/scene-family-720x720.png')
    FAMILY_EVENT_SEQUENCE_1 = pygame.image.load('assets/scene-family-speech1-720x720.png')
    FAMILY_EVENT_SEQUENCE_2 = pygame.image.load('assets/scene-family-speech1-720x720.png')

    CHEAT_METER_0 = pygame.image.load('assets/meter_1.png')
    CHEAT_METER_0_1 = pygame.image.load('assets/meter_1-1.png')
    CHEAT_METER_0_2 = pygame.image.load('assets/meter_1-2.png')
    CHEAT_METER_0_3 = pygame.image.load('assets/meter_1-3.png')
    CHEAT_METER_0_4 = pygame.image.load('assets/meter_1-4.png')
    CHEAT_METER_0_5 = pygame.image.load('assets/meter_1-5.png')
    CHEAT_METER_1 = pygame.image.load('assets/meter_2.png')
    CHEAT_METER_1_1 = pygame.image.load('assets/meter_2-1.png')
    CHEAT_METER_1_2 = pygame.image.load('assets/meter_2-2.png')
    CHEAT_METER_1_3 = pygame.image.load('assets/meter_2-3.png')
    CHEAT_METER_1_4 = pygame.image.load('assets/meter_2-4.png')
    CHEAT_METER_1_5 = pygame.image.load('assets/meter_2-5.png')
    CHEAT_METER_2 = pygame.image.load('assets/meter_3.png')
    CHEAT_METER_2_1 = pygame.image.load('assets/meter_3-1.png')
    CHEAT_METER_2_2 = pygame.image.load('assets/meter_3-2.png')
    CHEAT_METER_2_3 = pygame.image.load('assets/meter_3-3.png')
    CHEAT_METER_2_4 = pygame.image.load('assets/meter_3-4.png')
    CHEAT_METER_2_5 = pygame.image.load('assets/meter_3-5.png')
    CHEAT_METER_3 = pygame.image.load('assets/meter_4.png')

    SOUND_BOARD_MOVE = pygame.mixer.Sound('sounds/small_world_board_move.wav')
    SOUND_DICE_ROLL = pygame.mixer.Sound('sounds/small_world_dice_roll.wav')
    SOUND_SHOW_ROLL_RESULT = pygame.mixer.Sound('sounds/small_world_show_roll_result.wav')
    SOUND_EVENT_DISAPPEAR = pygame.mixer.Sound('sounds/small_world_event_disappear.wav')
    SOUND_HAPPY_EVENT_APPEAR = pygame.mixer.Sound('sounds/small_world_happy_event_appear.wav')
    SOUND_SAD_EVENT_APPEAR = pygame.mixer.Sound('sounds/small_world_sad_event_appear.wav')
    SOUND_MENU_SELECTION = pygame.mixer.Sound('sounds/small_world_menu_selection.wav')


def init_pygame():
    global GD, CLK, DISPLAY_W, DISPLAY_H
    pygame.init()
    pygame.mixer.pre_init(44100, 16, 2, 4096)
    GD = pygame.display.set_mode((DISPLAY_W, DISPLAY_H))
    pygame.display.set_caption("Invested")
    CLK = pygame.time.Clock()
    pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN, pygame.KEYUP])


def init():
    init_pygame()
    load_imgs()

