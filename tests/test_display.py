from src.display import Display


class StdoutLogger:
    def __init__(self):
        self.log = ""

    def write(self, message):
        self.log += message


class StdinInputer:
    def __init__(self, input):
        self.input = input
        self.stripped_input = ""

    def readline(self):
        self.stripped_input += self.input


class TestDisplay:
    def test_output(self):
        stdout = StdoutLogger()
        stdin = StdinInputer("Welcome to Tic-Tac-Toe\n")
        message = "Welcome to Tic-Tac-Toe"
        display = Display(stdout, stdin)

        display.output(message)

        assert stdout.log == f'{message}\n'

    def test_input(self):
        stdin = StdinInputer("Welcome to Tic-Tac-Toe\n")
        stdout = StdoutLogger()
        display = Display(stdout, stdin)

        display.input()

        assert "Welcome to Tic-Tac-Toe\n" == stdin.stripped_input
