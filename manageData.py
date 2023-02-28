import csv
import math

from Package import Package


# HashTable class using chaining.
class PackageHashTable:
    # Constructor with optional initial capacity parameter.
    # Assigns all buckets with an empty list.
    def __init__(self, initial_capacity=39):
        # initialize the hash table with empty bucket list entries.
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    def printPackageStatuses(self, key):
        # get the bucket list where this key would be.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # search for the key in the bucket list
        for kv in bucket_list:
            # print (key_value)
            if kv[0] == key:
                print(kv[1].getStatus())  # value

    # Inserts a new item into the hash table.
    def insert(self, key, item):  # does both insert and update
        # get the bucket list where this item will go.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # update key if it is already in the bucket
        for kv in bucket_list:
            # print (key_value)
            if kv[0] == key:
                kv[1] = item
                return True

        # if not, insert the item to the end of the bucket list.
        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    # Searches for an item with matching key in the hash table.
    # Returns the item if found, or None if not found.
    def search(self, key):
        # get the bucket list where this key would be.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # search for the key in the bucket list
        for kv in bucket_list:
            # print (key_value)
            if kv[0] == key:
                return kv[1]  # value
        return None

    # Removes an item with matching key from the hash table.
    def remove(self, key):
        # get the bucket list where this item will be removed from.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # remove the item from the bucket list if it is present.
        for kv in bucket_list:
            # print (key_value)
            if kv[0] == key:
                bucket_list.remove([kv[0], kv[1]])


def loadPackageData(fileName, hashTable):
    with open(fileName) as packageFile:
        packageData = csv.reader(packageFile, delimiter=',')
        for line in range(8):
            next(packageData)  # skip header
        for package in packageData:
            packageID = int(package[0])
            packageAddress = package[1]
            packageCity = package[2]
            packageState = package[3]
            packageZip = int(package[4])
            packageDelivery = package[5]
            packageMass = int(package[6])
            packageNotes = package[7]

            # movie object
            newPackage = Package(packageID, packageAddress, packageCity, packageState, packageZip,
                                 packageDelivery, packageMass, packageNotes, " at HUB")
            # print(newPackage)

            # insert it into the hash table
            hashTable.insert(packageID, newPackage)


def loadDistanceData(distanceDataInput):
    with open('WGUPS Distance Table.csv') as locationFile:
        locationData = csv.reader(locationFile, delimiter=',')
        for line in range(5):
            next(locationData)  # skip header
        for row in locationData:
            readString = row[2:]
            intConversion = list(map(float, readString))
            distanceDataInput.append(intConversion)


def loadAddressData(addressDataInput):
    with open('WGUPS Distance Table.csv') as locationFile:
        locationData = csv.reader(locationFile, delimiter=',')
        for line in range(5):
            next(locationData)  # skip header
        for row in locationData:
            # Currently extracting street address only. Eliminate second index for zip
            addressDataInput.append(row[1][1:-8])
