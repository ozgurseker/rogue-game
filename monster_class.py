import numpy as np
from Site_class import Site


class Monster:

    def __init__(self, G):
        self.gm = G
        self.dungeon = self.gm.dungeon
        self.N = self.dungeon.N
        self.place = self.gm.monsterSite
        self.rogplace = self.gm.rogueSite

    def move(self):
        monster = self.place
        rogue = self.rogplace
        move = None
        n = 0
        if monster.equals(rogue):
            return monster
        movematrix = np.full((3,3), np.inf)

        for i in range(3):
            for j in range(3):
                site = Site(i + monster.i - 1, monster.j + j - 1)
                if self.dungeon.isLegalMove(monster, site):
                    movematrix[i][j] = site.euclideanTo(rogue)
        j = np.argmin(movematrix) % 3
        i = int((np.argmin(movematrix) - j) / 3)
        move = Site(i + monster.i - 1, monster.j + j - 1)

        return move


