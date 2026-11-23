import matplotlib.pyplot as plt

# 1. Define the data points (X and Y coordinates)
x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 5, 3]

# 2. Create the line plot
plt.plot(x, y)

# 3. Add titles and labels (optional, but recommended)
plt.title("Simple Line Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

# 4. Display the chart
plt.show()