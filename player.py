import mglobals


class Player(object):

    def __init__(self, player_hint):
        if player_hint == 'dev':
            self.player_img = mglobals.P_DEV
        elif player_hint == 'doc':
            self.player_img = mglobals.P_DOC
        else:
            self.player_img = mglobals.P_SALES
        self.position = mglobals.ZERO
        self.coord = (mglobals.ZERO, mglobals.ZERO)
        self.cash = mglobals.SECOND_UI_VALUE
        self.heart = mglobals.SECOND_UI_VALUE
        self.face = mglobals.FIRST_UI_VALUE
        self.round = mglobals.ZERO

    def reposition(self):
        self.coord = mglobals.player_positioning[self.position]

    def advance(self, count):
        if self.position + count > mglobals.BOARD_SQUARES:
            self.position = self.position + count - mglobals.BOARD_SQUARES - 1
            self.round += 1
        else:
            self.position += count
        self.reposition()
        self.render()

    def render(self):
        mglobals.GD.blit(self.player_img, self.coord)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
