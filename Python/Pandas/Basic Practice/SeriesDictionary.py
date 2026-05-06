import pandas as pd

#dictionary
data = {'math': 90,'Science': 85,'English': 88}

#Convert dictionary to Series
series = pd.Series(data)

print("Dictionary converted to series: ")
print(series)