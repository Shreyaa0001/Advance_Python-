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

===================OUTPUT=======================================================================================================================================================
PS C:\Users\ASUS\ShreyaaExcel> & C:\Users\ASUS\AppData\Local\Programs\Python\Python314\python.exe c:/Users/ASUS/ShreyaaExcel/customer_sys.py

Customer Records:
{'AccountNo': 'ACC1001', 'Name': 'John Doe', 'Balance': '5000'}
{'AccountNo': 'ACC1002', 'Name': 'Jane Smith', 'Balance': '3000'}
{'AccountNo': 'ACC1003', 'Name': 'Bob Johnson', 'Balance': '7000'}
{'AccountNo': 'ACC1004', 'Name': 'Alice Brown', 'Balance': '2000'}
{'AccountNo': 'ACC1005', 'Name': 'Charlie Davis', 'Balance': '10000'}

Enter Account Number to search: ACC1004

Customer Found:
Account No : ACC1004
Name       : Alice Brown
Balance    : 2000
PS C:\Users\ASUS\ShreyaaExcel> 
