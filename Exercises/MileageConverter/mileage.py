print('How many kilometers did you cycle today?')
# prompts the user to enter something & waits for them to hit the return key
kms = input()
miles = float(kms) / 1.609344
miles = round(miles, 2)
print(f'OK, you said you cycled {kms} kilometers, or {miles} miles!')
