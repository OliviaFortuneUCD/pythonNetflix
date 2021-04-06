import pandas as pd

canadian_youtube = pd.read_csv("CAvideos.csv")
british_youtube = pd.read_csv("GBvideos.csv")

concat_data= pd.concat([canadian_youtube, british_youtube])

