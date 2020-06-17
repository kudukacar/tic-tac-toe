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
        self.count = 0

    def run(self):
        self.show_board()
        while self.board.draw() == False and self.board.winner() == None:
            self.play_turn()
            self.show_board()

    def play_turn(self):
        player = self.players[self.count % 2]
        selection = player.get_selection(self.display, self.board)
        self.board.place(selection, player.token)
        self.count += 1

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
