import pandas as pd
import csv



pd.options.display.max_columns = None
pd.options.display.max_rows = None
pd.set_option('display.max_colwidth', None)

canadian_youtube = pd.read_csv("CAvideos.csv")
british_youtube = pd.read_csv("GBvideos.csv")

pd.options.display.max_rows = None




#CanadaSearch = canadian_youtube[canadian_youtube['title'].str.match('Ed Sheeran.*')== True]


Canadalikes = canadian_youtube[canadian_youtube['likes']> 1900000]
print(Canadalikes.title,Canadalikes.date)
#Britishlikes  = british_youtube[british_youtube['likes']> 100000]
#print(Britishlikes.likes)


