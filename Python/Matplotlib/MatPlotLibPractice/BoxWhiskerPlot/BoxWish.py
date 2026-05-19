import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Load the dataset
df= pd.read_csv(r'D:\Code\Python\Matplotlib\MatPlotLibPractice\BoxWhiskerPlot\tips1.csv')
df.boxplot(by ='day', column=['total_bill'], grid=False)

plt.show()