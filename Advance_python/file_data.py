import csv

with open('data.csv', 'w', newline='') as file:
    content = csv.writer(file)
    content.writerow(['Name', 'Age', 'City'])
    content.writerow(['Alice', 30, 'New York'])