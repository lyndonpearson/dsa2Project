# This file contains the Package class definition. Package objects are created
# and fields assigned in the loadPackageData function in manageData.py


class Package:

    # Constructor with fields assigned from package data file.
    # The status field is an additional field used for tracking each package.
    def __init__(self, ID, address, city, state, zip, delivery, mass, notes, status):
        self.ID = ID
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.delivery = delivery
        self.mass = mass
        self.notes = notes
        self.status = "Package ID " + str(self.ID) + status

    def getAddress(self):
        return self.address

    def setAddress(self, address):
        self.address = address

    def getStatus(self):
        return self.status

    def setStatus(self, statusUpdate):
        self.status = statusUpdate

    def getID(self):
        return self.ID
