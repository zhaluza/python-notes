# Create a game in which the computer randomly chooses a number between 1 and 10 (can also expand this to include any number)
# If player guesses too high, tell them they're too high. Too low — tell them they're too low
# If they guess correctly, tell them they win, and ask if they want to play again (y/n)
# Break on 'no'

import random

random_number = random.randint(1, 10)
guess = None

while True:
    guess = input('Guess a number between 1 & 10: ')
    guess = int(guess)

    if guess > random_number:
        print('Too high! Guess again')
    elif guess < random_number:
        print('Too low! Guess again')
    else:
        print(f'Congrats! The number was {random_number}!')
        play_again = input('Do you want to play again? (y/n) ')
        play_again = play_again.lower()
        if play_again == 'y':
            random_number = random.randint(1, 10)
            guess = None

        else:
            print('Thanks for playing!')
            break
