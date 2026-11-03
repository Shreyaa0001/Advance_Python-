import csv
import json

with open('data.csv','w', newline = "")as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Alice", 30, "New York"])
    writer.writerow(["Bob", 25, "Los Angeles"])
    writer.writerow(["Charlie", 35, "Chicago"])
    
with open('data.csv','r') as csv_file:
    data = list(csv.reader(csv_file))
    print(data)
    
with open('data.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)
    
print("\nCSV to JSON conversion completed successfully.")
print(json.dumps(data, indent=4))        