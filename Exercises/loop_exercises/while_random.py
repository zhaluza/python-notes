# Use a while loop to generate a random number between 1 and 10 until you get the number 5. Every time the loop runs, increment the variable i.

# Generate a random number between 1 & 10 using randint(1, 10), storing the result in the number variable
# Write a while loop to keep regenerating a new random number between 1 & 10 while the random number is not equal to 5
# Add 1 to i each time through the loop
from random import randint

number = 0
i = 0
while number != 5:
    number = randint(1, 10)
    i += 1
