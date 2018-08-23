#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Maksim Vasilev'

import pygame
import utils
from time import sleep
import constants


class InfoEvent(object):
    def __init__(self, intro_scene=None):

        self.scene = constants.BOARD

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
                    elif event.key == pygame.K_RETURN:
                        return
            utils.draw_sprite(self.intro_scene_img)


class UpdateMetersEvent(object):
    def __init__(self, meter_hapiness_asset: list=None, meter_health_asset: list=None, meter_finance_asset: list=None):
        self.meters = (meter_hapiness_asset, meter_health_asset, meter_finance_asset)
        self.done = False

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
                    elif event.key == pygame.K_RETURN:
                        self.done = False
                        return
            if not self.done:
                for _ in self.meters:
                    if _ is not None:
                        utils.draw_sprite(self.intro_scene_img)
                    sleep(0.3)
                self.done = True


class PlayerChoiceEvent(object):
    """
    TODO: Make an event where the player can choose between several answers

    """
    def __init__(self, dialogue_sequence: list):

        self.dialogue_sequence = dialogue_sequence
        self.done = False
        self.choice_one_yes = (constants.DOC_YES, 'doc')
        self.choice_one_no = (constants.DOC_YES, 'doc')
        self.choice_two_yes = (constants.DEV_YES, 'dev')
        self.choice_two_no = (constants.DEV_YES, 'dev')
        self.choice_three_yes = (constants.SALES_YES, 'sales')
        self.choice_three_no = (constants.SALES_YES, 'sales')
        self.choice_four_yes = (constants.SALES_YES, 'sales')
        self.choice_four_no = (constants.SALES_YES, 'sales')

        self.position_0 = (self.choice_one_yes,
                           self.choice_two_no,
                           self.choice_three_no,
                           self.choice_four_no)
        self.position_1 = (self.choice_one_yes,
                           self.choice_two_no,
                           self.choice_three_no,
                           self.choice_four_no)
        self.position_2 = (self.choice_one_yes,
                           self.choice_two_no,
                           self.choice_three_no,
                           self.choice_four_no)
        self.position_3 = (self.choice_one_yes,
                           self.choice_two_no,
                           self.choice_three_no,
                           self.choice_four_no)


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
                    if event.key in [pygame.K_DOWN]:
                        self.choice_one_yes

                        one, two = two, one



                        utils.draw_start_menu(one[0], one[1])
                    elif event.key in [pygame.K_UP]:
                        pass
                    elif event.key == pygame.K_RETURN:
                        self.done = False
                        return

            if not self.done:
                for _ in self.dialogue_sequence:
                    if _ is not None:
                        utils.draw_sprite(self.intro_scene_img)
                    sleep(1)
                self.done = True

            utils.draw_player_menu(one)


class DialogueEvent(object):
    def __init__(self, dialogue_sequence: list):

        self.dialogue_sequence = dialogue_sequence
        self.done = False

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
                    elif event.key == pygame.K_RETURN:
                        self.done = False
                        return
            if not self.done:
                for _ in self.dialogue_sequence:
                    if _ is not None:
                        utils.draw_sprite(self.intro_scene_img)
                    sleep(1)
                self.done = True


