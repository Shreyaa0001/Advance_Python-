import numpy as np

# Create a 1-D NumPy array from 1 to 10
arr = np.arange(1, 11)

print("Original Array:")
print(arr)

# Slicing operations
print("\nFirst 5 elements:")
print(arr[:5])

print("\nElements from index 3 to 7:")
print(arr[3:8])

print("\nLast 3 elements:")
print(arr[-3:])

# Statistical measures
print("\nStatistical Measures")
print("Sum =", np.sum(arr))
print("Mean =", np.mean(arr))
print("Maximum =", np.max(arr))
print("Minimum =", np.min(arr))

# Broadcasting (add 5 to each element)
modified_arr = arr + 5

print("\nArray after Broadcasting (Adding 5):")
print(modified_arr)