import math
import random
import time
from time import time
class Player:
    def __init__(self, letter):
        # Letter is X or O
        self.letter = letter

    # we want all platers to get their next move given a game
    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\' s turn. Input move(0-8):')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("Invalid Square. Try again")
        return val

class GeniusComputerPlayer(Player):
    def __init__(self,letter):
        super().__init__(letter)

    def get_move(self, game):
        init = time()
        #if len(game.available_moves()) == 9:
        #square = random.choice(game.available_moves())
        #else:
            # Get the square based on minimax algorithm
        square = self.minimax(game, self.letter)['position']
        print(f"Time Taken by AI: {time()-init:.20}")
        return square
    
    def minimax(self, state, player):
        max_player = self.letter # Yourself
        other_player = 'O' if player == 'X' else 'X'

        # first we want to check if the previous move is a winner
        # This is our base case

        if state.current_winner == other_player:
            # we should return position and score because we need to keep track of the score
            # for minimax to work
            return {
                'position': None,
                'score': 1 * (state.num_empty_squares()+ 1) if other_player == max_player else -1 * (state.num_empty_squares()+ 1)
            }
            
        elif not state.empty_squares(): # No empty squares
            return {'position': None, 'score': 0}
        
        if player == max_player:
            best = {'position': None, 'score': -math.inf} # Each score should maximize
        else:
            best = {'position': None, 'score': math.inf} # Each score should minimize

        for possible_move in state.available_moves():
            # step 1: make a move, try that spot
            state.make_move(possible_move, player)

            # step 2: recurse using minimax to simulate a game after making that move
            sim_score = self.minimax(state, other_player) # now we alternate player

            # step 3: undo the move and
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move
            
            # step 4: Update the dictionary if necessary
            if player == max_player: # We are trying to maximize the max_player
                if sim_score['score'] > best['score']:
                    best = sim_score # replace best
            else: # but minimize the other player
                if sim_score['score'] < best['score']:
                    best = sim_score # replace best 

        return best