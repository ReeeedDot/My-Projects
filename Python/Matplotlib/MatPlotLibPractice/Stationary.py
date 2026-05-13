import matplotlib.pyplot as plt
import numpy as np
items= ["Pen", "Pencil","Eraser", "Scale"]
price = [10, 5, 7, 15]

x= np.arange(len(items))
width=1
plt.bar(x , price, color='orange',width=0.3, edgecolor='blue')
plt.xticks(x, items)
plt.ylabel("Price")
plt.title("Stationary Items Price")
plt.grid(True, color='black', alpha=0.4)
plt.show()