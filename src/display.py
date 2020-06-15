class Display:
    def __init__(self, stdout):
        self.stdout = stdout

    def output(self, message):
        self.stdout.write(f'{message}\n')

    def input(self):
        return input()
