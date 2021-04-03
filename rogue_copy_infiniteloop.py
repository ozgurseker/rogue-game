import  numpy as np
from Site_class import Site
from monster_class import Monster

class Rogue:
    def __init__(self, G):
        self.game = G
        self.dungeon = G.dungeon
        self.N = G.N
        self.place = self.game.rogueSite
        self.monplace = self.game.monsterSite
        self.path = list()
        self.test_r = self.place
        self.test_m = None
        self.counter = 0

    def move(self):
        monster = self.monplace
        rogue = self.place

        return self.LifeTimeMaxPath(rogue,monster)[1]


    def LifeTimeMaxPath(self, r, m):
        self.counter += 1
        print(self.counter)
        if r.equals(m):
            return [0, None]
        else:
            monster = Monster(self.game)
            monster.place = m
            movelist = self.dungeon.LegalMoves(r)
            lifes = list()
            for next in movelist:
                monster.rogplace = next
                mmove = monster.move()

                if self.isInfiniteLoop(next,mmove):
                    life = np.inf
                    move = next
                    return [life, move]

                elif next.equals(self.test_r) and mmove.equals(self.test_m):
                    life = np.inf
                    move = next
                    return [life, move]
                else:
                    lifes.append(1 + self.LifeTimeMaxPath(next, mmove)[0])

            move = movelist[np.argmax(lifes)]
            life = max(lifes)

            return [life, move]

    def isInfiniteLoop(self, r, m):
        self.test_m = m
        self.test_r = r
        if self.LifeTimeMaxPath(r,m)[0] == np.inf:
            self.test_m = None
            self.test_r = self.place
            return True
        else:
            self.test_m = None
            self.test_r = self.place
            return False








