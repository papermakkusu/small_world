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


class PlayerUI(pygame.sprite.Sprite):
    def __init__(self, cash=mglobals.FIRST_UI_VALUE, heart=mglobals.FIRST_UI_VALUE, face=mglobals.SECOND_UI_VALUE):
        super(PlayerUI, self).__init__()
        self.cash = cash
        self.heart = heart
        self.face = face

    def update(self, cash=None, heart=None, face=None):
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


class EventUI(pygame.sprite.Sprite):
    def __init__(self):
        super(EventUI, self).__init__()
        self.active_event = None

    class PiggyBank(object):
        def __init__(self):
            self.img = mglobals.PIGGY_BANK
            self.choice_1_yes = None
            self.choice_1_no = None
            self.choice_2_yes = None
            self.choice_2_no = None

    class Finance(object):
        def __init__(self):
            self.img = mglobals.FINANCE
            self.choice_1_yes = None
            self.choice_1_no = None
            self.choice_2_yes = None
            self.choice_2_no = None

    def update(self, event_type: int):
        if event_type in mglobals.CellTypes.PIGGY_BANK.value:
            self.active_event = self.PiggyBank()
        elif event_type in mglobals.CellTypes.FINANCE.value:
            self.active_event = self.Finance()

    def play(self):
        if self.active_event is not None:
            ev = (self.active_event.img, 'event')
            mglobals.GD.blit(self.active_event.img, self.active_event.img.get_rect())
            #utils.image_display(start)
            #utils.image_display(quit)
            while True:
                mglobals.GD.blit(self.active_event.img, self.active_event.img.get_rect())
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
                pygame.display.update()
                mglobals.CLK.tick(30)


class MsgUI(pygame.sprite.Sprite):
    def __init__(self):
        super(MsgUI, self).__init__()
        self.active_msg = self.ThankYou()

    class ThankYou(object):
        def __init__(self):
            self.img = mglobals.THANK_YOU

        def action(self):
            main()

    def update(self, msg_type):
        if msg_type == mglobals.THANK_YOU:
            self.active_msg = self.ThankYou()

    def play(self):
        mglobals.GD.blit(self.active_msg.img, self.active_msg.img.get_rect())

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
                        self.active_msg = None
                    mglobals.GD.blit(self.active_msg.img, self.active_msg.img.get_rect())

            pygame.display.update()
            mglobals.CLK.tick(30)

