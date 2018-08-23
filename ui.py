#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Maksim Vasilev'


import pygame
import utils
import constants
from game import main


def draw_start_screen():
    one, two = (constants.START_BTN_YES, constants.QUIT_BTN_NO, 'start'), \
               (constants.START_BTN_NO, constants.QUIT_BTN_YES, 'quit')
    utils.draw_start_menu(one[0], one[1])
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                if event.key in [pygame.K_UP, pygame.K_DOWN]:
                    one, two = two, one
                    utils.draw_start_menu(one[0], one[1])

                elif event.key == pygame.K_RETURN:
                    if one[2] == 'quit':
                        pygame.quit()
                        quit()
                    elif one[2] == 'start':
                        return
        pygame.display.update()
        constants.CLK.tick(30)


def draw_char_select_screen():
    one, two, three = (constants.DOC_YES, 'doc'), \
                      (constants.DEV_YES, 'dev'), \
                      (constants.SALES_YES, 'sales')
    utils.draw_player_menu(one)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                if event.key in [pygame.K_LEFT]:
                    one, two, three = three, one, two
                elif event.key in [pygame.K_RIGHT]:
                    one, two, three = two, three, one
                elif event.key == pygame.K_RETURN:
                    constants.PLAYER = one[1]
                    return
                utils.draw_player_menu(one)
        pygame.display.update()
        constants.CLK.tick(30)


class PlayerUI(object):
    def __init__(self, cash=constants.FIRST_UI_VALUE, heart=constants.FIRST_UI_VALUE, face=constants.SECOND_UI_VALUE):
        super(PlayerUI, self).__init__()
        self.cash = cash
        self.heart = heart
        self.face = face

    def update_active(self, cash=None, heart=None, face=None):
        self.cash = cash if cash is not None else self.cash
        self.heart = heart if heart is not None else self.heart
        self.face = face if face is not None else self.face

    def render(self):
        for _ in (self.cash, self.heart, self.face):
            cash = (constants.CASH_0, constants.CASH_1, constants.CASH_2, constants.CASH_3)
            heart = (constants.HEART_0, constants.HEART_1, constants.HEART_2, constants.HEART_3)
            face = (constants.FACE_1, constants.FACE_2, constants.FACE_3)
            constants.GD.blit(cash[self.cash], cash[self.cash].get_rect())
            constants.GD.blit(heart[self.heart], heart[self.heart].get_rect())
            constants.GD.blit(face[self.face], face[self.face].get_rect())


class EventUI(object):
    def __init__(self):
        super(EventUI, self).__init__()
        self.active_event = None
        self.position = None

    class Event(object):
        def __init__(self, intro_scene, dialogue_0=None, dialogue_1=None, choice_screen=None, choice_1_yes=None,
                     choice_1_no=None, choice_2_yes=None, choice_2_no=None, choice_3_yes=None, choice_3_no=None,
                     choice_4_yes=None, choice_4_no=None, results=None):
            self.intro_scene = intro_scene
            self.dialogue_0 = dialogue_0
            self.dialogue_1 = dialogue_1
            self.choice_screen = choice_screen
            self.choice_1_yes = choice_1_yes
            self.choice_1_no = choice_1_no
            self.choice_2_yes = choice_2_yes
            self.choice_2_no = choice_2_no
            self.choice_3_yes = choice_3_yes
            self.choice_3_no = choice_3_no
            self.choice_4_yes = choice_4_yes
            self.choice_4_no = choice_4_no
            self.results = results

                return
                constants.GD.blit(self.active_event.img, self.active_event.img.get_rect())
                pygame.display.update()
                constants.CLK.tick(30)


class MsgUI(pygame.sprite.Sprite):
    def __init__(self):
        super(MsgUI, self).__init__()
        self.active_msg = None

    class ThankYou(object):
        def __init__(self):
            self.img = constants.THANK_YOU

        def action(self):
            main()

    def update_active(self, msg_type):
        if msg_type in constants.cell_types['msg']:
            self.active_msg = self.ThankYou()

    def play(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()
                    # if event.key in [pygame.K_LEFT]:
                    #    one, two, three = three, one, two
                    # elif event.key in [pygame.K_RIGHT]:
                    #    one, two, three = two, three, one
                    elif event.key == pygame.K_RETURN:
                        self.active_msg.action()
                        #self.active_msg = None

            constants.GD.blit(self.active_msg.img, self.active_msg.img.get_rect())
            pygame.display.update()
            constants.CLK.tick(30)

