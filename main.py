from prettytable import PrettyTable
import csv


def get_input(prompt: str, validation_func=None, error_msg="Invalid input, please try again."):
    while True:
        value = input(prompt)
        if validation_func is None or validation_func(value):
            return value
        else:
            print(error_msg)


def is_non_empty_string(value: str):
    return value.strip() != ""


def is_yes_no(value: str):
    return value.lower() in ["yes", "no"]


def is_valid_iin(value: str):
    return value.isdigit() and len(value) == 12


def add_or_edit_student(lst: list, index=None):
    name1 = get_input("Enter the student's first name: ", is_non_empty_string)
    name2 = get_input("Enter the student's last name: ", is_non_empty_string)
    name3 = get_input("Enter the student's patronymic (if any): ")
    form = get_input("Is the student on a scholarship? yes/no: ", is_yes_no)
    iin = get_input("Enter the student's IIN: ", is_valid_iin)
    group = get_input("Enter the student's group: ", is_non_empty_string)
    address = get_input("Enter the student's address: ", is_non_empty_string)

    student_data = [name1, name2, name3, form, iin, group, address]
    if index is None:
        lst.append(student_data)
    else:
        lst[index] = student_data


def remove_student(lst: list, index):
    lst.pop(index)


def get_int(prompt: str, max_value: int):
    while True:
        try:
            value = int(input(prompt))
            if 0 <= value < max_value:
                return value
            else:
                print(f"Value must be between 0 and {max_value - 1}.")
        except ValueError:
            print("Invalid input, please enter a number.")


def search_student(lst: list):
    first_name = get_input("Enter the student's first name to search: ", is_non_empty_string)
    results = [student for student in lst if student[0].lower() == first_name.lower()]

    if results:
        table = create_table(results)
        print("Search Results:")
        print(table)
    else:
        print("No students found with that first name.")


def sort_students(lst: list, attribute_index: int):
    lst.sort(key=lambda x: x[attribute_index])


def create_table(lst: list):
    table = PrettyTable()
    table.field_names = ["INDEX", "FIRST NAME", "LAST NAME", "PATRONYMIC", "ON SCHOLARSHIP", "IIN", "GROUP", "ADDRESS"]
    for i, student in enumerate(lst):
        table.add_row([i] + student)
    return table


def write_csv(lst: list):
    with open('students.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(lst)


loop_flag = True
change_flag = False
students = []

try:
    with open('students.csv', newline='') as f:
        reader = csv.reader(f)
        students = [row for row in reader]
        print(create_table(students))
except FileNotFoundError:
    print("Database file of students not found! The list of students is empty!")
    print("When adding students to the list, the file will be created automatically.")

while loop_flag:
    if not students:
        print("The list of students is empty!")

    print("Select the action number:")
    print("1. Add, 2. Edit, 3. Delete, 4. Clear All, 5. Search, 6. Sort, 0. Exit")
    user_input = get_input("", lambda x: x in ["0", "1", "2", "3", "4", "5", "6"],
                           "Invalid selection, please try again.")

    if user_input == "1":
        add_or_edit_student(students)
        change_flag = True

    if user_input == "2":
        if students:
            index = get_int("Enter the student index to edit: ", len(students))
            add_or_edit_student(students, index)
            change_flag = True

    if user_input == "3":
        if students:
            index = get_int("Enter the student index to delete: ", len(students))
            remove_student(students, index)
            change_flag = True

    if user_input == "4":
        sure = get_input("Are you sure? yes/no: ", is_yes_no)
        if sure.lower() == "yes":
            students.clear()
            change_flag = True

    if user_input == "5":
        search_student(students)

    if user_input == "6":
        print("Sort by: 1. First Name, 2. Last Name, 3. IIN")
        sort_choice = get_input("", lambda x: x in ["1", "2", "3"], "Invalid selection, please try again.")
        sort_students(students, int(sort_choice) - 1)
        change_flag = True

    if user_input == "0":
        loop_flag = False

    if change_flag:
        print(create_table(students))
        write_csv(students)
        change_flag = False
