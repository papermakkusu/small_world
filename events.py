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
        sleep(1)
        constants.SOUND_EVENT_DISAPPEAR.play()
        utils.draw_sprite(self.scenes[screen])
        player_ui.update(0)     # (player_state)
        sleep(1)
        player_ui.render()

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
                        if screen == 1:
                            player_state['cash'] += 1
                            player_state['heart'] += 1
                            player_state['face'] += 1
                            # utils.draw_sprite(self.scenes[screen])
                            constants.SOUND_HAPPY_EVENT_APPEAR.play()
                            player_ui.update(1)  # (player_state)
                            player_ui.render()
                        if screen == 2:
                            return player_state
                        screen += 1
                        utils.draw_sprite(self.scenes[screen])
                        player_ui.render()
            pygame.display.update()
            constants.CLK.tick(constants.FPS)


class CareerEvent(object):
    def __init__(self):
        self.scenes = (constants.CAREER_EVENT_SEQUENCE_0,
                       constants.CAREER_EVENT_SEQUENCE_1,
                       constants.CAREER_EVENT_SEQUENCE_2,
                       constants.CAREER_EVENT_SEQUENCE_4,
                       constants.CAREER_EVENT_SEQUENCE_4,
                       constants.CAREER_EVENT_SEQUENCE_4,
                       constants.CAREER_EVENT_SEQUENCE_4,
                       )
        self.choice = 0

    def draw_first_choice(self, player_ui: object, player_state: dict):
        # player_state['cash'] += 1
        # player_state['heart'] += 1
        # player_state['face'] -= 1
        utils.draw_sprite(self.scenes[3])
        # player_ui.update(2)  # (player_state)
        # player_ui.render()
        # sleep(0.5)
        return  # player_ui, player_state

    def draw_second_choice(self, player_ui: object, player_state: dict):
        # player_state['cash'] += 1
        # player_state['heart'] += 1
        # player_state['face'] = player_state['face']
        utils.draw_sprite(self.scenes[4])
        # player_ui.update(2)  # (player_state)
        # player_ui.render()
        # sleep(0.5)
        return  # player_ui, player_state

    def draw_third_choice(self, player_ui, player_state):
        # player_state['cash'] += 1
        # player_state['heart'] -= 1
        # player_state['face'] = player_state['face']
        utils.draw_sprite(self.scenes[5])
        # player_ui.update(2)  # (player_state)
        # layer_ui.render()
        # sleep(0.5)
        return  # player_ui, player_state

    def draw_forth_choice(self, player_ui, player_state):
        # player_state['cash'] = player_state['cash']
        # player_state['heart'] -= 1
        # player_state['face'] += 1
        utils.draw_sprite(self.scenes[6])
        # player_ui.update(2)  # (player_state)
        # player_ui.render()
        # sleep(0.5)
        return  # player_ui, player_state

    def play(self, player_ui, player_state):

        screen = 0
        sleep(1)
        constants.SOUND_EVENT_DISAPPEAR.play()
        utils.draw_sprite(self.scenes[screen])
        sleep(1)
        player_ui.render()

        screen = 0
        one = constants.CAREER_EVENT_SEQUENCE_3_BUTTON_1
        two = constants.CAREER_EVENT_SEQUENCE_3_BUTTON_2
        three = constants.CAREER_EVENT_SEQUENCE_3_BUTTON_3
        four = constants.CAREER_EVENT_SEQUENCE_3_BUTTON_4

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()
                    if event.key in [pygame.K_DOWN]:
                        if screen == 3:
                            constants.SOUND_MENU_SELECTION.play()
                            one, two, three, four = two, three, four, one
                    if event.key in [pygame.K_UP]:
                        if screen == 3:
                            constants.SOUND_MENU_SELECTION.play()
                            one, two, three, four = four, one, two, three
                    if event.key == pygame.K_RETURN:
                        screen += 1
                        if screen != 3:
                            utils.draw_sprite(self.scenes[screen])
                            player_ui.render()
                        if screen == 5:
                            constants.SOUND_SAD_EVENT_APPEAR.play()
                            utils.draw_sprite(self.scenes[screen])
                            player_ui.update(2)
                            player_ui.render()
                        if screen == 6:
                            return player_state

            if screen == 3:
                utils.draw_sprite(one)
                player_ui.render()
            pygame.display.update()


class FamilyEvent(object):
    def __init__(self):
        self.scenes = (constants.FAMILY_EVENT_SEQUENCE_0,
                       constants.FAMILY_EVENT_SEQUENCE_1,
                       constants.FAMILY_EVENT_SEQUENCE_2,
                       )

    def play(self, player_ui: object, player_state: dict):

        screen = 0
        sleep(1)
        constants.SOUND_EVENT_DISAPPEAR.play()
        utils.draw_sprite(self.scenes[screen])
        player_ui.update(2)  # (player_state)
        sleep(1)
        player_ui.render()

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
                        if screen == 1:
                            player_state['cash'] -= 1
                            player_state['heart'] += 1
                            player_state['face'] -= 2
                            constants.SOUND_HAPPY_EVENT_APPEAR.play()
                            # utils.draw_sprite(self.scenes[screen])
                            player_ui.update(3)  # (player_state)
                            player_ui.render()
                        if screen == 2:
                            return player_state
                        screen += 1
                        utils.draw_sprite(self.scenes[screen])
                        # player_ui.update(player_state)
                        player_ui.render()

            pygame.display.update()
            constants.CLK.tick(constants.FPS)

