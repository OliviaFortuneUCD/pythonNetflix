import pandas as pd

import numpy as np


netflix_data = pd.read_csv("Netflix_titles.csv", index_col = 0)
pd.options.display.max_columns = None
pd.options.display.max_rows = None


missing_values_count = netflix_data.isnull().sum()
print(missing_values_count[0:5])
droprows= netflix_data.dropna()
print(netflix_data.shape,droprows.shape)
dropcolumns = netflix_data.dropna(axis=1)
print(netflix_data.shape,dropcolumns.shape)
cleaned_data = netflix_data.fillna(0)
cleaned_data = netflix_data.fillna(method='bfill', axis=0).fillna(0)
drop_duplicates= netflix_data.drop_duplicates()
print(netflix_data.shape,drop_duplicates.shape)

