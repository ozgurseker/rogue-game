import math

class Laby:
    def __init__(self, s):
        self.f = open(s, "r")
        self.t = self.f.read()
        self.N = int(math.ceil(math.sqrt(len(self.t)/2)))
        self.NEWLINE = "\n"
        self.counter = 0

    def readLine(self):
        b = self.counter * self.N * 2
        e = b + self.N * 2
        self.counter = self.counter + 1
        s = self.t[b:e]
        return s

    def readAll(self):
        return self.t
        #sb = list()
        #while s != None and s != "":
        #    sb.append(s).append(self.NEWLINE)
        #    s = self.readLine()
        #return str(sb)


    def close(self):
        self.f.close()



#s = "sampleB.txt"
#lmn = Laby(s)
#s = lmn.readLine()
#while s != None and s != "":
#    print (s)
#    s = lmn.readLine()