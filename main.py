# LYNDON PEARSON STUDENT ID: 010389649
# See "Documentation" folder for algorith overview Word document
from manageData import PackageHashTable
from PackageDeliveryProgram import packageDeliveryProgram

packageTable = PackageHashTable()

# The main file called first in the program.
# If the user presses 1, the entire package
# delivery program is executed and total stats
# are displayed to console.
# If the user presses 2, they are prompted for
# a time. The package delivery program is ran
# until that time, at which a complete status
# report of all packages is displayed to console.
# If the user presses 3, the program terminates
if __name__ == '__main__':

    # loop until user is satisfied
    isExit = True
    while isExit:
        print("\nOptions:")
        print("1. Run package delivery routes, print completion time and total miles traveled")
        print("2. Get all package status at input time")
        print("3. Exit the Program")
        option = input("Chose an option (1,2, or 3): \n")
        if option == "1":
            packageDeliveryProgram(packageTable)
        elif option == "2":
            optionTime = input("Please enter time in format HH:MM ")
            (h, m) = optionTime.split(':')
            inputTime = float(h) + float(m) / 60
            print("###################### PACKAGE STATUS REPORT AT " + optionTime + ": ##########################")
            packageDeliveryProgram(packageTable, inputTime)
        elif option == "3":
            isExit = False
        else:
            print("Wrong option, please try again!")
        # main - END
