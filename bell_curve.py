import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read in data from Excel file
data = pd.read_excel('/content/bell curve (1).xlsx')

# Create a bell-shaped curve using a normal distribution
mu = data['z'].mean()
sigma = data['z'].std()
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
y = 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (x - mu)**2 / (2 * sigma**2) )

# Plot the curve
plt.plot(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Bell Curve')
plt.show()