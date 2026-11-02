import numpy as np

marks = np.array([75, 92, 68, 85, 90, 78, 95, 82])

print("Student Marks:", marks)
print("Mean Marks:", np.mean(marks))
print("Median Marks:", np.median(marks))
print("Maximum Marks:", np.max(marks))
print("Minimum Marks:", np.min(marks))

high_scores = marks[marks > 80]
print("\nMarks greater than 80:")
print(high_scores)

==============================================================================================================================================================================
PS C:\Users\ASUS\ShreyaaExcel> & C:\Users\ASUS\AppData\Local\Programs\Python\Python314\python.exe c:/Users/ASUS/ShreyaaExcel/.vscode/Student_sys.py
Student Marks: [75 92 68 85 90 78 95 82]
Mean Marks: 83.125
Median Marks: 83.5
Maximum Marks: 95
Minimum Marks: 68

Marks greater than 80:
[92 85 90 95 82]
PS C:\Users\ASUS\ShreyaaExcel
