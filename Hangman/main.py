import time
import random
import os

def title():
    print("Welcome to the Hangman Game")
    name = input("Please Enter your name: ")
    print(f"Welcome {name} to the game, Best Of Luck!")
    time.sleep(2)
    print("The Game is about to start")
    time.sleep(3)


def hangMan():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit = 5
    print("This is hangman word "+display)
    guess = input("Enter your guess: ")
    os.system('cls')
    guess = guess.strip().lower()
    if len(guess) >= 2 or len(guess) <= 0:
        print("Invalid Input")
        hangMan()
    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_"+ word[index+1:]
        display = display[:index] + guess + display[index+1:]
        print(display)
        print()
    elif guess in already_guessed:
        print("already guessed")
    else:
        count += 1
        if count == 1:
            time.sleep(1)
            print("""  
                                            ---------
                                            |       
                                            |       
                                            |       
                                            |    
                                            |    
                                            |    
                                            |                 
                                        ____|____         
                                    """)
            print("Wrong Guess. "+ str(limit - count)+ " guess reamins" )
        elif count == 2:
            time.sleep(1)
            print("""  
                                        ---------
                                        |       |
                                        |       |
                                        |       |
                                        |
                                        |
                                        |
                                        |                 
                                    ____|____         
                                """)
            print("Wrong Guess. " + str(limit - count) + " Guess remaining")
        elif count == 3:
            time.sleep(1)
            print("""  
                                        ---------
                                        |       |
                                        |       |
                                        |       |
                                        |       O
                                        |
                                        |
                                        |                 
                                    ____|____         
                                """)
            print("Wrong Guess. " + str(limit - count) + " Guess remaining")
        elif count == 4:
            time.sleep(1)
            print("""  
                                        ---------
                                        |       |
                                        |       |
                                        |       |
                                        |       O
                                        |      /|\\
                                        |       
                                        |                 
                                    ____|____         
                                """)
            print("Wrong Guess. " + str(limit - count) + " Guess remaining")
        elif count == 5:
            time.sleep(1)
            print("""  
                                        ---------
                                        |       |
                                        |       |
                                        |       |
                                        |       O
                                        |      /|\\
                                        |      /|\\
                                        |                 
                                    ____|____         
                                """)
            print("Wrong Guess. You are Hanged")
            print("The Word was: ", word)
            print("You Guessed: ", already_guessed)
            play_loop()
    if word == '_' * length:
        print("Congrats! You won the game")
        play_loop()
    elif count != limit:
        hangMan()

def play_loop():
    global play_game
    play_game = input("Do you want to play again (y/n)").lower()
    while play_game not in ['y','n']:
        play_game = input("Do you want to play again (y/n)").lower()
    if play_game == 'y':
        main()
        hangMan()
    else:
        print("Thank you for playing")
        exit(0)


def main():
    global count
    global word
    global already_guessed
    global length
    global play_game
    global display
    word_to_guess=["january", "border", "image", "film", "promise", "kids", "lungs", "doll",
                      "rhyme", "damage", "plants"]
    word = random.choice(word_to_guess)
    length = len(word)
    already_guessed = []
    display = "_" * length
    count = 0
    play_game = ''

if __name__ == '__main__':
    title()
    main()
    hangMan()