import pygame
import utils
import mglobals
from game import main


def draw_start_screen():
    one, two = (mglobals.START_BTN_YES, mglobals.QUIT_BTN_NO, 'start'), \
               (mglobals.START_BTN_NO, mglobals.QUIT_BTN_YES, 'quit')
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
        mglobals.CLK.tick(30)


def draw_char_select_screen():
    one, two, three = (mglobals.DOC_YES, 'doc'), \
                      (mglobals.DEV_YES, 'dev'), \
                      (mglobals.SALES_YES, 'sales')
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
                    mglobals.PLAYER = one[1]
                    return
                utils.draw_player_menu(one)
        pygame.display.update()
        mglobals.CLK.tick(30)


class PlayerUI(object):
    def __init__(self, cash=mglobals.FIRST_UI_VALUE, heart=mglobals.FIRST_UI_VALUE, face=mglobals.SECOND_UI_VALUE):
        super(PlayerUI, self).__init__()
        self.cash = cash
        self.heart = heart
        self.face = face

    def update_active(self, cash=None, heart=None, face=None):
        self.cash = cash if cash is not None else self.cash
        self.heart = heart if heart is not None else self.heart
        self.face = face if face is not None else self.face

    def render(self):
        for _ in (self.cash, self.heart, self.face):
            cash = (mglobals.CASH_0, mglobals.CASH_1, mglobals.CASH_2, mglobals.CASH_3)
            heart = (mglobals.HEART_0, mglobals.HEART_1, mglobals.HEART_2, mglobals.HEART_3)
            face = (mglobals.FACE_1, mglobals.FACE_2, mglobals.FACE_3)
            mglobals.GD.blit(cash[self.cash], cash[self.cash].get_rect())
            mglobals.GD.blit(heart[self.heart], heart[self.heart].get_rect())
            mglobals.GD.blit(face[self.face], face[self.face].get_rect())


class EventUI(object):
    def __init__(self):
        super(EventUI, self).__init__()
        self.active_event = None
        self.position = None

    class Event(object):
        def __init__(self, img, intro_scene, dialogue_0, dialogue_1, choice_screen, choice_1_yes, choice_1_no,
                     choice_2_yes, choice_2_no, choice_3_yes, choice_3_no, choice_4_yes, choice_4_no, results):
            self.img = mglobals.PIGGY_BANK
            self.intro_scene = None
            self.dialogue_0 = None
            self.dialogue_1 = None
            self.choice_screen = None
            self.choice_1_yes = None
            self.choice_1_no = None
            self.choice_2_yes = None
            self.choice_2_no = None
            self.choice_3_yes = None
            self.choice_3_no = None
            self.choice_4_yes = None
            self.choice_4_no = None
            self.results = None

        def play_event(self)
            pass

    class Finance(object):
        def __init__(self):
            self.img =
            self.choice_1_yes = None
            self.choice_1_no = None
            self.choice_2_yes = None
            self.choice_2_no = None

    def update_active(self, player_position):

        if player_position in mglobals.cell_types['piggy_bank']:
            self.active_event = self.Event(mglobals.PIGGY_BANK, )
        elif player_position in mglobals.cell_types['finance']:
            self.active_event = self.Event(mglobals.FINANCE, )

    def play(self):

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
                        #if event.key in [pygame.K_LEFT]:
                        #    one, two, three = three, one, two
                        #elif event.key in [pygame.K_RIGHT]:
                        #    one, two, three = two, three, one
                        elif event.key == pygame.K_RETURN:
                            self.active_event = None
                            return

                mglobals.GD.blit(self.active_event.img, self.active_event.img.get_rect())
                pygame.display.update()
                mglobals.CLK.tick(30)


class MsgUI(pygame.sprite.Sprite):
    def __init__(self):
        super(MsgUI, self).__init__()
        self.active_msg = None

    class ThankYou(object):
        def __init__(self):
            self.img = mglobals.THANK_YOU

        def action(self):
            main()

    def update_active(self, msg_type):
        if msg_type in mglobals.cell_types['msg']:
            self.active_msg = self.ThankYou()

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
                    # if event.key in [pygame.K_LEFT]:
                    #    one, two, three = three, one, two
                    # elif event.key in [pygame.K_RIGHT]:
                    #    one, two, three = two, three, one
                    elif event.key == pygame.K_RETURN:
                        self.active_msg.action()
                        #self.active_msg = None

            mglobals.GD.blit(self.active_msg.img, self.active_msg.img.get_rect())
            pygame.display.update()
            mglobals.CLK.tick(30)

