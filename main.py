from GreedyAlgorithm import GreedyAlgorithm
from Truck import Truck
from readCSV import ChainingHashTable, loadPackageData, loadDistanceData, loadAddressData, Package

myHash = ChainingHashTable()
loadPackageData('WGUPS Package File.csv', myHash)

# Create Distance & Address Lists
distanceData = []
addressData = []

# Load the lists with data
loadDistanceData(distanceData)
loadAddressData(addressData)

print("*******************************************************")
# TRUCK 1 SECTION HERE #######################################
Truck1 = Truck(1)
Truck2 = Truck(2)
Truck3 = Truck(3)

package1 = myHash.search(1) #10:30
# package2 = myHash.search()
# package3 = myHash.search()
# package4 = myHash.search()
# package5 = myHash.search()
# package6 = myHash.search()
package7 = myHash.search(10)
# package8 = myHash.search(11)
package9 = myHash.search(12)
package10 = myHash.search(13) #10:30
package11 = myHash.search(14) #10:30 must be with 15 & 19
package12 = myHash.search(15) #9:00
package13 = myHash.search(16) #10:30 #must be with 13 & 19
package14 = myHash.search(19)
package15 = myHash.search(20) #10:30 must be with 13 & 15
package16 = myHash.search(21)


Truck1.loadPackage(package1)
# Truck1.loadPackage(package2)
# Truck1.loadPackage(package3)
# Truck1.loadPackage(package4)
# Truck1.loadPackage(package5)
# Truck1.loadPackage(package6)
Truck1.loadPackage(package7)
# Truck1.loadPackage(package8)
Truck1.loadPackage(package9)
Truck1.loadPackage(package10)
Truck1.loadPackage(package11)
Truck1.loadPackage(package12)
Truck1.loadPackage(package13)
Truck1.loadPackage(package14)
Truck1.loadPackage(package15)
Truck1.loadPackage(package16)
count = 0
while len(Truck1.packageList) > 0:
    GreedyAlgorithm(Truck1, addressData, distanceData)
    print("Total Distance Traveled: " + str(Truck1.distanceTraveled))
    count += 1
    print("Delivery #: " + str(count))
    print("Current time is: " + str(Truck1.time))
    print("*******************************************************")

# TRUCK 2 SECTION HERE ##############################################
package17 = myHash.search(3)
package18 = myHash.search(17)
package19 = myHash.search(18)
package20 = myHash.search(22)
package21 = myHash.search(23)
package22 = myHash.search(24)
package23 = myHash.search(33) #problem with #26 address?
package24 = myHash.search(27)
package25 = myHash.search(29)
package26 = myHash.search(30)
package27 = myHash.search(31)
package28 = myHash.search(34)
package29 = myHash.search(36)
package30 = myHash.search(37)
package31 = myHash.search(38)
package32 = myHash.search(40)


Truck2.loadPackage(package17)
Truck2.loadPackage(package18)
Truck2.loadPackage(package19)
Truck2.loadPackage(package20)
Truck2.loadPackage(package21)
Truck2.loadPackage(package22)
Truck2.loadPackage(package23)
Truck2.loadPackage(package24)
Truck2.loadPackage(package25)
Truck2.loadPackage(package26)
Truck2.loadPackage(package27)
Truck2.loadPackage(package28)
Truck2.loadPackage(package29)
Truck2.loadPackage(package30)
Truck2.loadPackage(package31)
Truck2.loadPackage(package32)

print("TRUCK 2 STATUS *****************************")
print("********************************************")

count = 0
while len(Truck2.packageList) > 0:
    GreedyAlgorithm(Truck2, addressData, distanceData)
    print("Total Distance Traveled: " + str(Truck2.distanceTraveled))
    count += 1
    print("Delivery #: " + str(count))
    print("Current time is: " + str(Truck2.time))
    print("*******************************************************")

# TRUCK 3 SECTION HERE ####################################
print("TRUCK 3 STATUS *****************************")
print("********************************************")
package33 = myHash.search(6) #arrive 9:05, deliver 10:30
package34 = myHash.search(9) #wrong address corrected ~11
package35 = myHash.search(25) #arrive 9:05, deliver 10:30
package36 = myHash.search(26) #problem with #26 address?
package37 = myHash.search(28) #arrive 9:05
package38 = myHash.search(32) #arrive 9:05
package39 = myHash.search(35)
package40 = myHash.search(39)
package2 = myHash.search(2)
package3 = myHash.search(4)
package4 = myHash.search(5)
package5 = myHash.search(7)
package6 = myHash.search(8)
package8 = myHash.search(11)

Truck3.loadPackage(package33)
Truck3.loadPackage(package34)
Truck3.loadPackage(package35)
Truck3.loadPackage(package36) #Address causing problems
Truck3.loadPackage(package37)
Truck3.loadPackage(package38)
Truck3.loadPackage(package39)
Truck3.loadPackage(package40)
Truck3.loadPackage(package2)
Truck3.loadPackage(package3)
Truck3.loadPackage(package4)
Truck3.loadPackage(package5)
Truck3.loadPackage(package6)
Truck3.loadPackage(package8)


Truck3.setStartingTime(Truck1.time)
count = 0
timeChangeFlag = 0
while len(Truck3.packageList) > 0:
    GreedyAlgorithm(Truck3, addressData, distanceData)
    print("Total Distance Traveled: " + str(Truck3.distanceTraveled))
    count += 1
    if Truck3.time > 10.33333 and timeChangeFlag == 0:
        package34.setAddress(package4.getAddress())
        timeChangeFlag = 1
        print("TIME CHANGE ONCE PRINT")
    print("Delivery #: " + str(count))
    print("Current time is: " + str(Truck3.time))
    print("*******************************************************")

print("****************** FINISHED AT: " + str(Truck3.time) + "*********")
print("TOTAL MILES DRIVEN: " + str(Truck1.distanceTraveled + Truck2.distanceTraveled
                                   + Truck3.distanceTraveled))
#Can also get package status directly from package object...probably better than calling truck.package.status
#print(package1.status)
#print(package1.getStatus())
