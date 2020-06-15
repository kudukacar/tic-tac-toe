from src.player import Player


class InputOutputDisplay:
    def __init__(self, inputs):
        self.outputs = ""
        self.inputs = inputs

    def output(self, message):
        self.outputs += message

    def input(self):
        return self.inputs.pop(0)


class BoardWithOneAvailable:
    def get(position):
        if position == 1:
            return False
        else:
            return True


class TestUser:
    def test_get_input(self):
        display = InputOutputDisplay(["?", "10", "2", "1"])
        board = BoardWithOneAvailable
        player = Player("X")

        assert player.get_selection(display, board) == 1
