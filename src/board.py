class Board:
    def __init__(self):
        self.board = [None for x in range(9)]

    def place(self, position, token):
        self.board[position - 1] = token

    def get(self, position):
        return self.board[position - 1]

    def draw(self):
        no_winner = self.winner() == None
        board_full = not(None in self.board)
        return no_winner and board_full

    def winner(self):
        winning_lines = self.rows() + self.columns() + self.diagonals()
        winning_line = list(filter(lambda line: (self.get(line[0]) == self.get(
            line[1]) == self.get(line[2])) and self.get(line[0] != None), winning_lines))
        if len(winning_line) > 0:
            return self.get(winning_line[0][0])
        else:
            return None

    def rows(self):
        return [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    def columns(self):
        return [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

    def diagonals(self):
        return [[1, 5, 9], [3, 5, 7]]
