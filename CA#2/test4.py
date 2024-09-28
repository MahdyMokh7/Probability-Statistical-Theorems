import matplotlib.pyplot as plt

# Create two subplots in a single figure
fig, (ax1, ax2) = plt.subplots(1, 2)

# Plot your first graph in the first subplot
ax1.plot(x_values, y_values1)
ax1.set_title('Graph 1')
ax1.set_xlabel('X-axis')
ax1.set_ylabel('Y-axis')

# Plot your second graph in the second subplot
ax2.plot(x_values, y_values2)
ax2.set_title('Graph 2')
ax2.set_xlabel('X-axis')
ax2.set_ylabel('Y-axis')

# Tighten the layout to ensure the plots are displayed side by side
plt.tight_layout()
plt.show()
