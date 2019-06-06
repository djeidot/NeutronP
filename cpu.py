from player import Player
from position import Pos
from direction import allDirs
from random import choice

class Cpu(Player):

    def moveNeutron(self):
        posNeutron = self.board.getNeutron()
        moves = self.getPossibleMoves(posNeutron)
        dir = choice(moves)
        print("Player " + self.playerPiece + " moving neutron to " + dir)
        self.board.move(posNeutron, "*", dir)

    def movePlayerPiece(self):
        poss = self.getPlayerPositions()
        pos = choice(poss)
        moves = self.getPossibleMoves(pos)
        dir = choice(moves)
        print("Player " + self.playerPiece + " moving piece " + pos.toString() + " to " + dir)
        self.board.move(pos, self.playerPiece, dir)

    def getPossibleMoves(self, pos):
        moves = []
        for dir in allDirs():
            if self.board.canMove(pos, dir):
                moves.append(dir)
        
        return moves

    def getPlayerPositions(self):
        poss = []
        for r in range(1, 6):
            for c in range(1, 6):
                pos = Pos(r, c)
                if self.board.hasPiece(pos, self.playerPiece):
                    poss.append(pos)
        
        return poss