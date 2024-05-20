import tweepy
from app.config import TWITTER_API_KEY, TWITTER_API_SECRET_KEY, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET

def fetch_tweets(query):
    try:
        auth = tweepy.OAuth1UserHandler(TWITTER_API_KEY, TWITTER_API_SECRET_KEY, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
        api = tweepy.API(auth)
        tweets = api.search_tweets(q=query, count=10)
        return [tweet.text for tweet in tweets]
    except tweepy.TweepyException as e:
        print(f"Twitter API error: {e}")
        return None

if __name__ == '__main__':
    query = 'AI'
    tweets = fetch_tweets(query)
    if tweets:
        print(tweets)
