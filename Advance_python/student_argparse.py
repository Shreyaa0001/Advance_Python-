import csv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--file", required=True)
args = parser.parse_args()

# Display all records
print("Student Records:")
with open(args.file, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)

# Search by Roll Number
roll = input("\nEnter Roll Number: ")

with open(args.file, "r") as file:
    reader = csv.DictReader(file)

    found = False
    for row in reader:
        if row["RollNo"] == roll:
            print("\nStudent Found:")
            print(row)
            found = True
            break

    if not found:
        print("Student not found")