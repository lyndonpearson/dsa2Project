from manageData import timeFloatToString


# This file contains the Truck class definition. Truck objects are created
# and fields assigned in the PackageDeliveryProgram.py
class Truck:
    # Truck constructor
    # O(1) operation
    def __init__(self, ID):
        self.ID = ID
        self.CAPACITY = 16
        self.packageList = []
        self.distanceTraveled = 0.0
        self.location = "4001 South 700 East"
        self.status = 0
        self.truckTime = 8.00

    # Truck method that adds an input package to its list
    # O(1) operation
    def loadPackage(self, package):
        if len(self.packageList) < self.CAPACITY:
            self.packageList.append(package)
            package.setStatus("Package ID " + str(package.getID()) + " en route")

    # Truck method that updates status field
    # O(1) operation
    def setStatus(self, updateStatus):
        self.status = updateStatus

    # Truck method that returns status field
    # O(1) operation
    def getStatus(self):
        return self.status

    # Truck method that returns package object by ID
    # O(n) operation as it looks through truck's package list
    def getPackageByID(self, packageID):
        for package in self.packageList:
            if package.ID == packageID:
                return package
        return None

    # Truck method that returns package object by position index
    # O(1) operation
    def getPackageByIndex(self, index):
        if index < len(self.packageList):
            return self.packageList[index]
        return None

    # Truck method that sets package object's location field
    # O(1) operation
    def setLocation(self, updateLocation):
        self.location = updateLocation

    # Truck method that returns package object's location field
    # O(1) operation
    def getLocation(self):
        return self.location

    # Truck method that returns package object's distanceTraveled field
    # O(1) operation
    def getDistanceTraveled(self):
        return self.distanceTraveled

    # Truck class method that given a package ID, sets
    # the truck location. It then updates the package delivery
    # with a timestamp and removes the package from its list

    # O(n) operation due to "getPackageByID" call since the method
    # loops through all packages in a truck's list
    def deliverPackage(self, ID):
        self.setLocation(self.getPackageByID(ID).getAddress())
        self.getPackageByID(ID).setStatus(
            ("Package ID " + str(ID) + " delivered by truck #" + str(self.getID()) + " at "
             + timeFloatToString(self.truckTime)) + " delivery deadline of " + self.getPackageByID(ID).getDeadline())
        self.packageList.remove(self.getPackageByID(ID))

    # Truck method that returns truck's time
    # O(1) operation
    def getTruckTime(self):
        return self.truckTime

    # Truck method that sets truck's time
    # O(1) operation
    def setTruckTime(self, inputTime):
        self.truckTime = inputTime

    # Truck class method that given an input delivery leg distance,
    # updates the total distance traveled as well as the time.
    # The updated time is returned
    # O(1) operation
    def updateTime(self, legDistance):
        self.distanceTraveled += float(legDistance)
        SPEED = 18
        self.truckTime += (legDistance / SPEED)
        return self.truckTime

    # Truck method that returns truck's ID
    # O(1) operation
    def getID(self):
        return self.ID
