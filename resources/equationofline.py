import matplotlib.pyplot as plt
import numpy as np

# 1. Define slope (m) and y-intercept (b)

def y (m,x,b):
    return m*x+b


print ("the equation of the line is --> y = mx + b")
mval = float(input("Enter the value of m:\n"))
xval = float(input("Enter the value of x:\n"))
bval = float(input("Enter the y-intr (b):\n"))



y = y(mval, xval, bval)

print(f"y = mx + b\n, {y} = ({mval} x {xval}) + {bval}")

# ------------------------------------------


# 2. Generate x data points
xval = np.linspace(0, 10, 100)  # 100 evenly spaced points

# 3. Calculate corresponding y data points using y = mx + b
y = mval * xval + bval

# 4. Plot the data points as a line
slope = xval*mval
plt.plot(slope, y, label=f"y = {mval}x + {bval}", color="blue")

# Optional: Plot individual scatter points if you have raw observation data
# plt.scatter(x_data, y_data, color="red")

# 5. Customize and display the plot
plt.title("Plot of y = mx + b")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.axhline(0, color="black", linewidth=0.5)
plt.axvline(0, color="black", linewidth=0.5)
plt.grid(True)
plt.legend()
plt.show()