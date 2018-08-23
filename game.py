#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Maksim Vasilev'


import pygame
import ui
import constants
import utils
from player import Player
from dice import Wheel
from time import sleep
import constants


def game_loop():

    dice_rolls = (3, 7, 8)

    player = Player(constants.PLAYER)
    wheel = Wheel()
    player_ui = ui.PlayerUI()
    event_ui = ui.EventUI()
    player_ui.update_active(player.cash, player.heart, player.face, player.goal)

    utils.draw_board()
    player.render()
    player_ui.render()

    while True:

        #if player.position in constants.cell_types['msg'] and player.round > 0:
        #    msg_ui.update_active(player.position)
        # #   msg_ui.play()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

                if event.key == pygame.K_RETURN:
                    wheel.throw()
                    wheel.show()

                    # Move the player token across the board
                    for _ in range(wheel.number):
                        utils.draw_board()
                        player_ui.render()
                        player.advance(1)
                        if player.round > constants.ZERO:
                            sleep(0.4)
                            break
                        sleep(0.4)
                        pygame.display.update()

        #event_ui.update_active(player.position)
        #event_ui.play()
        pygame.display.update()
        constants.CLK.tick(30)


def main():
    constants.init()
    #ui.draw_start_screen()
    #ui.draw_char_select_screen()
    game_loop()
    pygame.quit()
    quit()


if __name__ == '__main__':
    main()

