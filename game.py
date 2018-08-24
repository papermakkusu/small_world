#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Maksim Vasilev'


import pygame
import ui
import utils
from player import Player
from dice import Dice
from time import sleep
import constants


def game_loop():

    dice_rolls = (3, 7, 8, 0)

    event_counter = 0
    player = Player()
    dice = Dice()
    player_ui = ui.PlayerUI()
    event_ui = ui.EventUI()
    player_ui.update(0)  # (player.state)

    utils.draw_board()
    player.render()
    player_ui.render()

    while True:

        # if player.position in constants.cell_types['msg'] and player.round > 0:
        #    msg_ui.update_active(player.position)
        #    msg_ui.play()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

                if event.key == pygame.K_RETURN:
                    dice.throw(dice_rolls[event_counter])
                    event_counter += 1

                    # Move the player token across the board
                    for _ in range(dice.number):
                        utils.draw_board()
                        player_ui.render()
                        player.advance(1)
                        # if player.round > constants.ZERO:
                        #     sleep(0.4)
                        #     break
                        sleep(0.4)
                        pygame.display.update()
                        pygame.event.poll()

                    event_ui.spawn_event(player.position)
                    player.state = event_ui.play(player_ui, player.state)
                    utils.draw_board()
                    player.render()
                    player_ui.render()

        pygame.display.update()
        constants.CLK.tick(constants.FPS)
        if event_counter == 3:
            while True:
                for in_event in pygame.event.get():
                    if in_event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    elif in_event.type == pygame.KEYDOWN:
                        if in_event.key == pygame.K_ESCAPE:
                            pygame.quit()
                            quit()


def main():
    constants.init()
    # ui.draw_start_screen()
    # ui.draw_char_select_screen()
    game_loop()
    pygame.quit()
    quit()


if __name__ == '__main__':
    main()

