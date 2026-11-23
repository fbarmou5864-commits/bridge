import matplotlib.pyplot as plt
import numpy as np

def y (m,x,b):
    return m*x+b


print ("the equation of the line is --> y = mx + b")
mval = float(input("Enter the value of m:\n"))
xval = float(input("Enter the value of x:\n"))
bval = float(input("Enter the y-intr (b):\n"))



y = y(mval, xval, bval)

print(f"y = mx + b\n, {y} = ({mval} x {xval}) + {bval}")
# 2. Create the line plot
x = mval*xval
b = bval
x = np.linspace(-5, 5, 100)
plt.plot(xval, bval)


# bval = "ylabel"
# xval * mval = "xlabel"
# 3. Add titles and labels (optional, but recommended)
plt.title("Simple Line Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

# 4. Display the chart
plt.show()