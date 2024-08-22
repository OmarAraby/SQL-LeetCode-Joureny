import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    len_tweet = tweets['content'].str.len()>15
    return tweets[len_tweet][['tweet_id']]
    