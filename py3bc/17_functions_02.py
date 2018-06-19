from random import random

def coin_toss():
    if random() > 0.5:
        return 'heads'
    else:
        return 'tails'


print(coin_toss())
