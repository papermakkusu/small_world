#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Maksim Vasilev'

from events import Event
import utils


class SequenceOne(object):
    """
    Structured event sequence

    """

    def __init__(self, event_assets):

        self.events = []

        for _ in event_assets:
            self.events.add(Event(event_assets))

    def play_sequence(self):
        """
        1st event Market Event
        > Show picture
        > Show the next picture
        > delay
        > Show meters animations

        :return:
        """

        for _ in self.events:
            self.event.play(utils.draw_sprite, sprite)
