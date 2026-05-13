import numpy as np
import matplotlib.pyplot as plt

#data = np.random.randn(1000)
#data = np.random.rand(1000)
data = np.random.normal(loc=50, scale=10, size=1000)
plt.hist(data, bins=10, color='burlywood', edgecolor='black')

plt.xlabel("value")
plt.ylabel("Frequency")
plt.title("Histogram of Random Numbers")
plt.grid(True)
plt.show()