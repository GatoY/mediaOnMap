#!/usr/bin/env python
# -*- coding: utf-8 -*-
import couchdb
import collections
import re
import json

# Connect to db
def connectDB(db_server, db_name):
	server = couchdb.Server(db_server)
	db = server[db_name]
	print('Connect to db')
	return db

# Get hot topics
def get_topics(db):
	topic_box = []
	pos_topic_box = []
	neg_topic_box = []

	for id in db:
		doc = db.get(id)

		text = doc.get('text')
		if not text:
			continue

		text = re.sub("\"|,|\.|\!", "", text)

		splitTexts = text.strip().split()

		for splitText in splitTexts:
			if splitText.startswith('#'):
				topic_box.append(splitText)
				if doc['sentiment'] > 0:
					pos_topic_box.append(splitText)
				if doc['sentiment'] < 0:
					neg_topic_box.append(splitText)

	return collections.Counter(topic_box), collections.Counter(pos_topic_box), collections.Counter(neg_topic_box)

# Write to file
def wirte_to_file(common, pos_common, neg_common):
	all_list = []
	pos_list = []
	neg_list = []

	for topic in common:
		dict = {}
		dict['topic'] = topic[0].encode('utf-8').replace('#', '')
		dict['number'] = topic[1]
		all_list.append(dict)

	for topic in pos_common:
		dict = {}
		dict['topic'] = topic[0].encode('utf-8').replace('#', '')
		dict['number'] = topic[1]
		pos_list.append(dict)

	for topic in neg_common:
		dict = {}
		dict['topic'] = topic[0].encode('utf-8').replace('#', '')
		dict['number'] = topic[1]
		neg_list.append(dict)

	topic_list = {}

	topic_list['all_topics'] = all_list
	topic_list['pos_topics'] = pos_list
	topic_list['neg_topics'] = neg_list

	topics_json = json.dumps(topic_list)

	with open('hotTopics.json', 'w+') as file:
		file.write(topics_json)

	# with open('hotTopics.txt', 'w+') as file:
	# 	file.write('All topics:\n')
	# 	for topic in common:
	# 		file.write('%s, %d\n' % (topic[0].encode('utf-8'), topic[1]))

	# 	file.write('\nPostitive topics:\n')
	# 	for topic in pos_common:
	# 		file.write('%s, %d\n' % (topic[0].encode('utf-8'), topic[1]))

	# 	file.write('\nNegative topics:\n')
	# 	for topic in neg_common:
	# 		file.write('%s, %d\n' % (topic[0].encode('utf-8'), topic[1]))

def main():
	db_server = 'http://localhost:5984/'
	db_name = 'twitter'
	db = connectDB(db_server, db_name)

	topic_box, pos_topic_box, neg_topic_box = get_topics(db)

	common = topic_box.most_common(50)
	pos_common = pos_topic_box.most_common(50)
	neg_common = neg_topic_box.most_common(50)

	wirte_to_file(common, pos_common, neg_common)

if __name__ == '__main__':
	main()