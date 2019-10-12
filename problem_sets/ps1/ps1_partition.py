# From codereview.stackexchange.com                    
def partitions(set_):
    """

    """
    if not set_: # if set is not empty
        yield [] # yield a generator list
        return # stop the function with the above yield
    for i in range(2**len(set_)//2):
        parts = [set(), set()]  # parts consists of two unique sets
        for item in set_:
            parts[i & 1].add(item) # parts index can only equate to parts[0] for the first set and parts[1] for the second set. only 1 & 1 evaluates to 1, in all other values of i, it evaluates to 0
            i >>= 1 #changes i according to some function
        for b in partitions(parts[1]): # for each element of the func called on the second set in parts
            yield [parts[0]]+b #make a list out of the set and add b

def get_partitions(set_):
    for partition in partitions(set_):
        yield [list(elt) for elt in partition]




