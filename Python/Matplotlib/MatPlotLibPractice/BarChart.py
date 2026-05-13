import matplotlib.pyplot as plt
import numpy as np
fruits = ["Apple", "Banana", "Orange", "Mango"]
sales = [50,70,40,65]
y_pos= np.arange(len(fruits))
plt.bar(y_pos, sales, align='center', alpha=1, color='green')
plt.title("Fruits Sales")
plt.xticks(y_pos, fruits)
plt.ylabel("sales")
plt.show()