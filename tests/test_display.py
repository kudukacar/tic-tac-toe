import pytest
from src.display import Display

class FakeStdout:
    def __init__(self):
        self.log = ""

    def write(self, message):
        self.log += message

class TestDisplay:
    def test_output(self):
        stdout = FakeStdout()
        message = "Welcome to Tic-Tac-Toe"
        display = Display(stdout)

        display.output(message)
        
        assert stdout.log == f'{message}\n'