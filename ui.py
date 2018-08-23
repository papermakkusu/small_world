#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Maksim Vasilev'


import pygame
import utils
import constants
from game import main
import events_assets
import events


#def draw_start_screen():
#    one, two = (constants.START_BTN_YES, constants.QUIT_BTN_NO, 'start'), \
#               (constants.START_BTN_NO, constants.QUIT_BTN_YES, 'quit')
#    utils.draw_start_menu(one[0], one[1])
#    while True:
#        for event in pygame.event.get():
#            if event.type == pygame.QUIT:
#                pygame.quit()
#                quit()
#            elif event.type == pygame.KEYDOWN:
#                if event.key == pygame.K_ESCAPE:
#                    pygame.quit()
#                    quit()
#                if event.key in [pygame.K_UP, pygame.K_DOWN]:
#                    one, two = two, one
#                    utils.draw_start_menu(one[0], one[1])
#
#                elif event.key == pygame.K_RETURN:
#                    if one[2] == 'quit':
#                        pygame.quit()
#                        quit()
#                    elif one[2] == 'start':
#                        return
#        pygame.display.update()
#        constants.CLK.tick(30)


#def draw_char_select_screen():
#    one, two, three = (constants.DOC_YES, 'doc'), \
#                      (constants.DEV_YES, 'dev'), \
#                      (constants.SALES_YES, 'sales')
#    utils.draw_player_menu(one)
#    while True:
#        for event in pygame.event.get():
#            if event.type == pygame.QUIT:
#                pygame.quit()
#                quit()
#            elif event.type == pygame.KEYDOWN:
#                if event.key == pygame.K_ESCAPE:
#                    pygame.quit()
#                    quit()
#                if event.key in [pygame.K_LEFT]:
#                    one, two, three = three, one, two
#                elif event.key in [pygame.K_RIGHT]:
#                    one, two, three = two, three, one
#                elif event.key == pygame.K_RETURN:
#                    constants.PLAYER = one[1]
#                    return
#                utils.draw_player_menu(one)
#        pygame.display.update()
#        constants.CLK.tick(30)


class PlayerUI(object):
    def __init__(self, cash=constants.TWO, heart=constants.TWO, face=constants.TWO, goal=constants.FOUR):
        super(PlayerUI, self).__init__()
        self.cash = cash
        self.heart = heart
        self.face = face
        self.goal = goal

    def update_active(self, cash=None, heart=None, face=None, goal=None):
        self.cash = cash if cash is not None else self.cash
        self.heart = heart if heart is not None else self.heart
        self.face = face if face is not None else self.face
        self.goal = goal if goal is not None else self.goal

    def render(self):
        cash = (constants.METER_FINANCE_000,
                constants.METER_FINANCE_025,
                constants.METER_FINANCE_050,
                constants.METER_FINANCE_075,
                constants.METER_FINANCE_100,
                )
        heart = (constants.METER_HEALTH_000,
                 constants.METER_HEALTH_025,
                 constants.METER_HEALTH_050,
                 constants.METER_HEALTH_075,
                 constants.METER_HEALTH_100,
                 )
        face = (constants.METER_HAPPINESS_000,
                constants.METER_HAPPINESS_025,
                constants.METER_HAPPINESS_050,
                constants.METER_HAPPINESS_075,
                constants.METER_HAPPINESS_100,
                )
        goal = (constants.METER_GOAL_100,
                constants.METER_GOAL_100,
                constants.METER_GOAL_100,
                constants.METER_GOAL_100,
                constants.METER_GOAL_100,
                )
        constants.GD.blit(cash[self.cash], cash[self.cash].get_rect())
        constants.GD.blit(heart[self.heart], heart[self.heart].get_rect())
        constants.GD.blit(face[self.face], face[self.face].get_rect())
        constants.GD.blit(goal[self.goal], goal[self.goal].get_rect())


class EventUI(object):
    def __init__(self,):
        super(EventUI, self).__init__()
        self.active_event = None
        self.position = None
        self.market = events.InfoEvent(constants.BOARD)
        self.career = events.DialogueEvent((constants.BOARD, constants.BOARD))
        self.family = events.InfoEvent(constants.BOARD)

    def execute(self, position):

        if position in constants.cell_types['market']:
            self.market.play()
        elif position in self.constants.cell_types['career']:
            self.career.play()
        elif position in constants.cell_types['family']:
            self.family.play()


#class MsgUI(pygame.sprite.Sprite):
#    def __init__(self):
#        super(MsgUI, self).__init__()
#        self.active_msg = None
#
#    class ThankYou(object):
#        def __init__(self):
#            self.img = constants.THANK_YOU
#
#        def action(self):
#            main()
#
#    def update_active(self, msg_type):
#        if msg_type in constants.cell_types['msg']:
#            self.active_msg = self.ThankYou()
#
#    def play(self):
#
#        while True:
#            for event in pygame.event.get():
#                if event.type == pygame.QUIT:
#                    pygame.quit()
#                    quit()
#                elif event.type == pygame.KEYDOWN:
#                    if event.key == pygame.K_ESCAPE:
#                        pygame.quit()
#                        quit()
#                    # if event.key in [pygame.K_LEFT]:
#                    #    one, two, three = three, one, two
#                    # elif event.key in [pygame.K_RIGHT]:
#                    #    one, two, three = two, three, one
#                    elif event.key == pygame.K_RETURN:
#                        self.active_msg.action()
#                        #self.active_msg = None
#
#            constants.GD.blit(self.active_msg.img, self.active_msg.img.get_rect())
#            pygame.display.update()
#            constants.CLK.tick(30)

