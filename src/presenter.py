class Presenter:
    def display_board(self, board):
        return f"""
         {board.get(1) or " "} | {board.get(2) or " "} | {board.get(3) or " "} 
        ---+---+---
         {board.get(4) or " "} | {board.get(5) or " "} | {board.get(6) or " "} 
        ---+---+---
         {board.get(7) or " "} | {board.get(8) or " "} | {board.get(9) or " "} 
        """ + self.display_outcome(board)

    def display_outcome(self, board):
        if board.draw():
            return "Draw!"
        elif winner := board.winner():
            return f"{winner} Wins!"
        else:
            return ""
