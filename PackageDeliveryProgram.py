from RouteAndDeliver import RouteAndDeliver, returnToHub
from Truck import Truck, timeFloatToString
from manageData import loadPackageData, loadDistanceData, loadAddressData


def packageDeliveryProgram(hashTableInput, printTime=9999):

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

    PackageIdList1 = [2, 4, 5, 7, 14, 15, 16, 19, 20, 21, 22, 24, 30, 33, 34, 37]
    PackageIdList2 = [3, 8, 9, 10, 11, 12, 18, 23, 27, 28, 31, 32, 35, 36, 38, 39]
    PackageIdList3 = [1, 6, 13, 17, 25, 26, 29, 40]
    # LOAD PACKAGES INTO TRUCKS HERE
    for i in range(41):
        if i in PackageIdList1:
            Truck1.loadPackage(testList[i])
        elif i in PackageIdList2:
            Truck2.loadPackage(testList[i])
        elif i in PackageIdList3:
            Truck3.loadPackage(testList[i])

    while len(Truck1.packageList) > 0:
        if RouteAndDeliver(Truck1, addressData, distanceData, printTime, hashTableInput):
            return
        # Start truck 3 after 9:05AM
        if Truck1.getTruckTime() > 9.084 and len(Truck3.packageList) > 0:
            if RouteAndDeliver(Truck3, addressData, distanceData, printTime, hashTableInput):
                return
    Truck1.setStatus(1)
    returnToHub(Truck1, addressData, distanceData)

    while len(Truck3.packageList) > 0:
        if RouteAndDeliver(Truck3, addressData, distanceData, printTime, hashTableInput):
            return
        Truck2.setTruckTime(Truck1.getTruckTime())
        if RouteAndDeliver(Truck2, addressData, distanceData, printTime, hashTableInput):
            return

    Truck3.setStatus(1)
    returnToHub(Truck3, addressData, distanceData)

    while len(Truck2.packageList) > 0:
        if RouteAndDeliver(Truck2, addressData, distanceData, printTime, hashTableInput):
            return
    Truck2.setStatus(1)
    returnToHub(Truck2, addressData, distanceData)

    if Truck1.getStatus() and Truck2.getStatus() and Truck3.getStatus():
        if printTime < 9999.0:
            for package in range(41):
                hashTableInput.printPackageStatuses(package)
            print("##############################################################")
            print("\nAll packages delivered at: " + timeFloatToString(Truck2.getTruckTime()))
            print("Total miles traveled: " + str(Truck1.getDistanceTraveled() + Truck2.getDistanceTraveled() + Truck3.getDistanceTraveled()) + "\n")
            print("##############################################################")
        elif printTime < 99999:
            print("##############################################################")
            print("\nAll packages delivered at: " + timeFloatToString(Truck2.getTruckTime()))
            print("Total miles traveled: " + str(Truck1.getDistanceTraveled() + Truck2.getDistanceTraveled() + Truck3.getDistanceTraveled()) + "\n")
            print("##############################################################")
