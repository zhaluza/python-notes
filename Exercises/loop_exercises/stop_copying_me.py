# Repeat everything until the user types 'stop copying me'
msg = input('Hey, how\'s it going? ')
while msg.lower() != 'stop copying me':
    msg = input(f'{msg}\n')
print('Fine, you win!')

# Slightly longer version:
# while msg.lower() != 'stop copying me':
#     print(msg)
#     msg = input()
# print('Fine, you win!')
