import csv
import math
import string

from Truck import Truck
from readCSV import ChainingHashTable, loadPackageData, loadDistanceData, loadAddressData, Package

myHash = ChainingHashTable()
# Load movies to Hash Table
loadPackageData('WGUPS Package File.csv', myHash)

# print("Packages from Hashtable:")
# # Fetch data from Hash Table
# for i in range(len(myHash.table) + 1):
#     print("Package: {}".format(myHash.search(i + 1)))  # 1 to 11 is sent to myHash.search()

# Create Distance & Address Lists
distanceData = []
addressData = []

# Load the lists with data
loadDistanceData(distanceData)
loadAddressData(addressData)

# print(addressData)

print("*******************************************************")
Truck1 = Truck(1)

package1 = myHash.search(1)
package2 = myHash.search(22)

print("Package 1 status: " + package1.status)

print("*******************************************************")

Truck1.loadPackage(package1)
Truck1.loadPackage(package2)

print("Package 1 status: " + package1.status)

print("*******************************************************")

count = 0
for address in addressData:
    stripAddress = address.lstrip()
    if stripAddress == Truck1.getPackage(1).getAddress():
        destIndex = count
        break
    count += 1

count = 0
for address in addressData:
    stripAddress = address.lstrip()
    if stripAddress == Truck1.location:
        sourceIndex = count
        break
    count += 1

distance = distanceData[sourceIndex][destIndex]
Truck1.deliverPackage(distance)

print("*******************************************************")

print("Package 1 status: " + package1.status)

print("*******************************************************")
print("Leg distance: " + distance)
print("Total Truck distance" + str(Truck1.distanceTraveled))

print("*******************************************************")
Truck1.updateTime()
print("Current time: " + str(Truck1.time))


# Manually load 10 items on truck 1, have it deliver, track time/status, print to console, etc. before optimizing