#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import sys
import couchdb
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener 
from textblob import TextBlob

def readConfigFromFile():
	try:
		with open('config.json', 'r') as jsonFile:
			jsonData = json.loads(jsonFile.read())
			jsonFile.close()
			return jsonData
	except:
		print('Config file error.')
		sys.exit(0)

def connectDB(db_server, db_name):
	server = couchdb.Server(db_server)
	db = server[db_name]
	return db

def insertTweet(db, tweet):
	try:
		if tweet['id_str'] not in db:
			db[tweet['id_str']] = tweet
	except:
		print('Insert tweet error.')

def sentimentAnalysis(text):
	polarity = TextBlob(text).sentiment.polarity
	# print('textblob polarity = %f' % (polarity))
	return polarity

class MyStreamListener(StreamListener):
	def __init__(self, db):
		self.db = db

	def on_data(self, data):
		print(data)
		try:
			tweet = json.loads(data)

			if tweet['coordinates'] or tweet['geo'] or tweet['place']:
				# print(tweet['id_str'])
				text = tweet['text']
				# print(text)

				polarity = sentimentAnalysis(text)
				tweet['sentiment'] =  float('%.6f' % polarity)
				
				insertTweet(db, tweet)
		except:
			pass

		return True

	def on_error(self, status):
		print(status)

def main():
	config = readConfigFromFile()

	twitter_token = config['twitter_tokens'][0]
	consumer_key = twitter_token['consumer_key']
	consumer_secret = twitter_token['consumer_secret']
	access_token = twitter_token['access_token']
	access_token_secret = twitter_token['access_token_secret']
	db_server = config['db_server']
	db_name = config['db_name']
	locations = config['locations']

	auth = OAuthHandler(consumer_key, consumer_secret) 
	auth.set_access_token(access_token, access_token_secret)

	db = connectDB(db_server, db_name)

	myStreamListener = MyStreamListener(db)
	myStream = Stream(auth=auth, listener=myStreamListener)
	myStream.filter(locations=locations, languages=['en'])

if __name__ == '__main__':
	main()