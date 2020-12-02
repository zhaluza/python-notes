from pyfiglet import figlet_format
from termcolor import colored

def print_ascii_art(msg, color): 
    msg = figlet_format(msg)

    valid_colors = ['grey', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
    if color == 'gray':
        color = 'grey'
    if(color not in valid_colors):
        color = 'green'

    print(colored(msg, color=color))

# Gather user input
message = input('What message do you want to print?')
user_color = input('What color?')

# Process user input
print_ascii_art(message, user_color)