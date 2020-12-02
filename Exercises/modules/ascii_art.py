from pyfiglet import figlet_format
from termcolor import colored

# Gather user input
print('What message do you want to print?')
message = input()
print('What color?')
user_color = input()

# Process user input 
message = pyfiglet.figlet_format(message)

termcolors = ['grey', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
if user_color == 'gray':
    user_color = 'grey'
if(user_color not in termcolors):
    user_color = 'green'

print(colored(message, color=user_color))