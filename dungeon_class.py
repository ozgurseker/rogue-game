from Site_class import Site

class Dungeon:

    def __init__(self, board, m):
        self.N = m
        self.isRoom = []
        self.isCorridor = []

        for i in range(self.N):
            tmp_list1 = []
            tmp_list2 = []
            for j in range(self.N):
                if board [i][j] == '.':
                    tmp_list1.append(True)
                    tmp_list2.append(False)
                elif board[i][j] == '+':
                    tmp_list1.append(False)
                    tmp_list2.append(True)
                else:
                    tmp_list2.append(False)
                    tmp_list1.append(False)
            self.isRoom.append(tmp_list1)
            self.isCorridor.append(tmp_list2)


    def isCorridorSite (self, w):
        i = w.i
        j = w.j
        if i < 0 or j < 0 or i >= self.N or j >= self.N: return False
        return self.isCorridor[i][j]

    def isRoomSite (self, w):
        i = w.i
        j = w.j
        if i < 0 or j < 0 or i >= self.N or j >= self.N: return False
        return self.isRoom[i][j]

    def isWallSite(self, w):
        return  not (self.isCorridorSite(w) or self.isRoomSite(w))

    def isLegalMove(self, v, w):
        i1 = v.i
        i2 = w.i
        j1 = v.j
        j2 = w.j
        if (i1 < 0 or j1 < 0 or i1 >= self.N or j1 >= self.N): return False
        if (i2 < 0 or j2 < 0 or i2 >= self.N or j2 >= self.N): return False
        if self.isWallSite(v) or self.isWallSite(w) : return False
        if abs(i1 - i2) > 1 :  return False
        if abs(j1 - j2) > 1 : return False
        if self.isRoomSite(v) and self.isRoomSite(w): return True
        if i1 == i2 :               return True
        if j1 == j2 :               return True

    def LegalMoves(self, v):
        legals = list()
        i1 = v.i
        j1 = v.j
        for i in range(3):
            for j in range(3):
                if not i == 1 or not j == 1:
                    site = Site(i1 - 1 + i, j1 - 1 +j)
                    if self.isLegalMove(v, site):
                        legals.append(site)

        return legals

    def MinTime(self, v, w):
        if v.equals(w):
            return 0

        else:
            lifes = list()
            movelist = self.LegalMoves(v)
            for next in movelist:
                lifes.append(1 + self.MinTime(next, w))

            return min(lifes)

    def isInfSeq(self, A):
        dogrumu = True
        if len(A) < 4:
            return False
        if not A[0].equals(A[len(A)-1]):
            return False

        for i in range(len(A)):
            if not A[i-1] in A[i]:
                return False
            for j in range(len(A)):
                if not self.MinTime(A[i], A[j]) == min(abs(i-j), len(A)-abs(i-j)):
                    return False

        return dogrumu



