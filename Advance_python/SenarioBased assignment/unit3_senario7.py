import csv
from tkinter.filedialog import Open
def display_records(filename):
    try:
        with Open(filename, "r", newline="") as file:
            reader = csv.DictReader(file)

            print("\nStudent Records:")
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("Error: File not found!")
        return False
    return True
def search_student(filename, roll_no):
    with open(filename, "r", newline="") as file:
        reader = csv.DictReader(file)

        found = False
        for row in reader:
            if row["RollNo"] == roll_no:
                print("\nStudent Found:")
                print("Roll No :", row["RollNo"])
                print("Name    :", row["Name"])
                print("Marks   :", row["Marks"])
                found = True
                break

        if not found:
            print("Student not found.")
filename = input("Enter CSV file name: ")
if display_records(filename):
    roll_no = input("\nEnter Roll Number to search: ")
    search_student(filename, roll_no)
