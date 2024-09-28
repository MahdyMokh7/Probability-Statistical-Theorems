import pandas as pd
import matplotlib.pyplot as plt

FILE_ADD = "Tarbiat.csv"

df = pd.read_csv(FILE_ADD)

# Create a histogram of the `Pass` column
plt.hist(df)
plt.xlabel("Pass")
plt.ylabel("Frequency")
plt.title("Histogram")

plt.show()

# Create a scatter plot of the `Pass` and `Total` columns
plt.bar(100, 5000)
plt.xlabel("Pass")
plt.ylabel("Total")
plt.title("Scatter Plot")

plt.show()


import matplotlib.pyplot as plt
import numpy as np

# Generate data from Poisson distribution
lambda_value = 4
data = np.random.poisson(lambda_value, 100)

# Create a bar chart
plt.bar(data, height=np.ones_like(data))
plt.xlabel('Number of events')
plt.ylabel('Frequency')
plt.title('Poisson distribution with lambda = 4')
plt.show()
