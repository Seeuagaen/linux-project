from prettytable import PrettyTable
import csv

# function to add a student to the list
def addStudent(lst: list):
    while True:
        name1 = input("Enter the student's first name: ")
        name2 = input("Enter the student's last name: ")
        name3 = input("Enter the student's patronymic (if any): ")
        form = input("Is the student on a scholarship? yes/no: ")
        iin = getIIN()
        group = input("Enter the student's group: ")
        address = input("Enter the student's address: ")
        if name1 != "":
            lst.append([name1, name2, name3, form, iin, group, address])
            break
        else:
            print("Please fill in the fields again.")
            continue

# function to edit student data
def EditStudent(lst: list, index):
    while True:
        name1 = input("Enter the student's first name: ")
        name2 = input("Enter the student's last name: ")
        name3 = input("Enter the student's patronymic (if any): ")
        form = input("Is the student on a scholarship? yes/no: ")
        iin = getIIN()
        group = input("Enter the student's group: ")
        address = input("Enter the student's address: ")
        if name1 != "":
            lst[index] = [name1, name2, name3, form, iin, group, address]
            break
        else:
            print("Please fill in the fields again.")
            continue

# function to remove a student from the list
def RemoveStudent(lst: list, index):
    lst.pop(index)

# function to get a safe index
def getINT() -> int:
    while True:
        try:
            index = int(input("Enter the student index: "))
        except:
            print("You entered a non-numeric value, please try again.")
            continue
        if index <= (len(Students) - 1):
            return index
        else:
            print("There is no such index in the list.")
            continue

# function to get a numeric IIN
def getIIN() -> int:
    while True:
        try:
            iin = int(input("Enter the student's IIN: "))
            return iin
        except:
            print("You entered a non-IIN value, please try again.")
            continue

# function to add rows to the Table object
def row_table(lst: list):
    i = 0
    for element in lst:
        Table.add_row(
            [i, Students[i][0], Students[i][1], Students[i][2], Students[i][3], Students[i][4], Students[i][5],
             Students[i][6]])
        i = i + 1

# function to write the list to a CSV file
def write_CSV(lst: list):
    with open('students.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        for row in lst:
            writer.writerow(row)

loopFlag = True  # loop flag
changeFlag = False  # list change flag

# create a Table instance and assign column headers
Table = PrettyTable()
Table.field_names = ["INDEX", "FIRST NAME", "LAST NAME", "PATRONYMIC", "ON SCHOLARSHIP", "IIN", "GROUP", "ADDRESS"]

Students = []

# try to open the file with student data at the beginning of the program
try:
    with open('students.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            Students.append(row)
        row_table(Students)
        print(Table)
except FileNotFoundError:
    print("*********************************************")
    print("DATABASE FILE OF STUDENTS NOT FOUND!")
    print("*********************************************")
    print(Table)
    print("The list of students is empty!")
    print("When adding students to the list, the file will be created automatically.")

# MAIN LOOP
while loopFlag:
    if len(Students) == 0:
        print("The list of students is empty!")

    print("Select the action number")
    print("add 1, edit 2, delete 3, clear all 4, exit the program 0")
    userInput = input()

    if userInput == "1":
        addStudent(Students)
        changeFlag = True

    if userInput == "2":
        indexIn = getINT()
        EditStudent(Students, indexIn)
        changeFlag = True

    if userInput == "3":
        indexIn = getINT()
        RemoveStudent(Students, indexIn)
        changeFlag = True

    if userInput == "4":
        sure = input("Are you sure? yes/no (all data will be deleted!)")
        if sure.lower() == "yes":
            Students.clear()
            changeFlag = True

    if userInput == "0":
        loopFlag = False

    if changeFlag:
        Table.clear_rows()  # clear previously drawn table rows
        row_table(Students)  # fill table rows for display from the student list
        print(Table, "\n")  # display the table on the screen
        write_CSV(Students)  # write data from the list to the CSV file
        changeFlag = False  # all changes are recorded and there are no
