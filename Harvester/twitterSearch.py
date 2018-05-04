#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import sys
import couchdb
from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
from textblob import TextBlob
# from vaderSentiment.vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# reload(sys)
# sys.setdefaultencoding('utf-8')

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

# def sentimentAnalysis2(text):
# 	analyzer = SentimentIntensityAnalyzer()
# 	vs = analyzer.polarity_scores(text)
# 	polarity = vs['compound']
# 	print('vaderSen polarity = %f' % (polarity))
# 	return polarity

def searchTwitters(api, geocode, db):
	max_id = sys.maxsize

	while True:
		try:
			tweets = api.search(lang='en', geocode=geocode, max_id=(max_id - 1), count=100)

			i = 0
			
			if tweets:
				# Get the id of the last tweet as the max_id of next search
				max_id = tweets[len(tweets) - 1]._json['id']
				# print ('max id = %d' % (max_id))

				for myTweet in tweets:
					tweet = myTweet._json

					if tweet['coordinates'] or tweet['geo'] or tweet['place']:
						# print(tweet['id_str'])
						text = tweet['text']
						# print(text)

						polarity = sentimentAnalysis(text)
						# polarity2 = sentimentAnalysis2(text)
						tweet['sentiment'] =  float('%.6f' % polarity)

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

	searchTwitters(api, geocode, db)

if __name__ == '__main__':
	main()