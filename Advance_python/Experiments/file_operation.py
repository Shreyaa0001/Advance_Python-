# Create and write to myfile.txt
f = open("myfile.txt", "w")
f.write("Hello, World!")
f.write("\nWelcome to file operations in Python.\nThis is a sample text file.")
f.close()

# Copy contents to myfile2.txt
f = open("myfile.txt", "r")
f1 = open("myfile2.txt", "w")
data = f.read()
f1.write(data)
f.close()
f1.close()

# Read lines from myfile.txt
f = open("myfile.txt", "r")
lines = f.readlines()
f.close()

# Count lines
count = len(lines)
print("Number of lines:", count)

# Display first two lines
twolines = lines[:2]
print("First two lines:")
print(twolines)

# Write first two lines to myfile2.txt
f1 = open("myfile2.txt", "a")   # open again in append mode
for line in twolines:
    f1.write("\n" + line)
f1.close()