import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.figure(figsize=(8, 5))

plt.style.use("seaborn-v0_8-darkgrid")
plt.plot(x, y1, label="sin(x)", color='grey', linewidth=2)
plt.plot(x, y2, label="cos(x)", color='red', linestyle='--', linewidth='2')
plt.grid(True)
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("Line Plot of sin(x) and cos(x)")
plt.legend()
plt.show()