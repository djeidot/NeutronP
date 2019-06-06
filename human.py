from player import Player
from position import Pos
from exceptions import MoveError

class Human(Player):

    def moveNeutron(self):
        inp = input("Player " + self.playerPiece + " move neutron (direction only, e.g. 'NE'): ")

        try:
            self.board.move(self.board.getNeutron(), "*", inp)
        except TypeError as e1:
            print(str(e1))
            self.moveNeutron()
        except MoveError as e2:
            print(str(e2))
            self.moveNeutron()

    def movePlayerPiece(self):
        inp = input("Player " + self.playerPiece + " move piece (position + direction, e.g. 'A1 NE'): ")

        try:
            pos = Pos.parse(inp[0:2])
            dir = inp[3:].rstrip()
            self.board.move(pos, self.playerPiece, dir)
        except TypeError as e1:
            print(str(e1))
            self.movePlayerPiece()
        except MoveError as e2:
            print(str(e2))
            self.movePlayerPiece()
