
class Site:
    def __init__(self, i,j):
        self.i = i
        self.j = j


    def manhattanTo(self, w):
        i1 = self.i
        i2 = w.i
        j1 = self.j
        j2 = w.j
        return abs(i1 - i2) + abs(j1 - j2)

    def euclideanTo(self, w):
        i1 = self.i
        i2 = w.i
        j1 = self.j
        j2 = w.j
        return (i1-i2)**2 + (j1 - j2)**2

    def equals(self,w):
        if w == None:
            return False
        return self.manhattanTo(w) == 0



