import gc
import time

# Class to create cyclic references
class Node:
    def __init__(self):
        self.ref = self

# Function to create garbage objects
def create_objects(n):
    objects = []
    for _ in range(n):
        objects.append(Node())
    return objects

# Display GC status
print("Garbage Collection Enabled:", gc.isenabled())

# Record start time
start = time.time()

# Create cyclic objects
objs = create_objects(100000)

# Remove external references
del objs

end = time.time()
print(f"Object Creation Time: {end - start:.4f} seconds")

# Check objects tracked by GC
print("Objects tracked before collection:", len(gc.get_objects()))

# Manual garbage collection
start_gc = time.time()
collected = gc.collect()
end_gc = time.time()

print("\nManual Garbage Collection")
print("Objects Collected:", collected)
print(f"GC Time: {end_gc - start_gc:.6f} seconds")

print("Objects tracked after collection:", len(gc.get_objects()))