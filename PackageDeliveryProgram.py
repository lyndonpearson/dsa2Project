from RouteAndDeliver import RouteAndDeliver, returnToHub
from Truck import Truck, timeFloatToString
from manageData import loadPackageData, loadDistanceData, loadAddressData


def packageDeliveryProgram(hashTableInput, printTime=9999.0):
    currentTime = 8.00
    cumulativeDistance = 0.00
    printTime = float(printTime)
    loadPackageData('WGUPS Package File.csv', hashTableInput)

    # Create Distance & Address Lists
    distanceData = []
    addressData = []

    # Load the lists with data
    loadDistanceData(distanceData)
    loadAddressData(addressData)

    # TRUCK 1 SECTION HERE #######################################
    Truck1 = Truck(1)
    Truck2 = Truck(2)
    Truck3 = Truck(3)

    testList = []
    for i in range(41):
        testList.append(hashTableInput.search(i))

    PackageIdList1 = [2, 4, 5, 7, 14, 15, 16, 19, 20, 21, 22, 24, 30, 33, 34, 37] #11
    PackageIdList2 = [3, 8, 9, 10, 11, 12, 18, 23, 27, 28, 31, 32, 35, 36, 38, 39] #15
    PackageIdList3 = [1, 6, 13, 17, 25, 26, 29, 40] #14
    # LOAD PACKAGES INTO TRUCKS HERE
    for i in range(41):
        if i in PackageIdList1:
            Truck1.loadPackage(testList[i])
        elif i in PackageIdList2:
            Truck2.loadPackage(testList[i])
        elif i in PackageIdList3:
            Truck3.loadPackage(testList[i])

    while len(Truck1.packageList) > 0:
        timeUpdate3 = 999
        timeUpdate1, cumulativeDistance = RouteAndDeliver(Truck1, addressData, distanceData, currentTime,
                                                          printTime, hashTableInput, cumulativeDistance)
        # Start truck 3 after 9:05AM
        if currentTime > 9.084 and len(Truck3.packageList) > 0:
            timeUpdate3, cumulativeDistance = RouteAndDeliver(Truck3, addressData, distanceData, currentTime,
                                                              printTime, hashTableInput, cumulativeDistance)
        if timeUpdate1 is None:
            return
        elif timeUpdate1 < timeUpdate3:
            currentTime += timeUpdate1
        else:
            currentTime += timeUpdate3
    Truck1.setStatus(1)
    timeUpdate1 = returnToHub(Truck1, addressData, distanceData)
    currentTime += timeUpdate1
    while len(Truck3.packageList) > 0:
        timeUpdate3, cumulativeDistance = RouteAndDeliver(Truck3, addressData, distanceData, currentTime,
                                                          printTime, hashTableInput, cumulativeDistance)
        timeUpdate2, cumulativeDistance = RouteAndDeliver(Truck2, addressData, distanceData, currentTime,
                                                          printTime, hashTableInput, cumulativeDistance)
        if timeUpdate3 is None:
            return
        elif timeUpdate3 < timeUpdate2:
            currentTime += timeUpdate3
        else:
            currentTime += timeUpdate2

    Truck3.setStatus(1)
    timeUpdate3 = returnToHub(Truck3, addressData, distanceData)
    currentTime += timeUpdate3
    while len(Truck2.packageList) > 0:
        timeUpdate2, cumulativeDistance = RouteAndDeliver(Truck2, addressData, distanceData, currentTime,
                                                          printTime, hashTableInput, cumulativeDistance)
        if timeUpdate2 is None:
            return
        else:
            currentTime += timeUpdate2
    Truck2.setStatus(1)
    timeUpdate2 = returnToHub(Truck2, addressData, distanceData)
    currentTime += timeUpdate2
    if Truck1.getStatus() and Truck2.getStatus() and Truck3.getStatus():
        if printTime < 9999.0:
            for package in range(41):
                hashTableInput.printPackageStatuses(package)
            print("##############################################################")
            print("\nAll packages delivered at: " + timeFloatToString(currentTime))
            print("Total miles traveled: " + str(cumulativeDistance) + "\n")
            print("##############################################################")
        elif printTime < 99999:
            print("##############################################################")
            print("\nAll packages delivered at: " + timeFloatToString(currentTime))
            print("Total miles traveled: " + str(cumulativeDistance) + "\n")
            print("##############################################################")
