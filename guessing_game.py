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
    secret_number_min = 1
    secret_number_max = 10
    secret_number = random.randint(secret_number_min, secret_number_max)
    # Used https://docs.python.org/3.1/library/random.html to find randint method
    scores = []

    def number_game():
        times_guessed = 0
        while True:
            try:
                guessed_number = int(input("\nGuess a number between {} and {}\n> ".format(secret_number_min,secret_number_max)))
                if guessed_number < secret_number_min or guessed_number > secret_number_max:
                    raise ValueError("The number you've entered is outside the range.")
            except ValueError as err:
                print("Something went wrong. Try again!")
                print(err)
            else:
                if guessed_number == secret_number:
                    print("You got it!")
                    times_guessed += 1
                    print("Your score is {}.".format(times_guessed))
                    break
                elif guessed_number > secret_number:
                    print("Too high! Try again!")
                    times_guessed += 1
                    continue
                elif guessed_number < secret_number:
                    times_guessed += 1
                    print("Too low! Try again!")
                    continue
        return times_guessed

    def highest_score(all_scores):
        highest = secret_number_max
        for min_score in all_scores:
            if min_score < highest:
                highest = min_score
        return highest

    print("""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

I've picked a number between {} and {}.
You've got to guess it. Let's begin!
    """.format(secret_number_min, secret_number_max))
    score = number_game()
    scores.append(score)

    while True:
        play_again = input("\nWould you like to play again? (Y/N)\n> ")
        if play_again.lower() != 'y' and play_again.lower() != 'n':
            print("Whoops! That isn't the right command.")
            continue
        if play_again.lower() == "y":
            print("\nThe current high score is {}".format(highest_score(scores)))
            # Found min solution from https://stackoverflow.com/questions/2622994/python-finding-lowest-integer
            secret_number = random.randint(1, 10)
            score = number_game()
            scores.append(score)
            continue
        elif play_again.lower() == 'n':
            print("\nThanks for playing!")
            break


if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
