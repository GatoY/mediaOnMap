# coding=utf-8
import json

def r(x):
    for i in x.keys():
        print(i)

with open('data6832721887976589782.json') as f:
    text = json.load(f)
    r(text['features'])

