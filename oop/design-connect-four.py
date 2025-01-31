# pseudocode for OOP interview for design connect four game

class Game:
    def __init__(self, grid, players):
        self.connectN = 4
        self.grid = grid
        self.players = players

    def checkWin(self):
        # check if connectN pieces are connected horizontally, if yes return 
        # check if connectN pieces are connected vertically, if yes return 
        # check if connectN pieces are connected diagonally (/ or \), if yes return 

    def play(self):
        while True:
            self.playRound()

    def playRound(self):
        for player in players:
            piece = self.playTurn(player)
            self.checkWin(piece)

    def playTurn(self, player):
        return self.grid.placePiece(player, position);

class Grid:
    def __init__(self, height, width): # dependency inversion
        self.height = height
        self.width = width
        self.board = [null for row in range(self.height) for col in range(self.width)]

    def getBoard(self):
        return self.board

    def placePiece(self, player, position):
        # assign position in board to player name
        return position

class Player:
    def __init__(self, name):
        self.score = 0
        self.name = name # assumed to be unique for now
        # could add id, order, rounds played, games won, etc.

# driver code
grid = Grid(6, 7)
players = [Player('A'), Player('B')]
connectFourGame = Game(grid, players)
connectFourGame.play()
