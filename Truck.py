from readCSV import ChainingHashTable, loadPackageData, loadDistanceData, loadAddressData, Package


class Truck:
    def __init__(self, ID):
        self.ID = ID
        self.CAPACITY = 16
        self.packageList = []
        self.time = 8.00
        self.distanceTraveled = 0.0
        self.location = "4001 South 700 East"

    def loadPackage(self, package):
        if len(self.packageList) < self.CAPACITY:
            self.packageList.append(package)
            package.status = "In Transit"

    def getPackage(self, packageID):
        for package in self.packageList:
            if package.ID == packageID:
                return package
        return None

    def printPackages(self):
        for package in self.packageList:
            print(package)

    def deliverPackage(self, distance):
        self.distanceTraveled += float(distance)
        deliveredPackage = self.packageList.pop(0)
        deliveredPackage.status = "Delivered"

    def updateTime(self):
        SPEED = 18
        spentTime = self.distanceTraveled / SPEED
        self.time += spentTime

