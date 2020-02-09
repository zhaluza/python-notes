from random import randint

# Rock beats scissors
# Scissors beat paper
# Paper beats rock

print('Rock Paper Scissors time!')
print('Player 1 goes first:')
player1 = input().lower()

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
    elif computer == 'paper':
        print('Computer wins!')
elif player1 == 'paper':
    if computer == 'rock':
        print('You win!')
    elif computer == 'scissors':
        print('Computer wins!')
elif player1 == 'scissors':
    if computer == 'paper':
        print('You win!')
    elif computer == 'rock':
        print('Computer wins!')
else:
    print('Something went wrong...\nMake sure you typed your choice correctly.')
