import requests
import numpy as np
import pandas as pd
from urllib.request import urlretrieve

URL = 'https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29'
tables = pd.read_html(URL)
df = tables[3]
print(df.columns)
print(df.head(3))
# Correcting column indexing and selection
df.columns = range(df.shape[1])
df = df[[0, 2]]
df = df.iloc[1:11, :]  # Select top 10 rows
df.columns = ['Country', 'GDP (Million USD)']

# Conversion to Billion USD
df['GDP (Million USD)'] = df['GDP (Million USD)'].astype(int)
df[['GDP (Million USD)']] = df[['GDP (Million USD)']] / 1000
df[['GDP (Million USD)']] = np.round(df[['GDP (Million USD)']], 2)

# Renaming correctly with inplace=True
df.rename(columns={'GDP (Million USD)': 'GDP (Billion USD)'}, inplace=True)

# Exporting the data
df.to_csv('./largest_economies.csv', index=False)
print("Data successfully saved as 'largest_economies.csv'")
