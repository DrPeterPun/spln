import pandas as pd

df = pd.read_csv("Tweets_pt_pt.csv")

df = df[['sentiment','tweet_text']]
print(df)

df['sentiment']= df['sentiment'].map('__Label__{}',format)
print(df)

df.to_csv('tweets.csv',index=False, header=False, sep=' ',quotechar=' ')
