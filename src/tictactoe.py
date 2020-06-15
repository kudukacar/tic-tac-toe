from .display import Display
from .presenter import Presenter
from .player import Player
from .board import Board
from sys import stdin, stdout


class TicTacToe:
    def __init__(self, display, presenter, players, board):
        self.display = display
        self.presenter = presenter
        self.players = players
        self.board = board

    def run(self):
        self.show_board()
        self.play_turn(self.players[0])
        self.show_board()
        self.play_turn(self.players[1])
        self.show_board()

    def play_turn(self, player):
        selection = player.get_selection(self.display, self.board)
        self.board.place(selection, player.token)

    def show_board(self):
        self.display.output(self.presenter.display_board(self.board))


if __name__ == "__main__":
    display = Display(stdout)
    presenter = Presenter()
    board = Board()
    first_player = Player("X")
    second_player = Player("O")
    players = [first_player, second_player]
    tictactoe = TicTacToe(display, presenter, players, board)
    tictactoe.run()
