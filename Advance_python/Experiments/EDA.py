import matplotlib.pyplot as plt
# Sample customer  data
customers = ["c101", "c102", "c103", "c104", "c105", "c106"]
charges = [500, 800, 600, 700, 650, 900]
tenure = [12, 3, 24, 6, 18, 2]
churn = ["No", "Yes", "No", "Yes", "No", "Yes"]

# Count  churn  categgories
yes_count  = churn.count("Yes")
no_count = churn.count ("No")

# Create  one  windlow for 
#all  graphs
plt.figure(figsize=(14, 9))

# 1. BAR GRAPH
plt.subplot(2, 3, 1)
plt.bar(customers, charges)
plt.xlabel("CustomerID")
plt.ylabel("Monthly Charges")
plt.title("Bar Graph")
plt.xticks(rotation=45)
plt.ylabel("Monthly Charges")
plt.title("Bar  Graph")
plt.xticks(rotation=45)

# 2. HISTOGRAM
plt.subplot(2, 3, 2)
plt.hist(charges, bins=5, edgecolor="black")
plt.xlabel("Monthly Charges")
plt.ylabel("Number of Customers ")
plt.title("Histogram")

# 3.  PIE  CHART
plt.subplot(2,  3, 3)
plt.pie(
[yes_count, no_count],
labels=["Churn  Yes", "Churn  No"],
autopct= "%1.1f%%",
startangle=90
)
plt.title("Pie Chart")

# 4. SCATTER  PLOT
plt.subplot(2,  3,  4)
plt.scatter(tenure, charges)
plt.xlabel("Tenure (Months)")
plt.ylabel("Monthly Charges")
plt.title("Scatter  Plot")

# 5. LINE  GRADH
plt.subplot(2, 3, 5)
plt.plot(customers, charges, marker="o")
plt.xlabel("Customer ID")
plt.ylabel("Monthly Charges")
plt.title("Line  Grraph")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

