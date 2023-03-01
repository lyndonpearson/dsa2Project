
def GreedyAlgorithm(Truck, addressList, distanceList):
    currentMinimum = 9999
    currentID = 0
    startIndex = addressList.index(Truck.location)
    for i in range(len(Truck.packageList)):
        if Truck.getPackageByIndex(i).getID() == 25 or Truck.getPackageByIndex(i).getID() == 26:
            Truck.getPackageByIndex(i).setAddress("5383 S 900 East #104")
        deliverIndex = addressList.index(Truck.getPackageByIndex(i).getAddress())
        if distanceList[startIndex][deliverIndex] < currentMinimum:
            currentMinimum = distanceList[startIndex][deliverIndex]
            currentID = Truck.getPackageByIndex(i).getID()
    return currentMinimum, currentID
