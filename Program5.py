import pandas as pd

pd.options.display.max_columns = None
pd.options.display.max_rows = None
pd.set_option('display.max_colwidth', None)

canadian_youtube = pd.read_csv("CAvideos.csv")
british_youtube = pd.read_csv("GBvideos.csv")

concat_data= pd.concat([canadian_youtube, british_youtube])
print("List of Columns:",concat_data.columns)

print(canadian_youtube)