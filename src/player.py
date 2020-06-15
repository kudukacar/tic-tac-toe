class Player:
    def __init__(self, token):
        self.token = token

    def get_selection(self, display, board):
        while True:
            display.output('Please select your move[1,9]')
            try:
                input = int(display.input().strip())
            except:
                input = 0

            if self.validate_range(display, input) and self.validate_availability(display, input, board):
                return input

    def validate_range(self, display, selection):
        if selection in range(1, 10):
            return selection
        else:
            display.output('Invalid entry')

    def validate_availability(self, display, selection, board):
        if board.get(selection):
            display.output('Selection taken')
        else:
            return selection
