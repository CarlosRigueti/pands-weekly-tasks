# HelloWorld.py
# This program just print out Hello World.
# Autor: Carlos Rigueti

import matplotlib.pyplot as plt
import numpy as np

# Generating 1000 random values from a normal distribution
mean = 5
std_dev = 2
num_values = 1000
data = np.random.normal(mean, std_dev, num_values)

# Plot of histogram
plt.figure(figsize=(8, 6))
plt.hist(data, bins=30, color='skyblue', edgecolor='black')
plt.title('Histogram of Normal Distribution')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# Defining the function.
def h(x):
    return x ** 3

# Generating values for x.
x_values = np.linspace(0, 10, 100)

# Calculating corresponding y values using the function h(x)
y_values = h(x_values)

# Plotting the function
plt.figure(figsize=(8, 6))
plt.plot(x_values, y_values, color='green')
plt.title('Plot of the function h(x) = x^3')
plt.xlabel('x')
plt.ylabel('h(x)')
plt.grid(True)
plt.show()