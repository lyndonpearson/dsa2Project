def timeFloatToString(inputString):
    hours = int(inputString)
    minutes = (inputString * 60) % 60
    seconds = (inputString * 3600) % 60
    timeStamp = "%d:%02d:%02d" % (hours, minutes, seconds)
    return timeStamp


class Truck:
    def __init__(self, ID):
        self.ID = ID
        self.CAPACITY = 16
        self.packageList = []
        self.time = 8.00
        self.distanceTraveled = 0.0
        self.location = "4001 South 700 East"
        self.status = 0

    def loadPackage(self, package):
        if len(self.packageList) < self.CAPACITY:
            self.packageList.append(package)
            package.setStatus("Package ID " + str(package.getID()) + " en route")

    def setStatus(self, updateStatus):
        self.status = updateStatus

    def getStatus(self):
        return self.status

    def getPackageByID(self, packageID):
        for package in self.packageList:
            if package.ID == packageID:
                return package
        return None

    def getPackageByIndex(self, index):
        if index < len(self.packageList):
            return self.packageList[index]
        return None

    def setLocation(self, updateLocation):
        self.location = updateLocation

    def getLocation(self):
        return self.location

    def printPackages(self):
        for package in self.packageList:
            print(package)

    def updateDistance(self, distance, totalDistance):
        totalDistance += float(distance)

    def deliverPackage(self, distance, ID, currentTime, totalDistance):
        # self.distanceTraveled += float(distance)
        self.updateDistance(distance, totalDistance)
        self.setLocation(self.getPackageByID(ID).getAddress())
        self.getPackageByID(ID).setStatus(
            ("Package ID " + str(ID) + " delivered by truck #" + str(self.getID()) + " at " + timeFloatToString(currentTime)))
        self.packageList.remove(self.getPackageByID(ID))

    def updateTime(self, legDistance):
        SPEED = 18
        legTime = legDistance / SPEED
        return legTime

    def getID(self):
        return self.ID
