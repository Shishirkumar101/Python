from random import randint

EASY_TURN = 10
HARD_TURN = 5

def set_difficulty(mode):
    if mode == 'easy':
        return EASY_TURN
    else:
        return HARD_TURN

def check_answer(guess_number , actual_number , turn):
    if guess_number > actual_number:
        print("Too high.")
        return turn-1
    elif guess_number < actual_number:
        print("Too low")
        return turn-1
    else:
        print(f"You got it! The answer was {actual_number}.")
        
def guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    answer = randint(1, 100)
    guess = 0

    game_mode = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    turn = set_difficulty(game_mode)

    while(guess != answer):
        print(f"You have {turn} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turn = check_answer(guess , answer , turn)
        if turn == 0 :
            print("You've run out of guesses. Refresh the page to run again.")
            return
        elif guess != answer:
            print("Guess again.")

guessing_game()