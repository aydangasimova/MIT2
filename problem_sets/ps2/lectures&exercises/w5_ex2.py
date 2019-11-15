import random

def genEven():
    '''
    Returns a random even number x, where 0 <= x < 100
    '''
    even_numbers = []

    for n in range(100):
        if n % 2 == 0:
            even_numbers.append(n)

    random_numbers = []

    for i in range(len(even_numbers)):
        random_numbers.append(random.choice(even_numbers))

    return random_numbers

generated = genEven()




