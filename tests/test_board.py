from src.board import Board


class TestBoard:
    def test_place(self):
        board = Board()

        board.place(1, "X")

        assert board.get(1) == "X"
        assert board.get(2) == None
