#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import sys
import couchdb
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener 
from textblob import TextBlob
from getSuburb import CoordinateToSA2

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
	return polarity

class MyStreamListener(StreamListener):
	def __init__(self, db, sa2):
		self.db = db
		self.sa2 = sa2

	def on_data(self, data):
		try:
			tweet = json.loads(data)

			if tweet['coordinates'] or tweet['geo'] or tweet['place']:
				text = tweet['text']

				polarity = sentimentAnalysis(text)
				tweet['sentiment'] =  float('%.6f' % polarity)

				sa2_code = None
				sa2_name = None
				if tweet['coordinates']:
					sa2_code, sa2_name = sa2.sa2_maincode(tweet['coordinates']['coordinates'])

				tweet['sa2_code'] = sa2_code
				tweet['sa2_name'] = sa2_name
				
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

	sa2 = CoordinateToSA2()

	myStreamListener = MyStreamListener(db, sa2)
	myStream = Stream(auth=auth, listener=myStreamListener)
	myStream.filter(locations=locations, languages=['en'])

if __name__ == '__main__':
	main()