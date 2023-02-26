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
package2 = myHash.search(23)
package3 = myHash.search(11)
package4 = myHash.search(33)
package5 = myHash.search(2)
package6 = myHash.search(3)
package7 = myHash.search(4)
package8 = myHash.search(5)
package9 = myHash.search(6)
package10 = myHash.search(7)
package11 = myHash.search(8)
package12 = myHash.search(9)
package13 = myHash.search(10)
package14 = myHash.search(15)
package15 = myHash.search(12)
package16 = myHash.search(13)


print("Package 1 status: " + package1.status)

Truck1.loadPackage(package1)
Truck1.loadPackage(package2)
Truck1.loadPackage(package3)
Truck1.loadPackage(package4)
Truck1.loadPackage(package5)
Truck1.loadPackage(package6)
Truck1.loadPackage(package7)
Truck1.loadPackage(package8)
Truck1.loadPackage(package9)
Truck1.loadPackage(package10)
Truck1.loadPackage(package11)
Truck1.loadPackage(package12)
Truck1.loadPackage(package13)
Truck1.loadPackage(package14)
Truck1.loadPackage(package15)
Truck1.loadPackage(package16)

print("*******************************************************")

for i in range(len(Truck1.packageList)):
    print("Package status: " + Truck1.getPackageByIndex(i).status)
    count = 0
    for address in addressData:
        stripAddress = address.lstrip()
        if stripAddress == Truck1.getPackageByIndex(i).getAddress():
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
    Truck1.deliverPackage(distance, i)

    print("Package status: " + Truck1.getPackageByIndex(i).status)

    print("*******************************************************")
    print("Leg distance: " + distance)
    print("Total Truck distance: " + str(Truck1.distanceTraveled))

    print("*******************************************************")
    Truck1.updateTime()
    print("Current time: " + str(Truck1.time))
    print("*******************************************************")


# Manually load 10 items on truck 1, have it deliver, track time/status, print to console, etc. before optimizing