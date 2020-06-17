import pytest
from src.presenter import Presenter


class BoardWithOneValue:
    def __init__(self, draw, winner):
        self.draw_outcome = draw
        self.winner_outcome = winner

    def get(self, position):
        return "X"

    def draw(self):
        return self.draw_outcome

    def winner(self):
        return self.winner_outcome


class TestPresenter:
    def test_display_board_with_no_outcome(self):
        presenter = Presenter()
        board = BoardWithOneValue(False, None)
        expected_board = """
         X | X | X 
        ---+---+---
         X | X | X 
        ---+---+---
         X | X | X 
        """

        assert presenter.display_board(board) == expected_board

    def test_display_board_with_draw_outcome(self):
        presenter = Presenter()
        board = BoardWithOneValue(True, None)
        expected_outcome = "Draw!"
        expected_board = """
         X | X | X 
        ---+---+---
         X | X | X 
        ---+---+---
         X | X | X 
        """

        assert presenter.display_board(
            board) == expected_board + expected_outcome

    def test_display_board_with_draw_outcome(self):
        presenter = Presenter()
        board = BoardWithOneValue(False, "X")
        expected_outcome = "X Wins!"
        expected_board = """
         X | X | X 
        ---+---+---
         X | X | X 
        ---+---+---
         X | X | X 
        """

        assert presenter.display_board(
            board) == expected_board + expected_outcome
