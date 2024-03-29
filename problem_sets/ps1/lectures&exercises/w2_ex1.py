class Item(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = float(v)
        self.weight = float(w)

    def getName(self):
        return self.name

    def getValue(self):
        return self.value

    def getWeight(self):
        return self.weight

    def __str__(self):
        return '<' + self.name + ', ' + str(self.value) + ', ' \
               + str(self.weight) + '>'


def buildItems():
    return [Item(n, v, w) for n, v, w in (('clock', 175, 10),
                                          ('painting', 90, 9),
                                          ('radio', 20, 4),
                                          ('vase', 50, 2),
                                          ('book', 10, 1),
                                          ('computer', 200, 20))]


def buildRandomItems(n):
    return [Item(str(i), 10 * random.randint(1, 10), random.randint(1, 10))
            for i in range(n)]


def powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        combo = []
        for j in range(N):
            # test bit jth of integer i
            if (i // 2**j) % 2 == 1:
                combo.append(items[j])
                print('appending', items[j])
        yield combo

my_gen = powerSet([1,2,3])

for i in my_gen:
     print(i)
'''
def yieldAllCombos(items):
    """
        Generates all combinations of N items into two bags, whereby each
        item is in one or zero bags.

        Yields a tuple, (bag1, bag2), where each bag is represented as a list
        of which item(s) are in each bag.
    # """
    # generate all combinations of N items into two bags
    N = len(items)
    for i in range(3**N):
        bag1 = []
        bag2 = []
        for j in range(N):
            # test bit jth of integer i
            # if
                bag1.append(items[j])
            # if
                bag2.append(items[j])
            combo = (bag1, bag2)
    yield combo


# my_gen2 = yieldAllCombos(['a','b'])
#
# count = 0
# for i in my_gen2:
#     print(i)
#     count += 1
'''
print("---------------------")


def yieldAllCombos(items):
    N = len(items)
    # enumerate the 3**N possible combinations
    for i in range(3**N):
        bag_1 = []
        bag_2 = []
        for j in range(N):
            # test bit jth of integer i
            if (i // 3**j) % 3 == 0:
                bag_1.append(items[j])
            elif (i // 3**j) % 3 == 1:
                bag_2.append(items[j])
        yield (bag_1, bag_2)


my_gen = yieldAllCombos([1, 2])

count = 0
for i in my_gen:
    print(i)
    count += 1

print(count)


def f2(items):
    N = len(items)