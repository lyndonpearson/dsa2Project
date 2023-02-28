class Package:
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

    def __str__(self):  # overwite print(Movie) otherwise it will print object reference
        return "%s, %s, %s, %s, %s, %s, %s, %s" % (self.ID, self.address, self.city, self.state, self.zip,
                                                   self.delivery, self.mass, self.notes)