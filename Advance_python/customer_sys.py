import csv
import re
def display_customers():
    print("\nCustomer Records:")
    with open("customers.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row)
def search_customer(acc_no):
    with open("customers.csv", "r") as file:
        reader = csv.DictReader(file)
        found = False

        for row in reader:
            if row["AccountNo"] == acc_no:
                print("\nCustomer Found:")
                print("Account No :", row["AccountNo"])
                print("Name       :", row["Name"])
                print("Balance    :", row["Balance"])
                found = True
                break
        if not found:
            print("Customer not found.")
display_customers()
acc_no = input("\nEnter Account Number to search: ")
pattern = r"^ACC\d{4}$"
if re.match(pattern, acc_no):
    search_customer(acc_no)
else:
    print("Invalid Account Number Format!")
    print("Format should be like: ACC1001")