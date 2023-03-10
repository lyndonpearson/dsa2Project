from GreedyAlgorithm import GreedyAlgorithm


# This function, given the truck object, address & distance data list, input time,
# and package hash table, calls the greedy algorithm to identify the closet package ID
# and its distance. If no input time is given, the package is delivered and its status updated
# and the function returns a value of 0.
# If an input time is given and the next delivery would exceed it, the package statuses are all
# printed to console and the function returns 1

# Total operation can be considered O(n) since the greedy algorithm is O(n) and the
# package status print out is also O(n). Adding the two together produces O(n+n) = O(2n) = O(n)
# since the coefficient can be discarded.
def RouteAndDeliver(truckInput, addressInput, distanceInput, printTime, hashTableInput):
    # The greedy algorith is an O(n) operation since it iterates through the packages
    # to find and return the closest one.
    currentMinimum, currentID = GreedyAlgorithm(truckInput, addressInput, distanceInput)

    if truckInput.updateTime(currentMinimum) >= printTime:
        # The package status printout is an O(n) operation since it iterates through
        # all package objects to print their status
        for package in range(41):
            hashTableInput.printPackageStatuses(package)
        return 1
    truckInput.deliverPackage(currentID)
    return 0


# This function, given a truck object, address & distance data list,
# calculates the distance and time required to return to the hub
# The truck's time and distance traveled are both updated.

# The returnToHub function is an O(1) operation since it merely
# returns a distance value given the indices.
def returnToHub(truckInput, addressInput, distanceInput):
    currentLocationIndex = addressInput.index(truckInput.getLocation());
    distanceToHub = distanceInput[0][currentLocationIndex]
    truckInput.updateTime(distanceToHub)
