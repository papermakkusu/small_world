import pygame
import collections
from enum import Enum

DISPLAY_W, DISPLAY_H = 720, 720
BOARD_WIDTH = 720
ZERO = 0
BOARD_SQUARES = 27
WHITE = (255, 255, 255)

ZERO_UI_VALUE = 0
FIRST_UI_VALUE = 1
SECOND_UI_VALUE = 2
THIRD_UI_VALUE = 3

WHEEL_ANIMATION_1 = None
WHEEL_ANIMATION_2 = None
WHEEL_ANIMATION_3 = None
WHEEL_10 = None

IMG = None
GD = None
CLK = None

PLAYER = None

DOC_YES = None
DEV_YES = None
SALES_YES = None

BG_IMG = None

P_DOC = None
P_DEV = None
P_SALES = None

START_IMG = None
START_BTN_YES = None
START_BTN_NO = None
QUIT_BTN_YES = None
QUIT_BTN_NO = None
BACK_IMG = None

CASH_0 = None
CASH_1 = None
CASH_2 = None
CASH_3 = None

HEART_0 = None
HEART_1 = None
HEART_2 = None
HEART_3 = None

FACE_1 = None
FACE_2 = None
FACE_3 = None

PIGGY_BANK = None
FINANCE = None

THANK_YOU = None


class CellTypes(Enum):
    PIGGY_BANK = (3, 10, 13, 19, 23),
    FINANCE = (4, 17, 20, 26),
    MSG = (0, )


font_size_map = {
    'big': 50,
    'mid': 25,
    'small_p': 15,
    'small': 12,
}

player_positioning = {
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

color_map = {
    'white': (255, 255, 255),
    'black': (0, 0, 0,)
}


def load_imgs():
    global BACK_IMG, P1_IMG, P2_IMG, P_INFO_CLRSCR, MSG_CLRSCR, START_IMG, START_BTN_YES, START_BTN_NO, QUIT_BTN_YES, \
        QUIT_BTN_NO, DOC_YES, DEV_YES, SALES_YES, BG_IMG, P_DOC, P_DEV, P_SALES, WHEEL_ANIMATION_1, WHEEL_ANIMATION_2, \
        WHEEL_ANIMATION_3, WHEEL_10, CASH_0, CASH_1, CASH_2, CASH_3, HEART_0, HEART_1, HEART_2, HEART_3, FACE_1, \
        FACE_2, FACE_3, PIGGY_BANK, FINANCE, THANK_YOU

    DOC_YES = pygame.image.load('assets/player_doc.png')
    DEV_YES = pygame.image.load('assets/player_dev.png')
    SALES_YES = pygame.image.load('assets/player_sales.png')
    P_DOC = pygame.image.load('assets/p_doc.png')
    P_DEV = pygame.image.load('assets/p_dev.png')
    P_SALES = pygame.image.load('assets/p_sales.png')

    WHEEL_ANIMATION_1 = pygame.image.load('assets/wheel_spin_1.png')
    WHEEL_ANIMATION_2 = pygame.image.load('assets/wheel_spin_2.png')
    WHEEL_ANIMATION_3 = pygame.image.load('assets/wheel_spin_3.png')
    WHEEL_10 = pygame.image.load('assets/wheel_10.png')

    BG_IMG = pygame.image.load('assets/bg_pic_default.png')
    START_IMG = pygame.image.load('assets/start_screen_bg.png')
    START_BTN_YES = pygame.image.load('assets/start_yes.png')
    START_BTN_NO = pygame.image.load('assets/start_no.png')
    QUIT_BTN_YES = pygame.image.load('assets/quit_yes.png')
    QUIT_BTN_NO = pygame.image.load('assets/quit_no.png')
    BACK_IMG = pygame.image.load('assets/bg_pic_game.png')
    BACK_IMG = pygame.transform.scale(BACK_IMG, (DISPLAY_W, DISPLAY_H))
    P_INFO_CLRSCR = pygame.Surface([380, 380])
    MSG_CLRSCR = pygame.Surface([380, 18])

    CASH_0 = pygame.image.load('assets/money_0.png')
    CASH_1 = pygame.image.load('assets/money_1.png')
    CASH_2 = pygame.image.load('assets/money_2.png')
    CASH_3 = pygame.image.load('assets/money_3.png')
    HEART_1 = pygame.image.load('assets/heart_0.png')
    HEART_1 = pygame.image.load('assets/heart_1.png')
    HEART_2 = pygame.image.load('assets/heart_2.png')
    HEART_3 = pygame.image.load('assets/heart_3.png')
    FACE_1 = pygame.image.load('assets/face_disgust.png')
    FACE_2 = pygame.image.load('assets/face_normal.png')
    FACE_3 = pygame.image.load('assets/face_happy.png')

    PIGGY_BANK = pygame.image.load('assets/piggy_bank.png')
    FINANCE = pygame.image.load('assets/finance.png')
    THANK_YOU = pygame.image.load('assets/thank_you.png')


def init_pygame():
    global GD, CLK, IMG, PLAYER
    pygame.init()
    GD = pygame.display.set_mode((DISPLAY_W, DISPLAY_H))
    IMG = pygame.image
    pygame.display.set_caption("It's a small world!")
    CLK = pygame.time.Clock()
    pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN, pygame.KEYUP])
    PLAYER = {}


def init():
    init_pygame()
    load_imgs()
