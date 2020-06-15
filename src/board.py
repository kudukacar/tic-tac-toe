class Board:
    def __init__(self):
        self.board = [None for x in range(9)]

    def place(self, position, token):
        self.board.insert(position - 1, token)

    def get(self, position):
        return self.board[position - 1]
