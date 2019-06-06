from exceptions import MoveError
from position import Pos
from direction import allDirs

class Board:

    board = [['+', '-', '-', '-', '-', '-', '+'],
             ['|', 'X', 'X', 'X', 'X', 'X', '|'],
             ['|', ' ', ' ', ' ', ' ', ' ', '|'],
             ['|', ' ', ' ', '*', ' ', ' ', '|'],
             ['|', ' ', ' ', ' ', ' ', ' ', '|'],
             ['|', 'O', 'O', 'O', 'O', 'O', '|'],
             ['+', '-', '-', '-', '-', '-', '+']]

    def show(self):
        print()
        print("    1 2 3 4 5")
        for rowIndex in range(7):
            if rowIndex != 0 and rowIndex != 6:
                print(chr(ord('A') + rowIndex - 1), end=' ')
            else:
                print("  ", end='')
            for colIndex in range(7):
                print(self.board[rowIndex][colIndex], end='')
                if colIndex != 6:
                    if rowIndex == 0 or rowIndex == 6:
                        print("-", end = '')
                    else:
                        print(" ", end='')
            print()
        print()

    def pieceAt(self, pos):
        return self.board[pos.r][pos.c]

    def hasPiece(self, pos, piece):
        return self.pieceAt(pos) == piece

    def canMove(self, pos, dir):
        pos2 = pos.clone()
        pos2.move(dir)
        return self.pieceAt(pos2) == " "

    def moveInternal(self, pos, dir):
        posEnd = pos.clone()
        while self.canMove(posEnd, dir):
            posEnd.move(dir)

        self.movePieceTo(pos, posEnd);
        return posEnd

    def movePieceTo(self, pFrom, pTo):
        self.board[pTo.r][pTo.c] = self.board[pFrom.r][pFrom.c]
        self.board[pFrom.r][pFrom.c] = " "

    def move(self, pos, piece, dir):
        if not self.hasPiece(pos, piece):
            if (self.pieceAt(pos) == " "):
                raise MoveError("No piece in " + pos.toString() + " to move")
            else:
                raise MoveError("Piece in " + pos.toString() + " is not a " + piece + " piece.")
        elif not self.canMove(pos, dir):
            raise MoveError("Can't move piece " + pos.toString() + " in direction " + dir);
        else:
            self.moveInternal(pos, dir)
        
        self.show()

    def getNeutron(self):
        for r in range(1, 6):
            for c in range(1, 6):
                pos = Pos(r, c)
                if self.hasPiece(pos, "*"):
                    return pos

    def getNeutronBackLine(self):
        posNeutron = self.getNeutron()
        if posNeutron.r == 1:
            return "X"
        elif posNeutron.r == 5:
            return "O"
        else:
            return " "

    def isNeutronBlocked(self):
        posNeutron = self.getNeutron()
        for dir in allDirs():
            if self.canMove(posNeutron, dir):
                return False

        return True

    