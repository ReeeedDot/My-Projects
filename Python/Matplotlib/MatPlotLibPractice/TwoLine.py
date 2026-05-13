import matplotlib.pyplot as plt

days= [1,2,3,4,5]
city1= [30,32,31,29,35]
city2= [25,28,30,27,31]

plt.plot(days, city1, linestyle='--', color='orange',marker='o', label='Line2')

plt.plot(days, city2, linestyle=':', color='black', marker='o', label='Line2')
plt.title("CITY1 VS CITY2")
plt.xlabel("DAYS")
plt.ylabel("CITY")
plt.legend()
plt.show()