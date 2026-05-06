import pandas as pd

#Data
Name=['Amit','Riya','Kiran']
Age=[20, 19, 21] 
Marks=[85,92,76]
#data= {'Name':['Amit','Riya','Kiran'], 'Age':[20, 19, 21], 'Marks':[85,92,76]}
#df= pd.DataFrame(data)
df= pd.DataFrame({'Name':Name,'Ages':Age,'Marks':Marks})
print("Student DataFrame")
print(df)