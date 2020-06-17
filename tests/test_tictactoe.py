import pytest
from src.tictactoe import TicTacToe


class LetterPresenter:
    def display_board(self, board):
        return "".join([board.get(i) for i in range(1, 10)])


class BoardWithOutcomes:
    def __init__(self):
        self.board = ["-" for x in range(9)]

    def place(self, position, token):
        self.board[position - 1] = token

    def get(self, position):
        return self.board[position - 1]

    def draw(self):
        if self.board.count("X") < 5:
            return False
        else:
            return True

    def winner(self):
        return None


class OutputDisplay:
    def __init__(self):
        self.outputs = []

    def output(self, message):
        self.outputs.append(message)


class PlayerWithMoves:
    def __init__(self, moves, token):
        self.moves = moves
        self.token = token

    def get_selection(self, display, board):
        return self.moves.pop(0)


class TestTicTacToe:
    def test_run(self):
        display = OutputDisplay()
        presenter = LetterPresenter()
        board = BoardWithOutcomes()
        first_player = PlayerWithMoves([1, 3, 5, 7, 9], "X")
        second_player = PlayerWithMoves([2, 4, 6, 8], "O")
        players = [first_player, second_player]

        TicTacToe(display, presenter, players, board).run()

        expected_boards = [
            "---------",
            "X--------",
            "XO-------",
            "XOX------",
            "XOXO-----",
            "XOXOX----",
            "XOXOXO---",
            "XOXOXOX--",
            "XOXOXOXO-",
            "XOXOXOXOX",
        ]

        assert display.outputs == expected_boards
