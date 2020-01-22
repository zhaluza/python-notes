# ask for age
print('How old are you?')
age = input()

# 18-21: entry, no wristband
# 21+: wristband
# else: too young!

if age:
    age = int(age)
    if age >= 21:
        print('Here\'s a wristband. Get wasted!')
    elif age >= 18:
        print('Come on in! Can\'t drink, though.')
    else:
        print('Sorry, you\'re too young!')
else:
    print('Please enter a number!')
