from GreedyAlgorithm import GreedyAlgorithm


def RouteAndDeliver(truckInput, addressInput, distanceInput, printTime, hashTableInput):

    currentMinimum, currentID = GreedyAlgorithm(truckInput, addressInput, distanceInput)

    if truckInput.updateTime(currentMinimum) >= printTime:
        for package in range(41):
            hashTableInput.printPackageStatuses(package)
        return 1
    truckInput.deliverPackage(currentMinimum, currentID)
    return 0


def returnToHub(truckInput, addressInput, distanceInput):
    currentLocationIndex = addressInput.index(truckInput.getLocation());
    distanceToHub = distanceInput[0][currentLocationIndex]
    truckInput.updateTime(distanceToHub)
