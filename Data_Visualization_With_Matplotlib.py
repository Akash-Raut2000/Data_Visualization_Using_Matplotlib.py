# Importing the required libraries
import matplotlib.pyplot as plt
import numpy as np

# Step 1: Create a Random Dataset
# Generate random data for plotting
categories = ['A', 'B', 'C', 'D', 'E']
values = np.random.randint(1, 10, size=5)  # Random values between 1 and 10

# Step 2: Line Plot
# Creating a line plot
plt.figure(figsize=(8, 6))
plt.plot(categories, values, marker='o', linestyle='-', color='b', label='Line Plot')
plt.title('Line Plot Example')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.legend()
plt.grid(True)
plt.show()

# Step 3: Bar Plot
# Creating a bar plot
plt.figure(figsize=(8, 6))
plt.bar(categories, values, color='orange')
plt.title('Bar Plot Example')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()

# Step 4: Pie Chart
# Creating a pie chart
plt.figure(figsize=(8, 6))
plt.pie(values, labels=categories, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
plt.title('Pie Chart Example')
plt.show()

