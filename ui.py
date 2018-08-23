#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Maksim Vasilev'


import constants
import events
import pygame
import utils


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
        constants.CLK.tick(constants.FPS)


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
        constants.CLK.tick(constants.FPS)


class PlayerUI(object):
    def __init__(self):
        super(PlayerUI, self).__init__()
        self.cash = (constants.METER_FINANCE_000,
                     constants.METER_FINANCE_025,
                     constants.METER_FINANCE_050,
                     constants.METER_FINANCE_075,
                     constants.METER_FINANCE_100,
                     )
        self.heart = (constants.METER_HEALTH_000,
                      constants.METER_HEALTH_025,
                      constants.METER_HEALTH_050,
                      constants.METER_HEALTH_075,
                      constants.METER_HEALTH_100,
                      )
        self.face = (constants.METER_HAPPINESS_000,
                     constants.METER_HAPPINESS_025,
                     constants.METER_HAPPINESS_050,
                     constants.METER_HAPPINESS_075,
                     constants.METER_HAPPINESS_100,
                     )
        self.goal = (constants.METER_GOAL_100,
                     constants.METER_GOAL_100,
                     constants.METER_GOAL_100,
                     constants.METER_GOAL_100,
                     constants.METER_GOAL_100,
                     )
        self.active_state = {}

    def update(self, kwargs):
        self.active_state['cash'] = kwargs['cash']
        self.active_state['heart'] = kwargs['heart']
        self.active_state['face'] = kwargs['face']
        self.active_state['goal'] = kwargs['goal']

    def render(self):
        constants.GD.blit(self.cash[self.active_state['cash']], self.cash[self.active_state['cash']].get_rect())
        constants.GD.blit(self.heart[self.active_state['heart']], self.heart[self.active_state['heart']].get_rect())
        constants.GD.blit(self.face[self.active_state['face']], self.face[self.active_state['face']].get_rect())
        constants.GD.blit(self.goal[self.active_state['goal']], self.goal[self.active_state['goal']].get_rect())


class EventUI(object):
    def __init__(self,):
        super(EventUI, self).__init__()
        self.active_event = None

    def spawn_event(self, player_position):
        if player_position in constants.cell_types['market']:
            self.active_event = events.MarketEvent()
        elif player_position in constants.cell_types['career']:
            self.active_event = events.CareerEvent()
        elif player_position in constants.cell_types['family']:
            self.active_event = events.FamilyEvent()

    def play(self, player_ui, player_state):
        self.active_event.play(player_ui, player_state)

