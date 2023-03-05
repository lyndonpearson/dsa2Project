from GreedyAlgorithm import GreedyAlgorithm


# This function, given the truck object, address & distance data list, input time,
# and package hash table, calls the greedy algorithm to identify the closet package ID
# and its distance. If no input time is given, the package is delivered and its status updated
# and the function returns a value of 0.
# If an input time is given and the next delivery would exceed it, the package statuses are all
# printed to console and the function returns 1
def RouteAndDeliver(truckInput, addressInput, distanceInput, printTime, hashTableInput):
    currentMinimum, currentID = GreedyAlgorithm(truckInput, addressInput, distanceInput)

    if truckInput.updateTime(currentMinimum) >= printTime:
        for package in range(41):
            hashTableInput.printPackageStatuses(package)
        return 1
    truckInput.deliverPackage(currentID)
    return 0


# This function, given a truck object, address & distance data list,
# calculates the distance and time required to return to the hub
# The truck's time and distance traveled are both updated.
def returnToHub(truckInput, addressInput, distanceInput):
    currentLocationIndex = addressInput.index(truckInput.getLocation());
    distanceToHub = distanceInput[0][currentLocationIndex]
    truckInput.updateTime(distanceToHub)
