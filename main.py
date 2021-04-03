from laby_class import Laby
from Game_class import Game

s = "sampleB.txt"
frag = Laby(s)


gm = Game(frag)
pry = gm.printable()
print(pry)

gm.play()
pry = gm.printable()
print(pry)


