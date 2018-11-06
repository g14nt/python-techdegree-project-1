"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random

def start_game():
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.

    secret_number = random.randint(1, 10)
    scores = []

    def number_game():
        times_guessed = 0
        guessed_number = int(input("Guess a number between 1 and 10\n> "))
        while True:
            if guessed_number == secret_number:
                print("You did it!")
                times_guessed += 1
                break
            elif guessed_number > secret_number:
                print("Too high! Guess Again:")
                times_guessed += 1
                guessed_number = int(input("> "))
                continue
            elif guessed_number < secret_number:
                times_guessed += 1
                print("Too low! Guess Again:")
                guessed_number = int(input("> "))
                continue
        return times_guessed

    print("""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
    """)
    score = number_game()
    scores.append(score)

    while True:
        print("Your score is {}.".format(score))
        play_again = input("\nWould you like to play again? (Y/N)\n> ")
        if play_again.lower() == "y":
            print("\nThe current high score is {}".format(min(scores)))
            # Found min solution for list from https://stackoverflow.com/questions/3090175/python-find-the-greatest-number-in-a-list-of-numbers
            secret_number = random.randint(1, 10)
            score = number_game()
            scores.append(score)
            continue
        elif play_again.lower() == 'n':
            print("Thanks for playing!")
            break





if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
