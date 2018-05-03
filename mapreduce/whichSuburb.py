# coding=utf-8
"""
get the coordinates from twitter data
"""
import json


def getCoordinate(doc):
    # coordinate = [144.96138889, -37.82055556]
    # global coordinate
    try:
        if 'geo' in doc and doc['geo'] is not None:
            if 'coordinates' in doc['geo'] and doc['geo']['coordinates'] is not None:
                coordinate = doc['geo']['coordinates']
                return coordinate

    except:
        print("Error: no doc found")

def getSentiment(doc):
    try:
        if 'sentiment' in doc and doc['sentiment'] is not None:
            sentiment = doc['sentiment']
            return sentiment
    except:
        print("Error: no doc found")


with open('jsonExample.json') as f:
    dict_twitter = json.load(f)
    # print(type(dict_twitter))
    print(getCoordinate(dict_twitter))
    print(getSentiment(dict_twitter))

