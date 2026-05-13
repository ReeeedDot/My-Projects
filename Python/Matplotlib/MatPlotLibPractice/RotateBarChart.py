import matplotlib.pyplot as plt
import numpy as np

categories = ["Apples", "Bananas", "Cherries", "Dates", "Elderberries"]
values1 = [10,15,7,12,9]
values2 = [8,12,6,10,11]

x = np.arange(len(categories))
width=0.35

plt.figure(figsize=(8, 5))

plt.bar(x - width/2, values1, width, label="2025", color="SkyBlue")
plt.bar(x + width/2, values2, width, label="2026", color="orange")

plt.xticks(x, categories, rotation=30)

plt.xlabel("Fruit")
plt.ylabel("Quantity")
plt.title("Fruit sales comparison", fontsize=16)

plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.legend()

plt.show()