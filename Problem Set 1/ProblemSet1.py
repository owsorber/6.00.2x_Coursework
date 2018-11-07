"""
6.00.2x Problem Set 1: Space Cows 

Problem 1: 20/20 points
Problem 2: todo
Problem 3: todo

@author: owsorber
"""

from ps1_partition import get_partitions
import time

# This given function takes in a data file and creates a dictionary of cow names paired with their weights
def load_cows(filename):
    """
    Task:
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1: Greedy Cow Transport
def greedy_cow_transport(cows,limit):
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
    
    trips = [] # list of trips to be later returned
    
    # Sort cows into new list by their weight (heaviest to lightest)
    cowsSorted = []
    while len(cowsSorted) < len(cows):
        currHighestWeight = 0
        for cow in cows:
            if cows[cow] > currHighestWeight and cow not in cowsSorted:
                currHighestWeight = cows[cow]
                currHighestCow = cow
        
        cowsSorted.append(currHighestCow)
    
    
    # Generate trips with a greedy algorithm until no cows are left
    while len(cowsSorted) > 0:
        currTrip = [] # list of cows in current trip
        currWeight = 0 # weight of current trip we're producing
        currCow = 0 # index of cow currently being analyzed for potential allocation into currTrip
        
        while currCow < len(cowsSorted):
            if currWeight + cows[cowsSorted[currCow]] <= limit:
                currWeight += cows[cowsSorted[currCow]]
                currTrip.append(cowsSorted.pop(currCow))
            else:
                currCow += 1 # add 1 to currCow index to look at next cow in next iteration of loop
        
        trips.append(currTrip) # add current trip to the list of trips
        
    return trips


# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
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
    # TODO: Your code here
    pass

        
# Problem 3
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
    # TODO: Your code here
    pass




"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("Cow-Data.txt")
limit = 10
print(cows)

print(greedy_cow_transport(cows, limit))
print(brute_force_cow_transport(cows, limit))


