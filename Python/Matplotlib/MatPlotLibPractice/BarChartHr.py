import matplotlib.pyplot as plt
import numpy as np
students = ["Aman", "Riya", "Kunal", "Neha"]
scores = [85,90,78,88]
y_pos= np.arange(len(students))
plt.barh(y_pos, scores, align='center', alpha=0.5, color='purple', )
plt.title("Students Scores")
plt.yticks(y_pos, students)
plt.xlabel("scores")
plt.grid(True, linestyle='--')
plt.show()