import matplotlib.pyplot as plt


marks= [45,56,67,45,89,90,56,78,67,45,89]
num_bins=5
n,bins,patches = plt.hist(marks, num_bins, facecolor='green', alpha=1,)
plt.xlabel("Marks")
plt.ylabel("Repeat Count")
plt.title("Marks Chart")
plt.show()