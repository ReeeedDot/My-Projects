import matplotlib.pyplot as plt

Subjects =[1,2,3,4,5]
Marks =[67,72,90,81,75]

plt.plot(Subjects, Marks, color='green', linestyle='--', marker='o')
plt.title("Student VS Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.grid(True)
plt.show()
