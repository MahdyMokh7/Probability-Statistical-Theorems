import matplotlib.pyplot as plt
import numpy as np

# Generate some data
x = np.arange(10)
y = x**2

# Create a line chart
plt.plot(x, y)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Line Chart')
plt.show()


import matplotlib.pyplot as plt
import numpy as np

# Generate some data
x = np.random.randn(100)
y = np.random.randn(100)

# Create a scatter plot
plt.scatter(x, y)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Scatter Plot')
plt.show()


import matplotlib.pyplot as plt
import numpy as np

# Generate some data
data = np.random.randint(1, 100, 100)

# Create a histogram
plt.hist(data)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.show()


import matplotlib.pyplot as plt

# Create some data
data = {'A': 5, 'B': 2, 'C': 3, 'D': 1}

# Create a bar chart
plt.bar(data.keys(), data.values())
plt.xlabel('Category')
plt.ylabel('Frequency')
plt.title('Bar Chart')
plt.show()



import matplotlib.pyplot as plt

# Create some data
data = {'A': 5, 'B': 2, 'C': 3, 'D': 1}

# Create a pie chart
plt.pie(data.values(), labels=data.keys(), autopct='%1.1f%%')
plt.title('Pie Chart')
plt.show()
