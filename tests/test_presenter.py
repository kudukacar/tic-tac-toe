import pytest
from src.presenter import Presenter


class BoardWithOneValue:
    def get(self, position):
        return "X"


class TestPresenter:
    def test_display_board(self):
        presenter = Presenter()
        expected_board = """
         X | X | X 
        ---+---+---
         X | X | X 
        ---+---+---
         X | X | X 
        """

        assert presenter.display_board(BoardWithOneValue()) == expected_board
