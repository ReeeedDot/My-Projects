import pandas as pd
#Create the series
s = pd.Series([5, 10, 15, 20, 25])

#Find max min and sum
maximum = s.max()
minimum = s.min()
total = s.sum()

print("Series: ")
print(s)
print("\nMaximum:", maximum)
print("Minimum: ",minimum)
print("Sum: ", total)