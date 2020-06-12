from .display import Display
from .presenter import Presenter
from .player import Player
from .board import Board
import sys


class TicTacToe:
    def __init__(self, display, presenter, player, board):
        self.display = display
        self.presenter = presenter
        self.player = player
        self.board = board

    def run(self):
        self.show_board()
        self.play_turn()
        self.show_board()

    def play_turn(self):
        selection = self.player.get_selection(self.display)
        self.board.place(selection, "X")

    def show_board(self):
        self.display.output(self.presenter.display_board(self.board))


if __name__ == "__main__":
    display = Display(sys.stdout, sys.stdin)
    presenter = Presenter()
    board = Board()
    player = Player()
    tictactoe = TicTacToe(display, presenter, player, board)
    tictactoe.run()
