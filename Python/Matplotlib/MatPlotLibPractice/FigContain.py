import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,10,100)
y_line = np.sin(x)

categories = ["A","B","C","D"]
values = [10,15,7,12]

data = np.random.rand(500)
fig, axs = plt.subplots(1,3, figsize=(15,5))

#line Chart
axs[0].plot(x, y_line, color="blue", label="sin(x)")
axs[0].set_title("Line Plot Example")
axs[0].legend()
axs[0].grid(True)

#Bar Chart
axs[1].bar(categories, values, color="orange", label="Values")
axs[1].set_title("Bar Chart Example")
axs[1].legend()
axs[1].grid(True)

#Histogram
axs[2].hist(data, bins=20, color="green", edgecolor="black",label="Random Data")
axs[2].set_title("Histogram Example")
axs[2].legend()
axs[2].grid(True)

#adjust Layout
plt.tight_layout
plt.show()