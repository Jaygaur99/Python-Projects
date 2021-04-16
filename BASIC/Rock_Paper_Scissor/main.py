import random

def play():
    user = input("What's your choice 'r' for rock, 'p' for paper and 's' for scissors: ")
    computer = random.choice(['r','p','s'])
    if user == computer:
        return 'tie'
    if is_win(user, computer):
        return 'You Won'
    return "You Lost"

def is_win(player,computer):
    #return true if player wins
    if (player == 'r' and computer == 's') or (player == 's' and computer == 'p') or (player == 'p' and computer == 'r'):
        return True

print(play())