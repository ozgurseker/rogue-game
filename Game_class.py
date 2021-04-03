from monster_class import Monster
from rogue_class import Rogue
from dungeon_class import Dungeon
from Site_class import Site
from laby_class import Laby
import math

class Game:
    NEWLINE = "\n"

    def __init__(self, lmn):
        s = lmn.readLine()
        self.N = lmn.N
        self.board = list()
        mnstrlist = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "R", "S", "T",
                         "U", "V", "Y", "Z"]
        for i in range(self.N):
            row = list()
            for j in range(self.N):
                if s[j*2] in mnstrlist:
                    self.MONSTER = s[j*2]
                    self.monsterSite = Site(i,j)
                    #s[j*2] = '.'
                    row.append('.')


                elif s[j*2] == '@':
                    self.ROGUE = '@'
                    self.rogueSite = Site(i,j)
                    #s[j*2] = str('.')
                    row.append('.')

                else: row.append(s[j * 2])



            self.board.append(row)
            s = lmn.readLine()

        self.dungeon = Dungeon(self.board, self.N)
        self.monster = Monster(self)
        self.rogue = Rogue(self)

    def play(self):
        t = 0
        while(True):
            t += 1
            print("Move " + str(t))
            print("")
            self.rogue.counter = 0
            if self.monsterSite.equals(self.rogueSite):
                break

            next = self.monster.move()

            if self.dungeon.isLegalMove(self.monsterSite, next):
                self.monsterSite = next
                self.monster.place = next
                self.rogue.monplace = next

            else:
                print("cheating by monster")

            print(self.printable())

            if self.monsterSite.equals(self.rogueSite): break
            next = self.rogue.move()
            if self.dungeon.isLegalMove(self.rogueSite, next):
                self.rogueSite = next
                self.monster.rogplace = next
                self.rogue.place = next
            else:
                print("cheating by rogue")
            print(self.printable())





    def printable(self):
        s = ""
        for i in range(self.N):
            for j in range(self.N):
                site = Site(i,j)
                if self.rogueSite.equals(self.monsterSite) and self.rogueSite.equals(site):
                    s += "* "
                elif self.rogueSite.equals(site):
                    s += self.ROGUE   + " "
                elif self.monsterSite.equals(site):
                    s += self.MONSTER + " "
                elif self.dungeon.isRoomSite(site):
                    s += ". "
                elif self.dungeon.isCorridorSite(site):
                    s += "+ "
                elif self.dungeon.isRoomSite(site):
                    s += ". "
                elif self.dungeon.isWallSite(site):
                    s += "  "
            s += self.NEWLINE

        return s


