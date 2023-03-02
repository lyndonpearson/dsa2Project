from RouteAndDeliver import RouteAndDeliver, returnToHub
from Truck import Truck, timeFloatToString
from manageData import loadPackageData, loadDistanceData, loadAddressData


def packageDeliveryProgram(hashTableInput, printTime=9999.0):
    currentTime = 8.00
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

    # CREATE PACKAGES HERE ########################################
    PackageIdList1 = [1, 2, 10, 12, 13, 14, 15, 16, 19, 20, 21]
    PackageIdList2 = [3, 17, 18, 22, 23, 24, 33, 27, 29, 30, 31, 34, 36, 37, 38, 40 ]
    PackageIdList3 = [4, 5, 7, 8, 11, 6, 9, 25, 26, 28, 32, 35, 39 ]
    # LOAD PACKAGES INTO TRUCKS HERE
    for i in range(41):
        if i in PackageIdList1:
            Truck1.loadPackage(testList[i])
        elif i in PackageIdList2:
            Truck2.loadPackage(testList[i])
        elif i in PackageIdList3:
            Truck3.loadPackage(testList[i])

    while len(Truck1.packageList) > 0:
        currentTime = RouteAndDeliver(Truck1, addressData, distanceData, currentTime, printTime, hashTableInput)
        # Start truck 3 after 9:05AM
        if currentTime > 9.084:
            currentTime = RouteAndDeliver(Truck3, addressData, distanceData, currentTime, printTime, hashTableInput)
    Truck1.setStatus(1)
    currentTime = returnToHub(Truck1, addressData, distanceData, currentTime)
    while len(Truck3.packageList) > 0 and currentTime is not None:
        currentTime = RouteAndDeliver(Truck3, addressData, distanceData, currentTime, printTime, hashTableInput)
        currentTime = RouteAndDeliver(Truck2, addressData, distanceData, currentTime, printTime, hashTableInput)
    Truck3.setStatus(1)
    currentTime = returnToHub(Truck3, addressData, distanceData, currentTime)
    while len(Truck2.packageList) > 0 and currentTime is not None:
        currentTime = RouteAndDeliver(Truck2, addressData, distanceData, currentTime, printTime, hashTableInput)
    Truck2.setStatus(1)
    currentTime = returnToHub(Truck2, addressData, distanceData, currentTime)
    if Truck1.getStatus() and Truck2.getStatus() and Truck3.getStatus() and currentTime is not None:
        if printTime < 9999.0:
            for package in range(41):
                hashTableInput.printPackageStatuses(package)
            print("##############################################################")
            print("\nAll packages delivered at: " + timeFloatToString(currentTime))
            print("Total miles traveled: " + str(Truck1.distanceTraveled + Truck2.distanceTraveled
                                                 + Truck3.distanceTraveled) + "\n")
            print("##############################################################")
        elif printTime < 99999:
            print("##############################################################")
            print("\nAll packages delivered at: " + timeFloatToString(currentTime))
            print("Total miles traveled: " + str(Truck1.distanceTraveled + Truck2.distanceTraveled
                                                 + Truck3.distanceTraveled) + "\n")
            print("##############################################################")
