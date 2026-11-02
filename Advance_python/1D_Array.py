import numpy as np
marks=np.array([50,60,70,80,90])

print(marks)

print("Dim:",marks.ndim)

print(marks[0])
print(marks [3])
print(marks[-1])
print(marks[1:4])

print("\nSum:",np.sum(marks))
print("Mean:", np.mean(marks))
print("Maximum:", np.max(marks))
print("Minimum:", np.min(marks))

marks_modify = marks *5
print("\nModified Marks:", marks_modify)
