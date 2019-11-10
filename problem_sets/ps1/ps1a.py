###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name: Aydan Gasimova
# Collaborators: None
# Time:

from ps1_partition import get_partitions
import time
from functools import reduce


#================================
# Part A: Transporting Space Cows
#================================

# Problem 1


def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    with open(filename, 'r') as f:
        lines = f.readlines()
        type(lines)

        cow_dict = {}
        for line in lines:
            line = line.split(",")
            cow_dict[line[0]] = int(line[1].rstrip("\n\r"))

        return cow_dict

# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here

    cowsCopy = sorted(cows, key=cows.get, reverse=True)
    trips = []
    while len(cowsCopy) > 0:
        trip = []
        trip_space = limit
        for i in range(len(cowsCopy)):
            if cows.get(cowsCopy[i]) <= trip_space and any(cowsCopy[i] not in trip for trip in trips):
                trip.append(cowsCopy[i])
                trip_space -= cows.get(cowsCopy[i])

        trips.append(trip)
        cowsCopy = sorted(list(set(cowsCopy)-set(trip)), key=cows.get, reverse=True)
    trips.pop(0)
    return print(trips)

# Problem 3
def brute_force_cow_transport(cows, limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)

    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """

    trip_options = get_partitions(set(cows))
    legal_options = []

    for option in trip_options:
        option_weights = []
        for trip in option:
            trip_weight = 0
            for i in trip:
                trip_weight += cows.get(i)
            option_weights.append(trip_weight)

        if all(trip_weight <= limit for trip_weight in option_weights):
            legal_options.append(option)

    legal_options = sorted(legal_options, key=len, reverse=False)
    min_trips = legal_options[0]

    return min_trips

    # trip_options = get_partitions(set(cows))
    #
    # option_weights = []
    # for option in trip_options:
    #     for trip in option:
    #         in_weights = list(map(lambda x: cows[x], trip))
    #         trip_weight = reduce(lambda x, y: x+y, in_weights)
    #     option_weights.append(trip_weight)
    #
    # trip_options_list = list(get_partitions(set(cows)))
    # print("number of trip options are ", len(trip_options_list))
    #
    # weights_options_list = list(zip(option_weights, trip_options_list))
    # # print(weights_options_list)
    # weights_options_list[0]
    #
    # legal_options = list(filter(lambda x: x[0]<=10, weights_options_list))
    # legal_options = list(map(lambda x: x, [t[1] for t in legal_options]))
    # legal_options = sorted(legal_options, key=len, reverse=False)
    #
    # # print("legal options are \n")
    # # for i in range(10):
    # #     print(legal_options[i])
    #
    # min_trips = legal_options[0]
    #
    # return min_trips

# use a filter function to go through those to select the one with the lowest length option where the weight is below the permitted threshold

# Problem 4

def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.

    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """

    start = time.time()
    cow_dict = load_cows("ps1_cow_data.txt")
    end = time.time()
    print("Loading the cows data takes ", round(end-start, 4), "seconds to run", "\n\n")


    print("Greedy trips are: \n")
    start = time.time()
    greedy_cow_transport(cow_dict,limit=10)
    end = time.time()
    print("Greedy algorithm takes ", round(end - start, 4), "seconds to run", "\n\n")
    # greedy_trip = greedy_cow_transport(cow_dict,limit=10)
    # print("Length of trips is ",len(greedy_trip), "\n\n")


    print("Bruteforce trips are: \n")
    start = time.time()
    brute_force_cow_transport(cow_dict, limit=10)
    end = time.time()
    print("Bruteforce algorithm takes ", round(end - start, 4), "seconds to run", "\n\n")
    # brute_trip = brute_force_cow_transport(cow_dict, limit=10)
    # print("Length of trips is ",len(brute_trip), "\n\n")

# compare_cow_transport_algorithms()

cows = load_cows("ps1_cow_data_n.txt")
limit = 10
# print(cows)

print(brute_force_cow_transport(cows, limit))

# compare_cow_transport_algorithms()