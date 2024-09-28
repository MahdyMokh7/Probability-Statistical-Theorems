import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

# Creating data for the main graph
x = np.arange(0, 10, 0.1)
y = np.sin(x)

# Creating data for the Poisson distribution graph
mu = 3
x_poisson = np.arange(0, 10)
y_poisson = poisson.pmf(x_poisson, mu)

# Plotting the main graph
plt.plot(x, y, label='Main Graph')

# Plotting the Poisson distribution graph
plt.bar(x_poisson, y_poisson, label='Poisson Distribution', alpha=.7)

# Adding labels and legend
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()

# Displaying the combined graph
plt.show()
