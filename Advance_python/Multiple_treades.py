import threading
import time

# Task 1: Print numbers
def print_numbers():
    for i in range(1, 6):
        print(f"Number Thread: {i}")
        time.sleep(1)

# Task 2: Print alphabets
def print_alphabets():
    for ch in ['A', 'B', 'C', 'D', 'E']:
        print(f"Alphabet Thread: {ch}")
        time.sleep(1)

# Task 3: Print squares
def print_squares():
    for i in range(1, 6):
        print(f"Square Thread: {i}² = {i*i}")
        time.sleep(1)

# Create threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_alphabets)
t3 = threading.Thread(target=print_squares)

# Start threads
t1.start()
t2.start()
t3.start()

# Wait for all threads to complete
t1.join()
t2.join()
t3.join()

print("\nAll threads have completed execution.")