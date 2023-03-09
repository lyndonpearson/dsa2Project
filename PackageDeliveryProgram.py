from RouteAndDeliver import RouteAndDeliver, returnToHub
from Truck import Truck, timeFloatToString
from manageData import loadPackageData, loadDistanceData, loadAddressData


# This program is called by main.py and, depending on which option
# either runs to completion and prints out completion time & total miles
# or stops at the specified time and prints status for all packages.

def packageDeliveryProgram(hashTableInput, printTime=9999):
    printTime = float(printTime)
    loadPackageData('WGUPS Package File.csv', hashTableInput)

    # Create Distance & Address Lists
    distanceData = []
    addressData = []

    # Load the lists with data
    loadDistanceData(distanceData)
    loadAddressData(addressData)

    # 3 Trucks created for the delivery system
    Truck1 = Truck(1)
    Truck2 = Truck(2)
    Truck3 = Truck(3)

    # A list storing all packages
    completePackageList = []
    # Populating the package list with package objects
    # is an O(n) operation since it loops through the number
    # of packages. Searching the hash table is an O(1) operation.
    for i in range(41):
        completePackageList.append(hashTableInput.searchHashTable(i))

    # Manual package assignment, by ID, to trucks 1/2/3. All package constraints
    # are met by this assignment
    PackageIdList1 = [2, 4, 5, 7, 14, 15, 16, 19, 20, 21, 22, 24, 30, 33, 34, 37]
    PackageIdList2 = [3, 8, 9, 10, 11, 12, 18, 23, 27, 28, 31, 32, 35, 36, 38, 39]
    PackageIdList3 = [1, 6, 13, 17, 25, 26, 29, 40]

    # Loop through all packages and load them into the assigned truck.
    # O(n) operation as each element in the package list is accessed
    # in numerical order
    for i in range(41):
        if i in PackageIdList1:
            Truck1.loadPackage(completePackageList[i])
        elif i in PackageIdList2:
            Truck2.loadPackage(completePackageList[i])
        elif i in PackageIdList3:
            Truck3.loadPackage(completePackageList[i])

    # Truck 1 departs immediately at 0800. While there are remaining packages in the truck,
    # they are delivered one address at a time.

    # This is an O(n) operation, since for each package in the truck
    # this block of called is executed.
    while len(Truck1.packageList) > 0:
        if RouteAndDeliver(Truck1, addressData, distanceData, printTime, hashTableInput):
            return
        # Truck 3 departs after 0905 and delivers packages one address at a time
        # Also O(n) operation, since for each package in the truck this code
        # is executed
        if Truck1.getTruckTime() > 9.084 and len(Truck3.packageList) > 0:
            if RouteAndDeliver(Truck3, addressData, distanceData, printTime, hashTableInput):
                return
    # Once all packages from truck 1 are delivered, the truck's
    # status is set to complete, and it returns to the hub
    # O(1) operation since the return distance to hub is calculated
    # and added to the truck's total
    Truck1.setStatus(1)
    returnToHub(Truck1, addressData, distanceData)

    # Truck 3 continues delivering its remaining packages, one address at a time

    # This is an O(n) operation, since for each package in the truck
    # this block of called is executed.
    while len(Truck3.packageList) > 0:
        if RouteAndDeliver(Truck3, addressData, distanceData, printTime, hashTableInput):
            return
        # Truck 2 sets its local time of departure to truck 1's return to hub.
        # It then begins delivering packages one address at a time.
        # Also O(n) operation, since for each package in the truck this code
        # is executed
        Truck2.setTruckTime(Truck1.getTruckTime())
        if RouteAndDeliver(Truck2, addressData, distanceData, printTime, hashTableInput):
            return

    # Once all packages from truck 3 are delivered, the truck's
    # status is set to complete, and it returns to the hub
    # O(1) operation since the return distance to hub is calculated
    # and added to the truck's total
    Truck3.setStatus(1)
    returnToHub(Truck3, addressData, distanceData)

    # Truck 2 finishes its delivery of remaining packages

    # This is an O(n) operation, since for each package in the truck
    # this block of called is executed.
    while len(Truck2.packageList) > 0:
        if RouteAndDeliver(Truck2, addressData, distanceData, printTime, hashTableInput):
            return

    # Once all packages from truck 2 are delivered, the truck's
    # status is set to complete, and it returns to the hub
    # O(1) operation since the return distance to hub is calculated
    # and added to the truck's total
    Truck2.setStatus(1)
    returnToHub(Truck2, addressData, distanceData)

    # If all trucks have completed their deliveries, and a status report time
    # has not been specified, the total time is return to console. The
    # total mileage for all trucks is calculated and return to console.
    # If a time has been specified, then the status of all packages
    # is printed to console at that time.

    # The status report is an O(n) operation since it accesses the Package
    # objects in numerical order and prints their status to console.
    if Truck1.getStatus() and Truck2.getStatus() and Truck3.getStatus():
        for package in range(41):
            hashTableInput.printPackageStatuses(package)
        print("##############################################################")
        print("\nAll packages delivered at: " + timeFloatToString(Truck2.getTruckTime()))
        print("Total miles traveled: " + str(
            Truck1.getDistanceTraveled() + Truck2.getDistanceTraveled() + Truck3.getDistanceTraveled()) + "\n")
        print("##############################################################")

