import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[5,10,15,20,25]

plt.plot(x, y, linewidth='5', color='grey', marker='s', markersize='10', markerfacecolor='blue')
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("Modify Line With Square Marker")
plt.show()