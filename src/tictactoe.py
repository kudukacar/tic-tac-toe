from .display import Display
from .presenter import Presenter
import sys

class TicTacToe:
    def __init__(self, display, presenter):
        self.display = display
        self.presenter = presenter

    def run(self):
        self.display.output(self.presenter.display_board())


if __name__ == "__main__":
    display = Display(sys.stdout)
    presenter = Presenter()
    tictactoe = TicTacToe(display, presenter)
    tictactoe.run()
