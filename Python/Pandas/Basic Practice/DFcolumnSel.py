import pandas as pd

#Data

data= {'Name':['Amit','Riya','Kiran'], 'Age':[20, 19, 21], 'Marks':[85,92,76]}
df= pd.DataFrame(data)
#selected_df = df[['Name', 'Marks']]
#print(selected_df)
print(df[['Name', 'Marks']])
