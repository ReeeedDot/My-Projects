import matplotlib.pyplot as plt
import numpy as np

x= np.linspace(0,10,100)
y = np.sin(x)

plt.figure(figsize=(8,5))
plt.plot(x, y, label="sin(x)", color="blue", linewidth=2)

plt.grid(True)
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("Line Plot Example")
plt.legend()

plt.savefig("chart.png")

plt.show()