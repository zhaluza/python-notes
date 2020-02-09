# Rock beats scissors
# Scissors beat paper
# Paper beats rock

print('Rock Paper Scissors time!')
print('Player 1 goes first:')
player1 = input().lower()
print('NO CHEATING\n\n' * 20)
print('Player 2\'s turn:')
player2 = input().lower()

print('Shoot!')

# Conditional logic
if player1 == player2:
    print('It\'s a tie!')
elif player1 == 'rock':
    if player2 == 'scissors':
        print('Player 1 wins!')
    elif player2 == 'paper':
        print('Player 2 wins!')
elif player1 == 'paper':
    if player2 == 'rock':
        print('Player 1 wins!')
    elif player2 == 'scissors':
        print('Player 2 wins!')
elif player1 == 'scissors':
    if player2 == 'paper':
        print('Player 1 wins!')
    elif player2 == 'rock':
        print('Player 2 wins!')
else:
    print('Something went wrong!')
