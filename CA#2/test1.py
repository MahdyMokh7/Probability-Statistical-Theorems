import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random


FILE_ADD = "Tarbiat.csv"
MARGIN = 1000
X_SAMPLE = 1000

df = pd.read_csv(FILE_ADD)

# Create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 6))

# Create the histogram for metro
ax1.hist(df[df.columns[0]], label=df.columns[0], color='blue')

# Create the histogram for bus
ax2.hist(df[df.columns[1]], label=df.columns[1], color='green')

# Label the axes and set the title for each subplot
ax1.set_xlabel(f'{df.columns[0]} Frequency')
ax1.set_ylabel('Number of Times')
ax1.set_title(f'{df.columns[0]} Frequencies')

ax2.set_xlabel(f'{df.columns[1]} Frequency')
ax2.set_ylabel('Number of Times')
ax2.set_title(f'{df.columns[1]} Frequencies')

ax1.legend()
ax2.legend()

plt.tight_layout()

# Show the plot
plt.show()
