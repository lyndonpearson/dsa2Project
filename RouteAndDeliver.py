from GreedyAlgorithm import GreedyAlgorithm


def RouteAndDeliver(truckInput, addressInput, distanceInput, currentTime, printTime, hashTableInput):
    if currentTime is None:
        return
    elif currentTime >= printTime:
        for package in range(41):
            hashTableInput.printPackageStatuses(package)
        return
    currentMinimum, currentID = GreedyAlgorithm(truckInput, addressInput, distanceInput)
    truckInput.deliverPackage(currentMinimum, currentID, currentTime)
    currentTime += truckInput.updateTime(currentMinimum)
    return currentTime


def returnToHub(truckInput, addressInput, distanceInput, currentTime):
    currentLocationIndex = addressInput.index(truckInput.getLocation());
    distanceToHub = distanceInput[0][currentLocationIndex]
    print("Time before return is: " + str(currentTime))
    truckInput.updateDistance(distanceToHub)
    currentTime += truckInput.updateTime(distanceToHub)
    print("Distance to hub is: " + str(distanceToHub))
    print("Current location is: " + truckInput.getLocation())
    print("Time after return is: " + str(currentTime))
    return currentTime
