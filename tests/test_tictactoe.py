import pytest
from src.tictactoe import TicTacToe


class LetterPresenter:
    def display_board(self, board):
        return "".join([board.get(i) for i in range(1, 10)])


class BoardWithOutcomes:
    def __init__(self):
        self.board = ["-" for x in range(9)]

    def place(self, position, token):
        self.board.insert(position - 1, token)

    def get(self, position):
        return self.board[position - 1]


class OutputDisplay:
    def __init__(self):
        self.outputs = []

    def output(self, message):
        self.outputs.append(message)


class PlayerWithMoves:
    def __init__(self, move, token):
        self.move = move
        self.token = token

    def get_selection(self, display, board):
        return self.move


class TestTicTacToe:
    def test_run(self):
        display = OutputDisplay()
        presenter = LetterPresenter()
        board = BoardWithOutcomes()
        first_player = PlayerWithMoves(1, "X")
        second_player = PlayerWithMoves(2, "O")
        players = [first_player, second_player]

        TicTacToe(display, presenter, players, board).run()

        expected_boards = [
            "---------",
            "X--------",
            "XO-------"
        ]

        assert display.outputs == expected_boards
