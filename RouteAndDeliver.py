from GreedyAlgorithm import GreedyAlgorithm


def RouteAndDeliver(truckInput, addressInput, distanceInput, currentTime, printTime, hashTableInput, totalDistance):
    if currentTime >= printTime:
        for package in range(41):
            hashTableInput.printPackageStatuses(package)
        totalDistance = None
        updateTime = None
        return updateTime, totalDistance
    currentMinimum, currentID = GreedyAlgorithm(truckInput, addressInput, distanceInput)
    truckInput.deliverPackage(currentMinimum, currentID, currentTime, totalDistance)
    totalDistance += currentMinimum
    updateTime = truckInput.updateTime(currentMinimum)
    return updateTime, totalDistance


def returnToHub(truckInput, addressInput, distanceInput):
    currentLocationIndex = addressInput.index(truckInput.getLocation());
    distanceToHub = distanceInput[0][currentLocationIndex]
    updateTime = truckInput.updateTime(distanceToHub)
    return updateTime
