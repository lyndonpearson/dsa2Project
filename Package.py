# This file contains the Package class definition. Package objects are created
# and fields assigned in the loadPackageData function in manageData.py


class Package:

    # Constructor with fields assigned from package data file.
    # The status field is an additional field used for tracking each package.
    # O(1) operation
    def __init__(self, ID, address, city, state, zip, deadline, mass, notes, status):
        self.ID = ID
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.mass = mass
        self.notes = notes
        self.status = "Package ID " + str(self.ID) + status

    # Package method that returns address field
    # O(1) operation
    def getAddress(self):
        return self.address

    # Package method that returns deadline field
    # O(1) operation
    def getDeadline(self):
        return self.deadline

    # Package method that sets address field
    # O(1) operation
    def setAddress(self, address):
        self.address = address

    # Package method that returns status field
    # O(1) operation
    def getStatus(self):
        return self.status

    # Package method that sets status field
    # O(1) operation
    def setStatus(self, statusUpdate):
        self.status = statusUpdate

    # Package method that returns ID field
    # O(1) operation
    def getID(self):
        return self.ID
