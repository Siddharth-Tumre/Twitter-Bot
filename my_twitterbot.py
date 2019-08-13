import tweepy
import time

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

user = api.me()
print(user.name)


def main():
    search = ("100DaysOfCode")

    numberOfTweets = 10
    for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
        try:
            tweet.favorite()
            print("Tweet Liked")
        except tweepy.TweepError as e:
            print(e.reason)
