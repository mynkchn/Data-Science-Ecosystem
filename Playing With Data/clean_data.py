import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from urllib.request import urlretrieve
import csv

recipes=pd.read_csv('recipes.csv')
print(recipes.shape)
print(recipes.columns)

recipes_with_chicken=recipes.loc[recipes['chicken']==1]
print(recipes_with_chicken)

recipes['active']=True
print(recipes)
plt.bar(recipes.cuisine,recipes.dish)
plt.xlabel('Cuisine')
plt.ylabel('Dish')
plt.title('Food data for different cuisine')
plt.show()