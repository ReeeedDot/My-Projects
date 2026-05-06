import pandas as pd

values= [100, 200, 300]
indexes= ['a','b', 'c']

series= pd.Series(values, index=indexes)
print("Custom Indexed Series:")
print(series)
#print(series['b'])