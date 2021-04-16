import math
import random
class Player:
    def __init__(self, letter):
        self.letter = letter
    
    def get_move(self):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square

class HumanPLayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + " Enter square from (0-8):")
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("Invalid square, Try again.")
        return val

class GeniusComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choices(game.available_moves())
        else:
            square = self.minimax(game, self.letter)['position']
        return square

    def minimax(self, game_state, player):
        max_player = self.letter
        other_player = 'O' if player == 'X' else 'X'
        
        if game_state.current_winner == other_player:
            return {
                'position': None,
                'score'   : 1*(game_state.num_empty_squares() + 1) if other_player == max_player else -1*(game_state.num_empty_squares() + 1)
            }
        
        elif not game_state.empty_squares():
            return {
                'position' : None,
                "score"    : 0
            }
        
        if player == max_player:
            best = {'position': None, 'score': -math.inf} 
        else:
            best = {'position': None, 'score': math.inf}

        for possible_moves in game_state.available_moves():
            game_state.make_move(possible_moves, player)

            sim_score = self.minimax(game_state, other_player)

            game_state.board[possible_moves] = ' '
            game_state.current_winner = None
            sim_score['position'] = possible_moves

            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score

        return best