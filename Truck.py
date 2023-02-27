class Truck:
    def __init__(self, ID):
        self.ID = ID
        self.CAPACITY = 16
        self.packageList = []
        self.time = 8.00
        self.distanceTraveled = 0.0
        self.location = "4001 South 700 East"
        self.startingTime = 8.00

    def loadPackage(self, package):
        if len(self.packageList) < self.CAPACITY:
            self.packageList.append(package)
            package.status = "In Transit"

    def getPackageByID(self, packageID):
        for package in self.packageList:
            if package.ID == packageID:
                return package
        return None

    def getPackageByIndex(self, index):
        if index < len(self.packageList):
            return self.packageList[index]
        return None

    def printPackages(self):
        for package in self.packageList:
            print(package)

    def deliverPackage(self, distance, ID):
        self.distanceTraveled += float(distance)
        self.location = self.getPackageByID(ID).getAddress()
        self.getPackageByID(ID).status = "Delivered"
        print("Package ID: " + str(self.getPackageByID(ID).getID()) +
              " has been delivered at time " + str(self.time))
        self.packageList.remove(self.getPackageByID(ID))

    def setStartingTime(self, time):
        self.startingTime = time

    def updateTime(self):
        SPEED = 18
        spentTime = self.distanceTraveled / SPEED
        self.time = self.startingTime + spentTime


