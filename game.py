from board import Board
from human import Human
from cpu import Cpu
import api
import format

class Game:

    def __init__(self):
        self.board = Board()
        self.playerO = Human("O", self.board)
        self.playerX = Cpu("X", self.board)

    def run(self):
        self.join()
        # self.board.show()
        # gameEnd = False
        # while not gameEnd:
        #     gameEnd = self.playerMove(self.playerO) or self.playerMove(self.playerX)
        # 
        # print("Game Over")

    def join(self):
        gamesPojo = api.getGames()
        print("Here's a list of games to join:")
        print("Game ID         | Player O name | Player X name | Player turn")
        for gameId in gamesPojo:
            gamePojo = gamesPojo[gameId]
            print(gameId + " | "
                  + format.center(gamePojo["playerO"], 13, False) + " | "
                  + format.center(gamePojo["playerX"], 13, False) + " |      "
                  + gamePojo["move"])

        print()










    # private boolean joinGame() {
    #     GamesPojo gamesPojo = api.getGames();
    # List<GamePojo> validGames = new ArrayList<>();
    # 
    # System.out.println("Here's a list of games to join:");
    # System.out.println("Game ID         | Player O name | Player X name | Player turn");
    # for (GamePojo gamePojo : gamesPojo.getGames().values()) {
    # if (gamePojo.getWinner() == null) {
    # validGames.add(gamePojo);
    # System.out.println(gamePojo.getId() + " | "
    # + center(gamePojo.getPlayerO(), 13, false) + " | "
    # + center(gamePojo.getPlayerX(), 13, false) + " |      "
    # + gamePojo.getMove().getMark());
    # }
    # }
    # 
    # while (true) {
    # System.out.print("\nInput the last " + getMinimumGameIdDigits(validGames) + " digits of the game ID: ");
    # String input = scanner.nextLine().trim();
    # for (GamePojo gamePojo : validGames) {
    # if (gamePojo.getId().endsWith(input)) {
    # 
    #     System.out.println("\nInput the type of player for both players (H - Human, C - CPU, R - Remote)");
    # String playerOClass = getPlayerClass("Player O", gamePojo.getPlayerO());
    # String playerXClass = getPlayerClass("Player X", gamePojo.getPlayerX());
    # return startExistingGame(gamePojo, playerOClass, playerXClass);
    # }
    # }
    # 
    # System.out.println("Game with ID ending with " + input + " not identified.");
    # }
    # }


    def playerMove(self, player):
        player.moveNeutron()
        if self.checkNeutronInBackLine():
            return True

        player.movePlayerPiece()
        return self.checkNeutronBlocked(player.playerPiece)

    def other(self, piece):
        if piece == "X":
            return "O"
        elif piece == "O":
            return "X"
        else:
            return piece

    # Checks if the neutron is in one of the back lines.
    # The player whose back line the neutron is on loses
    def checkNeutronInBackLine(self):
        loser = self.board.getNeutronBackLine()
        if loser == "X" or loser == "O":
            winner = self.other(loser)
            print("Neutron is on player " + loser + "'s back line.")
            print("Player" + winner + " wins!!!")
            return True
    
        return False

    # Checks if the neutron is blocked
    # The player to have last played wins
    def checkNeutronBlocked(self, winner):
        if self.board.isNeutronBlocked():
            loser = self.other(winner)
            print("Player " + loser + " cannot move the neutron.")
            print("Player " + winner + " wins!!!")
            return True
        
        return False
