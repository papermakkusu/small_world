#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Maksim Vasilev'

import pygame
import utils


class InfoEvent(object):
    def __init__(self, intro_scene):

        self.scene = intro_scene

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


class PlayerChoiceEvent(object):
    """

    """


class DialogueEvent(object):
    def __init__(self, intro_scene, dialogue_0=None, dialogue_1=None, choice_screen=None, choice_1_yes=None,
                 choice_1_no=None, choice_2_yes=None, choice_2_no=None, choice_3_yes=None, choice_3_no=None,
                 choice_4_yes=None, choice_4_no=None, results=None):

        self.scene
        self.


        self.resources = {'intro_scene': intro_scene,
                          'dialogue_0': dialogue_0,
                          'dialogue_1': dialogue_1,
                          'choice_screen': choice_screen,
                          'choice_1_yes': choice_1_yes,
                          'choice_1_no': choice_1_no,
                          'choice_2_yes': choice_2_yes,
                          'choice_2_no': choice_2_no,
                          'choice_3_yes': choice_3_yes,
                          'choice_3_no': choice_3_no,
                          'choice_4_yes': choice_4_yes,
                          'choice_4_no': choice_4_no,
                          'results': results
                          }

    def play(self, func):
        """
        Play an abstract event

        :param func:
        :return:
        """
        if self.active_event is not None:
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
                            pass
                        elif event.key in [pygame.K_RIGHT]:
                            one, two, three = two, three, one
                        elif event.key == pygame.K_RETURN:
                            self.active_event = None
                            return

                func_3()
