import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random


FILE_ADD = "Tarbiat.csv"

df = pd.read_csv(FILE_ADD)

fig, ax = plt.subplots()

# Create a histogram with two colors
plt.hist(df, color=["orange", "blue"])

# Set labels for each color
# plt.legend(['First Column', 'Second Column'])

ax.set_xlabel("Pass")
ax.set_ylabel("frequency")
ax.set_title("Histogram")

# Show histogram
plt.legend(['First Column', 'Second Column'])
plt.show()
