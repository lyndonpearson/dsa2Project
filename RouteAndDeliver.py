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
