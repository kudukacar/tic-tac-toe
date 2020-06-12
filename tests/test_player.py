from src.player import Player


class InputOutputDisplay:
    def __init__(self, inputs):
        self.outputs = ""
        self.inputs = inputs

    def output(self, message):
        self.outputs += message

    def input(self):
        return self.inputs.pop(0)


class TestUser:
    def test_get_input(self):
        display = InputOutputDisplay(["?", "10", "1"])
        player = Player()

        assert player.get_selection(display) == 1
