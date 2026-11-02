import csv
file = open('student.csv', 'w')
content = csv.writer(file)
content.writerow(['RollNo', 'Name', 'Course', 'Marks'])
content.writerow(['101', 'Amit', 'BCA', '85'])
content.writerow(['102', 'Priya', 'BSc', '90'])
content.writerow(['103', 'Rahul', 'BCom', '78'])
content.writerow(['104', 'Neha', 'BCA', '88'])
file.close()
