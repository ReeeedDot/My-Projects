import matplotlib.pyplot as plt

x=[21,22,23,4,5,6,77,8,9,10,31,32,34,45,46,65,60,49,50,100]
num_bins=10
n,bins,patches = plt.hist(x, num_bins, facecolor='green', alpha=1, edgecolor='black')
plt.xlabel("Distribution")
plt.ylabel("Frequency")
plt.title("Histogram Chart")
plt.show()