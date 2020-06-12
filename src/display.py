class Display:
    def __init__(self, stdout, stdin):
        self.stdout = stdout
        self.stdin = stdin

    def output(self, message):
        self.stdout.write(f'{message}\n')

    def input(self):
        self.stdin.readline()
