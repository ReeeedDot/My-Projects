import matplotlib.pyplot as plt
import numpy as np
subjects=["MATH", "SCIENCE", "ENGLISH"]
boys=[78,85,80]
girls=[82,88,84]
x = np.arange(len(subjects))
width=0.35
plt.bar(x - width/2, boys, width, color='skyblue', label='Boys', edgecolor='black')
plt.bar(x + width/2, girls, width, color='green',label="Girls", edgecolor='black')
plt.xticks(x, subjects)
plt.ylabel("MARKS")
plt.title("BOYS vs GIRLS")
plt.legend()
plt.show()