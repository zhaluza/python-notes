from random import random


def flip_coin():
    # note: 'random' generates num between 0 and 1

    # generate random number (0-1) using 'random'
    # return 'heads' or 'tails' depending on whether it's closer to 0 or 1
    if random() > 0.5:
        return 'heads'
    else:
        return 'tails'


print(flip_coin())
