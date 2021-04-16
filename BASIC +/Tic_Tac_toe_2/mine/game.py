from player import HumanPLayer,GeniusComputerPlayer, RandomComputerPlayer
import time
import os

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None
    
    def print_board(self):
        for row in [self.board[j*3: (j+1)*3] for j in range(3)]:
            print(("|" + "|".join(row)+"|").center(50))
    
    @staticmethod
    def print_board_nums():
        num_board = [[str(j) for j in range((i*3),(i+1)*3)] for i in range(3)]
        for row in num_board:
            print(("|" + "|".join(row)+"|").center(50))

    
    def available_moves(self):
        return [i for i,spot in enumerate(self.board) if spot == ' ']
    

    def empty_squares(self):
        return ' ' in self.board
    

    def num_empty_squares(self):
        return self.board.count(' ')


    def make_move(self, square, letter):
        if self.board[square] == " ":
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    

    def winner(self, square, letter):
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind+1)*3]
        if all([spot== letter for spot in row]):
            return True
        # Column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot== letter for spot in column]):
            return True
        # Diagonal
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0,4,8]]
            if all([spot== letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2,4,6]]
            if all([spot== letter for spot in diagonal2]):
                return True
        return False

def play(game, x_player, o_player, print_game=True):
    letter = "X"
    while game.empty_squares():
        if print_game:
            game.print_board_nums()
            print('\n')
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        
        if game.make_move(square, letter):
            if print_game:
                print(letter, "makes a move to square ", square,'\n')
                game.print_board()
                print('\n')
        
            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                    return letter
            
            letter = 'O' if letter == "X" else 'X'
        time.sleep(0.7)
    if print_game:
        print("It's a tie")


if __name__ == "__main__":
    x_player = HumanPLayer('X')
    o_player = GeniusComputerPlayer("O")
    t = TicTacToe()
    play(t, x_player, o_player)