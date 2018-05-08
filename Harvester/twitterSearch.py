#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import sys
import couchdb
from tweepy import OAuthHandler
from tweepy import API
from textblob import TextBlob
from getSuburb import CoordinateToSA2

# Read config from file
def readConfigFromFile():
	try:
		with open('config.json', 'r') as jsonFile:
			jsonData = json.loads(jsonFile.read())
			jsonFile.close()
			return jsonData
	except:
		print('Config file error.')
		sys.exit(0)

# Connect to DB
def connectDB(db_server, db_name):
	server = couchdb.Server(db_server)
	db = server[db_name]
	return db

# Insert tweet to db
def insertTweet(db, tweet):
	try:
		if tweet['id_str'] not in db:
			db[tweet['id_str']] = tweet
	except:
		print('Insert tweet error.')

# Sentiment Analysis using TextBlob
def sentimentAnalysis(text):
	polarity = TextBlob(text).sentiment.polarity
	return polarity

# Search  Twitters
def searchTwitters(api, geocode, db, sa2):
	max_id = sys.maxsize

	while True:
		try:
			tweets = api.search(lang='en', geocode=geocode, max_id=(max_id - 1), count=100)

			i = 0
			
			if tweets:
				# Get the id of the last tweet as the max_id of next search
				max_id = tweets[len(tweets) - 1]._json['id']

				for myTweet in tweets:
					tweet = myTweet._json

					if tweet:
						text = tweet['text']

						polarity = sentimentAnalysis(text)
						tweet['sentiment'] =  float('%.6f' % polarity)

						sa2_code = None
						sa2_name = None
						if tweet['coordinates'] and tweet['coordinates']['coordinates']:
							sa2_code, sa2_name = sa2.sa2_maincode(tweet['coordinates']['coordinates'])

						tweet['sa2_code'] = sa2_code
						tweet['sa2_name'] = sa2_name

						insertTweet(db, tweet)

						i += 1
			else:
				print('No more tweets.')
				break

			print('Valid tweets count = %d' % (i))
		except:
			print('Tweets error. Continue next search.')

def main():
	config = readConfigFromFile()

	twitter_token = config['twitter_tokens'][0]
	consumer_key = twitter_token['consumer_key']
	consumer_secret = twitter_token['consumer_secret']
	access_token = twitter_token['access_token']
	access_token_secret = twitter_token['access_token_secret']
	db_server = config['db_server']
	db_name = config['db_name']
	geocode = config['geocode']

	auth = OAuthHandler(consumer_key, consumer_secret) 
	auth.set_access_token(access_token, access_token_secret)
	api = API(auth)

	db = connectDB(db_server, db_name)

	sa2 = CoordinateToSA2()

	searchTwitters(api, geocode, db, sa2)

if __name__ == '__main__':
	main()