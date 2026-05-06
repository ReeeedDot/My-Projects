import pandas as pd
s = pd.Series([10, 20, 30, 40, 50])

#First 2 Element
print("First 2 Elements: ")
print(s.head(2))

#Last 2 Element
print("\nLast 2 Elements: ")
print(s.tail(2))