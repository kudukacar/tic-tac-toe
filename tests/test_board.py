from src.board import Board


class TestBoard:
    def test_place(self):
        board = Board()

        board.place(1, "X")

        assert board.get(1) == "X"
        assert board.get(2) == None

    def test_winner(self):
        board = Board()

        board.place(1, "X")
        board.place(4, "X")
        board.place(7, "X")

        assert board.winner() == "X"

    def test_no_winner(self):
        board = Board()

        assert board.winner() == None

    def test_draw(self):
        board = Board()
        board.place(1, "X")
        board.place(2, "X")
        board.place(3, "O")
        board.place(4, "O")
        board.place(5, "O")
        board.place(6, "X")
        board.place(7, "X")
        board.place(8, "O")
        board.place(9, "X")

        assert board.draw() == True
