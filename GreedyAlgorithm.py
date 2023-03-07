# This method is passed in a Truck object, the address & distance lists. For each function call,
# the current location is identified in addition to the closest package. The closest package has its
# ID return in addition to the distance for its delivery.
def GreedyAlgorithm(Truck, addressList, distanceList):
    minimumDistance = 9999
    currentID = 0
    startIndex = addressList.index(Truck.location)
    # For this block of code in the greedy algorithm, big-O complexity is O(n)
    # for a single call of the greedy algorithm function as it loops through
    # the list of packages to identify which one has the smallest distance.
    for i in range(len(Truck.packageList)):
        if Truck.getPackageByIndex(i).getID() == 25 or Truck.getPackageByIndex(i).getID() == 26:
            Truck.getPackageByIndex(i).setAddress("5383 S 900 East #104")
        deliverIndex = addressList.index(Truck.getPackageByIndex(i).getAddress())
        if distanceList[startIndex][deliverIndex] < minimumDistance:
            minimumDistance = distanceList[startIndex][deliverIndex]
            currentID = Truck.getPackageByIndex(i).getID()
    return minimumDistance, currentID
