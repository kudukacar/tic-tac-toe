import pytest
from src.presenter import Presenter


class TestPresenter:
    def test_display_board(self):
        presenter = Presenter()
        expected_board = """
          |  |
        --+--+--
          |  |
        --+--+--
          |  |
        """
        
        assert presenter.display_board() == expected_board