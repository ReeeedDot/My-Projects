import matplotlib.pyplot as plt
import numpy as np

x= np.arange(0, 3* np.pi, 0.1)
y= np.sin(x)
plt.title("Sine Wave")

#plot the points using matplotlib
plt.plot(x, y)
plt.show()