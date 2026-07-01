import random
def coin_flip(coin_side):
    if coin_side == 0:
        return 'Its Head.'
    return 'Its Tail.'
r = random.randint(0,1)
results = coin_flip(r)
print(results)