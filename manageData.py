import csv
from Package import Package


# This file contains the PackageHashTable definitions in
# addition to functions that load Package, Address,
# and Distance data.
class PackageHashTable:
    # Constructor with optional initial capacity parameter
    # which is set to 40 by default. 40 empty lists
    # are appended to the object.

    # The population of the hash table is an O(n) operation
    # as it iterates through the number of packages to create
    # a list at each location
    def __init__(self, initial_capacity=40):
        # initialize the hash table with empty bucket list entries.
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # For an input key, this method identifies the "bucket"
    # containing the key-value pair and, loops through
    # the pairs to find the one matching the input key.
    # once found, the associated value (a Package object)
    # has its status method called and printed to console

    # The return of the index list given a key is an O(1)
    # operation since it is independent of data size.
    # The search through the index list is an O(n) operation
    # where n is the number of key-value pairs at the given
    # index list
    def printPackageStatuses(self, key):
        # get the bucket list where this key would be.
        index = hash(key) % len(self.table)
        index_list = self.table[index]

        # search for the key in the bucket list
        for key_value in index_list:
            # print (key_value)
            if key_value[0] == key:
                print(key_value[1].getStatus())  # value

    # Inserts a new item into the hash table.
    # For the given input key (Package ID) and item (Package object),
    # the hash method identifies the "bucket" of storage in the
    # PackageHashTable. If the object is already present, the method
    # returns True. If the object is not present, the key-value pair
    # (package ID - Package object) is appended to the "bucket"

    # The insertPackage method is an O(1) operation
    # since a single key is hashed and a single item
    # is stored
    def insertPackage(self, key, item):
        # get the bucket list where this item will go.
        index = hash(key) % len(self.table)
        index_list = self.table[index]

        # update key if it is already in the bucket
        for key_value in index_list:
            # print (key_value)
            if key_value[0] == key:
                key_value[1] = item
                return True

        # if not, insert the item to the end of the bucket list.
        key_value_insert = [key, item]
        index_list.append(key_value_insert)
        return True

    # Searches for an item with matching key in the hash table.
    # Returns the item if found, or None if not found.
    # This method, given the input key, identifies the corresponding
    # "bucket" via hash function. It then searches through key-value
    # pairs and if there is a matching key, returns its associated value (Package object)

    # The searchHashTable method is an O(1) operation
    # since a single key is hashed. The search
    # operation is O(n) in the case of multiple items
    # stored in that location
    def searchHashTable(self, key):
        # get the bucket list where this key would be.
        index = hash(key) % len(self.table)
        index_list = self.table[index]

        # search for the key in the bucket list
        for key_value in index_list:
            # print (key_value)
            if key_value[0] == key:
                return key_value[1]  # value
        return None

    # Removes an item with matching key from the hash table.
    # This method, given the input key, identifies the corresponding
    # "bucket" via the hash function. It then searches for a matching
    # key and, if found, removes that key-value pair from the hash table

    # The removePackage method is an O(1) operation
    # for hashing the single key. The search
    # operation is O(n) in the case of multiple items
    # stored in that location
    def removePackage(self, key):
        # get the bucket list where this item will be removed from.
        index = hash(key) % len(self.table)
        index_list = self.table[index]

        # remove the item from the bucket list if it is present.
        for key_value in index_list:
            # print (key_value)
            if key_value[0] == key:
                index_list.remove([key_value[0], key_value[1]])


# This function, given a file name and hash table,
# opens the package data file, skips the header, and
# uses the file data to create Package objects (each object
# created from one file row). These objects are then stored
# in the hash table via its insertPackage method


def loadPackageData(fileName, hashTable):
    with open(fileName) as packageFile:
        packageData = csv.reader(packageFile, delimiter=',')
        for line in range(8):
            next(packageData)  # skip header
        # Looping through the package data file is an O(n)
        # operation with n referring to the number of data rows
        # in the file
        for package in packageData:
            packageID = int(package[0])
            packageAddress = package[1]
            packageCity = package[2]
            packageState = package[3]
            packageZip = int(package[4])
            packageDelivery = package[5]
            packageMass = int(package[6])
            packageNotes = package[7]

            # The creation of a Package object is an O(1) operation
            newPackage = Package(packageID, packageAddress, packageCity, packageState, packageZip,
                                 packageDelivery, packageMass, packageNotes, " at HUB")
            # The inseration of a Package object into the hash table is an O(1) operation
            hashTable.insertPackage(packageID, newPackage)


# This function, given an input distance list,
# opens the distance data file, skips the header, and
# uses the file data to create a 2-D list containing
# distances at each element. The elements are converted
# to floats before storage into the input distance list
def loadDistanceData(distanceDataInput):
    with open('WGUPS Distance Table.csv') as locationFile:
        locationData = csv.reader(locationFile, delimiter=',')
        for line in range(5):
            next(locationData)  # skip header
        # Looping through the distance data file is an O(n)
        # operation with n referring to the number of data rows
        # in the file
        for row in locationData:
            readString = row[2:]
            intConversion = list(map(float, readString))
            distanceDataInput.append(intConversion)


# This function, given an input address list,
# opens the address data file, skips the header, and
# extract the address from reach row. The addresses
# are stored as elements in the input address list.
def loadAddressData(addressDataInput):
    with open('WGUPS Distance Table.csv') as locationFile:
        locationData = csv.reader(locationFile, delimiter=',')
        for line in range(5):
            next(locationData)  # skip header
        # Looping through the address data file is an O(n)
        # operation with n referring to the number of data rows
        # in the file
        for row in locationData:
            addressDataInput.append(row[1][1:-8])


# Function that given a time input, parses it
# into hours, minutes, and seconds in the format
# HH:MM:SS. This format is returned.
def timeFloatToString(inputString):
    hours = int(inputString)
    minutes = (inputString * 60) % 60
    seconds = (inputString * 3600) % 60
    timeStamp = "%d:%02d:%02d" % (hours, minutes, seconds)
    return timeStamp
