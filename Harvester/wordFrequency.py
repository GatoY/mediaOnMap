import couchdb
import collections
import re

def connectDB(db_server, db_name):
	server = couchdb.Server(db_server)
	db = server[db_name]
	return db

def get_words(db):
	pos_words_box = []
	neg_words_box = []

	for id in db:
		doc = db.get(id)

		text = doc.get('text')
		if not text:
			continue

		# if ('km/h' in text) and  ('hPa' in text):
		# 	db.delete(doc)
		# 	continue

		text = text.lower()
		text = re.sub("\"|,|\.|\!", "", text)

		if doc['sentiment'] > 0:
			pos_words_box.extend(text.strip().split())
		if doc['sentiment'] < 0:
			neg_words_box.extend(text.strip().split())

	return collections.Counter(pos_words_box), collections.Counter(neg_words_box)

def wirte_to_file(pos_common, neg_common):
	with open('words_comm.txt', 'w+') as file:
		file.write('Postitive words:\n')
		for pos_word in pos_common:
			isInNeg = False
			for neg_word in neg_common:
				if pos_word[0] == neg_word[0]:
					isInNeg = True
					break
			if not isInNeg:
				file.write('%s, %d\n' % (pos_word[0], pos_word[1]))

		file.write('\nNegative words:\n')
		for neg_word in neg_common:
			isInPos = False
			for pos_word in pos_common:
				if neg_word[0] == pos_word[0]:
					isInPos = True
					break
			if not isInPos:
				file.write('%s, %d\n' % (neg_word[0], neg_word[1]))

def main():
	db_server = 'http://localhost:5984/'
	db_name = 'twitter'
	db = connectDB(db_server, db_name)

	pos_words_box, neg_words_box = get_words(db)

	pos_common = pos_words_box.most_common(200)
	neg_common = neg_words_box.most_common(200)

	wirte_to_file(pos_common, neg_common)

if __name__ == '__main__':
	main()