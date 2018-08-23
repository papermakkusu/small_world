#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Maksim Vasilev'

import pygame
import utils
from time import sleep
import constants


class MarketEvent(object):
    def __init__(self):
        self.scenes = (constants.MARKET_EVENT_SEQUENCE_0,
                       constants.MARKET_EVENT_SEQUENCE_1,
                       constants.MARKET_EVENT_SEQUENCE_2,
                       )

    def play(self, player_ui: object, player_state: dict):

        screen = 0

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()
                    elif event.key == pygame.K_RETURN:
                        if screen == 2:
                            player_state['cash'] += 1
                            player_state['heart'] += 1
                            player_state['face'] += 1
                            player_ui.update(player_state)
                            player_ui.render()
                            sleep(0.5)
                            while True:
                                for inner_event in pygame.event.get():
                                    if inner_event.key == pygame.K_RETURN:
                                        return player_state
                        screen += 1

                player_ui.update(player_state)
                utils.draw_sprite(self.scenes[screen])
                player_ui.render()
                pygame.display.update()
                constants.CLK.tick(constants.FPS)


class CareerEvent(object):
    def __init__(self):
        self.scenes = (constants.CAREER_EVENT_SEQUENCE_0,
                       constants.CAREER_EVENT_SEQUENCE_1,
                       constants.CAREER_EVENT_SEQUENCE_2,
                       constants.CAREER_EVENT_SEQUENCE_3_BUTTON_1,
                       constants.CAREER_EVENT_SEQUENCE_3_BUTTON_2,
                       constants.CAREER_EVENT_SEQUENCE_3_BUTTON_3,
                       constants.CAREER_EVENT_SEQUENCE_3_BUTTON_4,
                       constants.CAREER_EVENT_SEQUENCE_4,
                       )
        self.choice = 0

    def draw_first_choice(self, player_ui: object, player_state: dict):
        player_state['cash'] += 1
        player_state['heart'] += 1
        player_state['face'] -= 1
        utils.draw_sprite(self.scenes[3])
        player_ui.update(player_state)
        player_ui.render()
        sleep(0.5)
        return player_state

    def draw_second_choice(self, player_ui: object, player_state: dict):
        player_state['cash'] += 1
        player_state['heart'] += 1
        player_state['face'] = player_state['face']
        utils.draw_sprite(self.scenes[3])
        player_ui.update(player_state)
        player_ui.render()
        sleep(0.5)
        return player_state

    def draw_third_choice(self, player_ui, player_state):
        player_state['cash'] += 1
        player_state['heart'] -= 1
        player_state['face'] = player_state['face']
        utils.draw_sprite(self.scenes[3])
        player_ui.update(player_state)
        player_ui.render()
        sleep(0.5)
        return player_state

    def draw_forth_choice(self, player_ui, player_state):
        player_state['cash'] = player_state['cash']
        player_state['heart'] -= 1
        player_state['face'] += 1
        utils.draw_sprite(self.scenes[3])
        player_ui.update(player_state)
        player_ui.render()
        sleep(0.5)
        return player_state

    def play(self, player_ui, player_state):

        screen = 0
        one = self.draw_first_choice
        two = self.draw_second_choice
        three = self.draw_third_choice
        four = self.draw_forth_choice

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()
                    elif event.key == pygame.K_RETURN:
                        if screen == 2:
                            end = False
                            while not end:
                                for inner_event in pygame.event.get():
                                    if inner_event.key in [pygame.K_DOWN]:
                                        one, two, three, four = four, one, two, three
                                        player_ui, player_state = one(player_ui, player_state)
                                    elif inner_event.key in [pygame.K_UP]:
                                        one, two, three, four = two, three, four, one
                                        player_ui, player_state = one(player_ui, player_state)
                                    elif inner_event.key == pygame.K_RETURN:
                                        screen += 1
                                        end = True
                                        break
                        if screen == 5:
                            return player_state
                        else:
                            screen += 1

            utils.draw_sprite(self.scenes[screen])
            player_ui.update(player_state)
            player_ui.render()


class FamilyEvent(object):
    def __init__(self):
        self.scenes = (constants.FAMILY_EVENT_SEQUENCE_0,
                       constants.FAMILY_EVENT_SEQUENCE_1,
                       constants.FAMILY_EVENT_SEQUENCE_2,
                       )

    def play(self, player_ui, player_state):

        screen = 0

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()
                    elif event.key == pygame.K_RETURN:
                        if screen == 2:
                            player_state['cash'] += 1
                            player_state['heart'] += 1
                            player_state['face'] += 1
                            player_ui.update(player_state)
                            player_ui.render()
                            sleep(0.5)
                            while True:
                                for inner_event in pygame.event.get():
                                    if inner_event.key == pygame.K_RETURN:
                                        return player_state
                        screen += 1
            utils.draw_sprite(self.scenes[screen])


