#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Maksim Vasilev'


import pygame
import ui
import constants
import utils
from player import Player
from dice import Dice
from time import sleep
import constants


def game_loop():

    dice_rolls = (3, 7, 8)

    event_counter = 0
    player = Player()
    dice = Dice()
    player_ui = ui.PlayerUI()
    event_ui = ui.EventUI()
    player_ui.update(player.state)

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
                    dice.throw(dice_rolls[event_counter])
                    dice.show()
                    event_counter += 1

                    # Move the player token across the board
                    for _ in range(dice.number):
                        utils.draw_board()
                        player_ui.render()
                        player.advance(1)
                        if player.round > constants.ZERO:
                            sleep(0.4)
                            break
                        sleep(0.4)
                        pygame.display.update()

                    event_ui.spawn_event(player.position)
                    event_ui.play(player_ui, player.state)
                    utils.draw_board()
                    player.render()
                    player_ui.render()

        #event_ui.update_active(player.position)
        #event_ui.play()
        pygame.display.update()
        constants.CLK.tick(constants.FPS)


def main():
    constants.init()
    #ui.draw_start_screen()
    #ui.draw_char_select_screen()
    game_loop()
    pygame.quit()
    quit()


if __name__ == '__main__':
    main()

