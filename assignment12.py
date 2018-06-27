#ques1
print("The Access Token is a credential that can be used by an application to access an API. It can be any type of token (such as an opaque string or a JWT) and is meant for an API. ... The Access Token should be used as a Bearer credential and transmitted in an HTTP Authorization header to the API")


#ques2
import socket
print(socket.gethostbyname('google.com'))
print(socket.gethostbyname('facebook.com'))


#ques3
from keys import consumer_key,consumer_secret,access_token,access_secret
import tweepy
oauth = tweepy.OAuthHandler(consumer_key,consumer_secret)
oauth.set_access_token(access_token,access_secret)
api=tweepy.API(oauth)
print(api.search("sanju"))


#ques4
print("A library is a collection of software that IMPLEMENTS an API.The “API” is a description of the interface between an application program and a library.")


#ques5
user = api.get_user('@ShubomN')
print(user.screen_name)
print(user.followers_count)
