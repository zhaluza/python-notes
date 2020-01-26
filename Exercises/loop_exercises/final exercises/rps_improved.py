from random import randint

# Rock beats scissors
# Scissors beat paper
# Paper beats rock

player_wins = 0
computer_wins = 0

# Change to customize length of game
winning_score = 3

while player_wins < winning_score and computer_wins < winning_score:

    print(f'Computer: {computer_wins}')
    print(f'You: {player_wins}')
    print('Choose rock, paper, or scissors (type "quit" to stop)')
    print('')
    print('Player 1 goes first:')
    player1 = input().lower()
    if player1 == 'quit' or player1 == 'q':
        break

    computer = randint(0, 2)
    if computer == 0:
        computer = 'rock'
    elif computer == 1:
        computer = 'paper'
    else:
        computer = 'scissors'

    print(f'Computer plays {computer}')

    # Conditional logic
    if player1 == computer:
        print('It\'s a tie!')
    elif player1 == 'rock':
        if computer == 'scissors':
            print('You win!')
            player_wins += 1
        elif computer == 'paper':
            print('Computer wins!')
            computer_wins += 1
    elif player1 == 'paper':
        if computer == 'rock':
            print('You win!')
            player_wins += 1
        elif computer == 'scissors':
            print('Computer wins!')
            computer_wins += 1
    elif player1 == 'scissors':
        if computer == 'paper':
            print('You win!')
            player_wins += 1
        elif computer == 'rock':
            print('Computer wins!')
            computer_wins += 1
    else:
        print('Something went wrong...\nMake sure you typed your choice correctly.')
print('FINAL SCORE:')
print(f'Computer {computer_wins}, Player {player_wins}')
if player_wins > computer_wins and player_wins < winning_score:
    print('You were so close!')
elif player_wins > computer_wins:
    print('Great job!')
elif player_wins == computer_wins:
    print('It\'s a tie!')
else:
    print('Better luck next time!')
