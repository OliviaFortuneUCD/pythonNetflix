import pandas as pd

canadian_youtube = pd.read_csv("CAvideos.csv")
british_youtube = pd.read_csv("GBvideos.csv")



#set index is to increase the speed of access.

left = canadian_youtube.set_index(['title', 'trending_date'])
right = british_youtube.set_index(['title', 'trending_date'])

leftfiltered =left.filter(regex ='[Spiderman]')
print(leftfiltered)
