import pandas as pd
import re
import numpy as np
import matplotlib.pyplot as plt
import os
pd.set_option('display.max_rows',5)
pd.set_option('display.max_columns',7)
df=pd.read_csv('D:\Data Science\Playing With Data\data.csv')
print(df)
print(df.shape)
print(df.dtypes)
print(df.columns)
list=list(df['Email'])
print(list)
df=df.dropna()
check=df.isnull().sum()
print(check)
people=(df['City']).count()
print(people)
df.groupby('Country')['City'].count().plot(kind='bar') 
plt.xlabel('Country')
plt.ylabel('City')
plt.title('TO IDENTIFY WHICH CITY OR COUNTRY HAS MORE CUSTOMERS')
plt.show()