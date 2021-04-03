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
        self.counter = 0
        self.memory = dict()

    def move(self):
        monster = self.monplace
        rogue = self.place

        return self.LifeTimeMaxPath(rogue,monster)[1]


    def LifeTimeMaxPath(self, r, m):
        self.counter += 1
        if self.counter % 500 == 0:
            print(self.counter)
        a = r.i + self.N * r.j + self.N ** 2 * m.i + self.N ** 3 * m.j
        if r.equals(m):
            return [0, None]

        elif a in self.memory.keys():
            return self.memory[a]


        else:
            monster = Monster(self.game)
            monster.place = m
            movelist = self.dungeon.LegalMoves(r)
            lifes = list()
            if self.counter > 200:
                life = np.inf
                move = movelist[0]
                return [life, move]
            for next in movelist:
                monster.rogplace = next
                mmove = monster.move()
                lifes.append(1 + self.LifeTimeMaxPath(next, mmove)[0])

            move = movelist[np.argmax(lifes)]
            life = max(lifes)
            if not life == np.inf:
                self.memory[a] = [life, move]

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








