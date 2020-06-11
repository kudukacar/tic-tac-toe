class Board:
    def __init__(self):
        self.board = [None for x in range(10)]

    def place(self, position, token):
        self.board.insert(position - 1, token)

    def get(self, position):
        return self.board[position - 1]