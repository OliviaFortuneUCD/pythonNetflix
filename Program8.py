import pandas as pd

canadian_youtube = pd.read_csv("CAvideos.csv")
british_youtube = pd.read_csv("GBvideos.csv")

pd.options.display.max_columns = None
pd.options.display.max_rows = None
pd.set_option('display.max_colwidth', None)

#set index is to increase the speed of access.

left = canadian_youtube.set_index(['title', 'trending_date'])
right = british_youtube.set_index(['title', 'trending_date'])

#print(left.columns)
#print(left.loc[(left.likes <= 1000) & (left.comment_count <= 10)])

print(left.loc[left.likes.between(1000, 1004),['likes']])

print(right.loc[right.likes.between(1000, 1004),['likes']])

