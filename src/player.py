class Player:
    def get_selection(self, display):
        while True:
            display.output('Please select your move[1,9]')
            try:
                input = int(display.input().strip())
            except:
                input = 0

            if input in range(1, 10):
                return input
            else:
                display.output('Invalid entry')
