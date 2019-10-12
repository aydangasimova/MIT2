###########################
# 6.0002 Problem Set 1b: Space Change
# Name:
# Collaborators:
# Time:
# Author: charz, cdenise

#================================
# Part B: Golden Eggs
#================================



# Problem 1
def dp_make_weight_norm(egg_weights, target_weight, memo = {}):
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always a egg of value 1.
    
    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)
    
    Returns: int, smallest number of eggs needed to make target weight
    """

    eggs_taken_sum = 0
    egg_weights = sorted(list(egg_weights), reverse=True)

    factors = []
    for i in range(len(egg_weights)):
        factor = 0
        while eggs_taken_sum + egg_weights[i] <= target_weight:
            eggs_taken_sum += egg_weights[i]
            factor += 1
        factors.append(factor)

    eggs_taken_factors = list(zip(egg_weights, factors))
    min_factors = reduce(lambda x, y: x + y, factors)
    print("eggs taken combo is ", eggs_taken_factors)

    return print("smallest number of eggs needed to make target weight is ", min_factors)


def dp_make_weight_norm2(egg_weights, target_weight, memo={}):
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always a egg of value 1.

    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)

    Returns: int, smallest number of eggs needed to make target weight
    """
    egg_weights = sorted(list(egg_weights), reverse=True)

    factors = []
    avail_weight = target_weight

    while avail_weight != 0:
        for i in range(len(egg_weights)):
            factor = avail_weight//egg_weights[i]
            avail_weight = avail_weight-factor*egg_weights[i]
            factors.append(factor)

    eggs_taken_factors = list(zip(egg_weights, factors))
    min_factors = reduce(lambda x, y: x + y, factors)
    print("eggs taken combo is ", eggs_taken_factors)

    return print("smallest number of eggs needed to make target weight is ", min_factors)


def dp_make_weight_dyn1(egg_weights, target_weight, memo={}):

    egg_weights = sorted(list(egg_weights), reverse=True)
    print("egg weights is ", egg_weights)
    avail_weight = target_weight

    if avail_weight == 0:
        # eggs_taken_factors = list(zip(egg_weights, factors))
        # print("eggs taken combo is ", eggs_taken_factors)
        print("smallest number of eggs needed to make target weight is \n")
        return 0

    elif len(egg_weights) == 0:
        return 0

    else:
        factor = avail_weight // egg_weights[0]
        print("avail weight before subtr is ", avail_weight)
        print("factor is", factor, "first el in egg weights is ", egg_weights[0])
        avail_weight = avail_weight - factor*egg_weights[0]
        print("avail weight after subtr is ", avail_weight)

        return factor + dp_make_weight_dyn1(egg_weights[1:], avail_weight)



def dp_make_weight_dyn2(egg_weights, target_weight, memo={}):
    """
        Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
        an infinite supply of eggs of each weight, and there is always a egg of value 1.

        Parameters:
        egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
        target_weight - int, amount of weight we want to find eggs to fit
        memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)

        Returns: int, smallest number of eggs needed to make target weight
        """
    print(memo)
    egg_weights = sorted(list(egg_weights), reverse=True)
    print("egg weights is ", egg_weights)
    avail_weight = target_weight

    if avail_weight == 0:
        print("smallest number of eggs needed to make target weight is \n")
        return sum(memo.values())
    elif len(egg_weights) == 0:
        return 0
    else:
        factor = avail_weight // egg_weights[0]
        memo[egg_weights[0]] = factor
        avail_weight = avail_weight - factor*egg_weights[0]
        return dp_make_weight_dyn2(egg_weights[1:], avail_weight, memo)


# EXAMPLE TESTING CODE, feel free to add more if you'd like
if __name__ == '__main__':
    from functools import reduce
    # egg_weights = (1, 7, 48, 3)
    egg_weights = (1, 5, 10, 25)
    n = 99
    print("Egg weights = (1, 5, 10, 25)")
    print("n = 99")
    print("Expected ouput: 9 (3 * 25 + 2 * 10 + 4 * 1 = 99)")
    print("Actual output:", dp_make_weight_dyn2(egg_weights, n))
    print()