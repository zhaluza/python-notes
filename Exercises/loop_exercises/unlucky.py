# INSTRUCTIONS
# Loop through numbers 1-20

# for 4 & 13, print 'x is unlucky'
# for even numbers, print 'x is even'
# for odd numbers, print 'x is odd'

############

# FIRST SOLUTION
# for num in range(1, 21):
#     if num == 4 or num == 13:
#         print(f'{num} is unlucky')
#     elif num % 2 == 0:
#         print(f'{num} is even')
#     else:
#         print(f'{num} is odd')

# The above solution works perfectly, but it's a bit repetitive (lots of print commands!)
# Here's a cleaner version:

for num in range(1, 21):
    if num == 4 or num == 13:
        state = 'unlucky'
    elif num % 2 == 0:
        state = 'even'
    else:
        state = 'odd'
    print(f'{num} is {state}')
