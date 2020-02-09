# Rock beats scissors
# Scissors beat paper
# Paper beats rock

print('Rock Paper Scissors time!')
print('Player 1 goes first:')
player1 = input().lower()
print('**NO CHEATING**')
print('**NO CHEATING**')
print('**NO CHEATING**')
print('**NO CHEATING**')
print('**NO CHEATING**')
print('**NO CHEATING**')
print('**NO CHEATING**')
print('**NO CHEATING**')
print('**NO CHEATING**')
print('**NO CHEATING**')
print('**NO CHEATING**')
print('**NO CHEATING**')
print('**NO CHEATING**')
print('**NO CHEATING**')
print('**NO CHEATING**')
print('**NO CHEATING**')
print('**NO CHEATING**')
print('**NO CHEATING**')
print('**NO CHEATING**')
print('**NO CHEATING**')
print('**NO CHEATING**')
print('**NO CHEATING**')
print('**NO CHEATING**')
print('**NO CHEATING**')
print('Player 2\'s turn:')
player2 = input().lower()

print('Shoot!')

# Conditional logic
if player1 == 'rock' and player2 == 'scissors':
    print('Player 1 wins!')
elif player2 == 'rock' and player1 == 'scissors':
    print('Player 2 wins!')
elif player1 == 'scissors' and player2 == 'paper':
    print('Player 1 wins!')
elif player2 == 'scissors' and player1 == 'paper':
    print('Player 2 wins!')
elif player1 == 'paper' and player2 == 'rock':
    print('Player 1 wins!')
elif player2 == 'paper' and player1 == 'rock':
    print('Player 2 wins!')
elif player1 == player2:
    print('It\'s a tie!')
else:
    print('Something went wrong!')
