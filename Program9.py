import pandas as pd
import numpy as np

pd.options.display.max_columns = None
pd.options.display.max_rows = None
pd.set_option('display.max_colwidth', None)

canadian_youtube = pd.read_csv("CAvideos.csv")
british_youtube = pd.read_csv("GBvideos.csv")

pd.options.display.max_rows = None

#set index is to increase the speed of access.

Canada = canadian_youtube.set_index(['title', 'likes'])



df = pd.DataFrame(Canada, index=['title','likes'])
print(df)