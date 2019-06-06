from direction import allDirs

class Pos:
    
    def __init__(self, r, c):
        self.r = r
        self.c = c

    @classmethod
    def parse(cls, posStr):
        r = ord(posStr[0]) - ord('A') + 1
        c = int(posStr[1])
        return cls(r, c)

    def toString(self):
        return chr(ord('A') - 1 + self.r) + str(self.c)

    def clone(self):
        return Pos(self.r, self.c)

    def move(self, dir):
        if dir not in allDirs():
            raise TypeError(dir + " is not a valid direction")

        if 'N' in dir:
            self.r -= 1
        if 'S' in dir:
            self.r += 1
        if 'E' in dir:
            self.c += 1
        if 'W' in dir:
            self.c -= 1
