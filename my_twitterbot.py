import tweepy
import time

consumer_key = 'yTIRUzP4NWJqjwsR0uWk5elyS'
consumer_secret = 'VskINepxlop2zW5EgwI5NDrskyTx5XgSuoruVlGUOjXSYQZ2Qk'
access_token = '2322379830-nwoh5dQybcIVBA01rxAjKJ8fNQENHAQERvhB7PQ'
access_token_secret = '0zmqyT8JC0rAeDCzuEFIT4oVJBmnuaRrbemswh3p3Z5aN'

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
