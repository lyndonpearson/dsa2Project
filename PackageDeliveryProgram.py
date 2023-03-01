from GreedyAlgorithm import GreedyAlgorithm
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

    # CREATE PACKAGES HERE ########################################
    package1 = hashTableInput.search(1)  # 10:30
    package2 = hashTableInput.search(2)
    package3 = hashTableInput.search(4)
    package4 = hashTableInput.search(5)
    package5 = hashTableInput.search(7)
    package6 = hashTableInput.search(8)
    package7 = hashTableInput.search(10)
    package8 = hashTableInput.search(11)
    package9 = hashTableInput.search(12)
    package10 = hashTableInput.search(13)  # 10:30
    package11 = hashTableInput.search(14)  # 10:30 must be with 15 & 19
    package12 = hashTableInput.search(15)  # 9:00
    package13 = hashTableInput.search(16)  # 10:30 #must be with 13 & 19
    package14 = hashTableInput.search(19)
    package15 = hashTableInput.search(20)  # 10:30 must be with 13 & 15
    package16 = hashTableInput.search(21)
    package17 = hashTableInput.search(3)
    package18 = hashTableInput.search(17)
    package19 = hashTableInput.search(18)
    package20 = hashTableInput.search(22)
    package21 = hashTableInput.search(23)
    package22 = hashTableInput.search(24)
    package23 = hashTableInput.search(33)
    package24 = hashTableInput.search(27)
    package25 = hashTableInput.search(29)
    package26 = hashTableInput.search(30)
    package27 = hashTableInput.search(31)
    package28 = hashTableInput.search(34)
    package29 = hashTableInput.search(36)
    package30 = hashTableInput.search(37)
    package31 = hashTableInput.search(38)
    package32 = hashTableInput.search(40)
    package33 = hashTableInput.search(6)  # arrive 9:05, deliver 10:30
    package34 = hashTableInput.search(9)  # wrong address corrected ~11
    package35 = hashTableInput.search(25)  # arrive 9:05, deliver 10:30
    package36 = hashTableInput.search(26)
    package37 = hashTableInput.search(28)  # arrive 9:05
    package38 = hashTableInput.search(32)  # arrive 9:05
    package39 = hashTableInput.search(35)
    package40 = hashTableInput.search(39)

    # LOAD PACKAGES IN TRUCKS HERE ########################################################
    Truck1.loadPackage(package1)
    Truck1.loadPackage(package2)
    Truck3.loadPackage(package3)
    Truck3.loadPackage(package4)
    Truck3.loadPackage(package5)
    Truck3.loadPackage(package6)
    Truck1.loadPackage(package7)
    Truck3.loadPackage(package8)
    Truck1.loadPackage(package9)
    Truck1.loadPackage(package10)
    Truck1.loadPackage(package11)
    Truck1.loadPackage(package12)
    Truck1.loadPackage(package13)
    Truck1.loadPackage(package14)
    Truck1.loadPackage(package15)
    Truck1.loadPackage(package16)
    Truck2.loadPackage(package17)
    Truck2.loadPackage(package18)
    Truck2.loadPackage(package19)
    Truck2.loadPackage(package20)
    Truck2.loadPackage(package21)
    Truck2.loadPackage(package22)
    Truck2.loadPackage(package23)
    Truck2.loadPackage(package24)
    Truck2.loadPackage(package25)
    Truck2.loadPackage(package26)
    Truck2.loadPackage(package27)
    Truck2.loadPackage(package28)
    Truck2.loadPackage(package29)
    Truck2.loadPackage(package30)
    Truck2.loadPackage(package31)
    Truck2.loadPackage(package32)
    Truck3.loadPackage(package33)
    Truck3.loadPackage(package34)
    Truck3.loadPackage(package35)
    Truck3.loadPackage(package36)
    Truck3.loadPackage(package37)
    Truck3.loadPackage(package38)
    Truck3.loadPackage(package39)
    Truck3.loadPackage(package40)

    while len(Truck1.packageList) > 0:
        currentMinimum, currentID = GreedyAlgorithm(Truck1, addressData, distanceData)
        if currentTime >= printTime:
            for package in range(41):
                hashTableInput.printPackageStatuses(package)
            return
        Truck1.deliverPackage(currentMinimum, currentID, currentTime)
        currentTime += Truck1.updateTime(currentMinimum)
        # Start truck 3 after 9:05AM
        if currentTime > 9.084:
            currentMinimumTruck3, currentIDTruck3 = GreedyAlgorithm(Truck3, addressData, distanceData)
            if currentTime >= printTime:
                for package in range(41):
                    hashTableInput.printPackageStatuses(package)
                return
            Truck3.deliverPackage(currentMinimumTruck3, currentIDTruck3, currentTime)
            currentTime += Truck3.updateTime(currentMinimumTruck3)
    Truck1.setStatus(1)
    while len(Truck3.packageList) > 0:
        currentMinimum3, currentID3 = GreedyAlgorithm(Truck3, addressData, distanceData)
        if currentTime >= printTime:
            for package in range(41):
                hashTableInput.printPackageStatuses(package)
            return
        Truck3.deliverPackage(currentMinimum3, currentID3, currentTime)
        currentTime += Truck3.updateTime(currentMinimum3)
        currentMinimum2, currentID2 = GreedyAlgorithm(Truck2, addressData, distanceData)
        if currentTime >= printTime:
            for package in range(41):
                hashTableInput.printPackageStatuses(package)
            return
        Truck2.deliverPackage(currentMinimum2, currentID2, currentTime)
        currentTime += Truck2.updateTime(currentMinimum2)
    Truck3.setStatus(1)
    while len(Truck2.packageList) > 0:
        if currentTime >= printTime:
            for package in range(41):
                hashTableInput.printPackageStatuses(package)
            return
        currentMinimum2, currentID2 = GreedyAlgorithm(Truck2, addressData, distanceData)
        Truck2.deliverPackage(currentMinimum2, currentID2, currentTime)
        currentTime += Truck2.updateTime(currentMinimum2)
    Truck2.setStatus(1)
    if Truck1.getStatus() and Truck2.getStatus() and Truck3.getStatus():
        print("\nAll packages delivered at: " + timeFloatToString(currentTime))
        print("Total miles traveled: " + str(Truck1.distanceTraveled + Truck2.distanceTraveled
                                             + Truck3.distanceTraveled) + "\n")
        if printTime < 9999.0:
            for package in range(41):
                hashTableInput.printPackageStatuses(package)
            return
