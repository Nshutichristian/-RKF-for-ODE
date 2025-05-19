import math
import matplotlib.pyplot as plt

# Define the differential equation dy/dx = -y + ln(x)
def f(x, y):
    return -y + math.log(x)

# Perform one step of RK4
def rk4_step(x, y, h):
    k1 = f(x, y)
    k2 = f(x + h/2, y + h*k1/2)
    k3 = f(x + h/2, y + h*k2/2)
    k4 = f(x + h, y + h*k3)

    y_next = y + (h/6)*(k1 + 2*k2 + 2*k3 + k4)
    x_next = x + h

    return x_next, y_next, k1, k2, k3, k4

# Initial values
x0 = 2.0
y0 = 1.0
h = 0.3
steps = 5

# Store results
x_vals = [x0]
y_vals = [y0]

# Run RK4 for 5 steps
for i in range(steps):
    x_next, y_next, k1, k2, k3, k4 = rk4_step(x_vals[-1], y_vals[-1], h)
    x_vals.append(x_next)
    y_vals.append(y_next)
    
    print(f"x{i+1} = {x_next:.6f}, y{i+1} = {y_next:.6f}")
    print(f"k1 = {k1:.6f}, k2 = {k2:.6f}, k3 = {k3:.6f}, k4 = {k4:.6f}\n")

# Plot the results
plt.plot(x_vals, y_vals, marker='o', label="RK4 Solution")
plt.title("RK4 Solution of dy/dx = -y + ln(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.show()
