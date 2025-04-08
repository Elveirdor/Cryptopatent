class ChessGame:
    def __init__(self):
        self.board = self.initialize_board()

    def initialize_board(self):
        board = []
        for i in range(8):
            row = []
            for j in range(8):
                if i == 1:
                    row.append('P')
                elif i == 6:
                    row.append('p')
                elif i == 0:
                    if j in [0, 7]:
                        row.append('R')
                    elif j in [1, 6]:
                        row.append('N')
                    elif j in [2, 5]:
                        row.append('B')
                    elif j == 3:
                        row.append('Q')
                    elif j == 4:
                        row.append('K')
                elif i == 7:
                    if j in [0, 7]:
                        row.append('r')
                    elif j in [1, 6]:
                        row.append('n')
                    elif j in [2, 5]:
                        row.append('b')
                    elif j == 3:
                        row.append('q')
                    elif j == 4:
                        row.append('k')
                else:
                    row.append('-')
            board.append(row)
        return board

    def print_board(self):
        for row in self.board:
            print(' '.join(row))

chess_game = ChessGame()
chess_game.print_board()
