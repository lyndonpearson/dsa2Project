from GreedyAlgorithm import GreedyAlgorithm
from Truck import Truck
from manageData import PackageHashTable, loadPackageData, loadDistanceData, loadAddressData, Package

packageTable = PackageHashTable()
loadPackageData('WGUPS Package File.csv', packageTable)

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

package1 = packageTable.search(1) #10:30
package7 = packageTable.search(10)
package9 = packageTable.search(12)
package10 = packageTable.search(13) #10:30
package11 = packageTable.search(14) #10:30 must be with 15 & 19
package12 = packageTable.search(15) #9:00
package13 = packageTable.search(16) #10:30 #must be with 13 & 19
package14 = packageTable.search(19)
package15 = packageTable.search(20) #10:30 must be with 13 & 15
package16 = packageTable.search(21)


Truck1.loadPackage(package1)
Truck1.loadPackage(package7)
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
package17 = packageTable.search(3)
package18 = packageTable.search(17)
package19 = packageTable.search(18)
package20 = packageTable.search(22)
package21 = packageTable.search(23)
package22 = packageTable.search(24)
package23 = packageTable.search(33)
package24 = packageTable.search(27)
package25 = packageTable.search(29)
package26 = packageTable.search(30)
package27 = packageTable.search(31)
package28 = packageTable.search(34)
package29 = packageTable.search(36)
package30 = packageTable.search(37)
package31 = packageTable.search(38)
package32 = packageTable.search(40)


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
package33 = packageTable.search(6) #arrive 9:05, deliver 10:30
package34 = packageTable.search(9) #wrong address corrected ~11
package35 = packageTable.search(25) #arrive 9:05, deliver 10:30
package36 = packageTable.search(26)
package37 = packageTable.search(28) #arrive 9:05
package38 = packageTable.search(32) #arrive 9:05
package39 = packageTable.search(35)
package40 = packageTable.search(39)
package2 = packageTable.search(2)
package3 = packageTable.search(4)
package4 = packageTable.search(5)
package5 = packageTable.search(7)
package6 = packageTable.search(8)
package8 = packageTable.search(11)

print(package6.getStatus())
print(package6.getStatus())
print(package6.getStatus())

Truck3.loadPackage(package33)
Truck3.loadPackage(package34)
Truck3.loadPackage(package35)
Truck3.loadPackage(package36)
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

print(package6.getStatus())
print(package6.getStatus())
print(package6.getStatus())

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

print(package6.getStatus())
print(package6.getStatus())
print(package6.getStatus())

# main - START
if __name__ == '__main__':
    print("\nWelcome to C950: Classic Movies: Hash Table, CSV Import, Greedy Algorithm, Dijkstra Algorithm")

    # loop until user is satisfied
    isExit = True
    while isExit:
        print("\nOptions:")
        print("1. Load Trucks")
        print("2. Start Trucks")
        print("3. Get Status")
        print("4. Exit the Program")
        option = input("Chose an option (1,2,3 or 4): ")
        if option == "1":
            # LOAD TRUCKS (CAN LOAD 1&2 TOGETHER, TRUCK3 I THINK AT 9:05
            print("Option 1")
        elif option == "2":
            # DELIVER PACKAGES HERE, NEED TO START WITH TRUCK 1&2, THEN #3 WHEN 1 IS COMPLETE
            print("Option 2")
        elif option == "3":
            for i in range(41):
                packageTable.printPackageStatuses(i)
        elif option == "4":
            isExit = False
        else:
            print("Wrong option, please try again!")
        # main - END

