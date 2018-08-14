from pymongo import MongoClient
from bson.objectid import ObjectId # Needed to be imported to "find" a Document by ObjectID
import datetime
import numpy
import urllib
import sys
import pandas as pd
import pymongo
import json
import os
import nltk
from nltk.tokenize import RegexpTokenizer

# Creating the connection
client = pymongo.MongoClient("mongodb+srv://requester:" + urllib.parse.quote("aba@#H2PQ") + "@alphapennyworthchatbot-xapjt.mongodb.net/test?retryWrites=true")
db = client.alphapennyworthchatbot

#Creating the Collection (It's like the folder the Documents will be stored) = client.clustertest.test (connection.db.collectionname)
# collection = db.test

# Simple Collection 'Select' command
# cursor = collection.find({})
# for document in cursor:
# 	print(document)

# Creating a new Collection
ai_intents = db.ai_intents

ai_intents.insert({
	"name" : "greeting",
	"patterns" : [ "Hi", "How are you", "Is anyone there?", "Hello", "Good day" ],
	"responses" : [ "Hi, thanks for visiting", "Hi there, how can I help?", "Hello", "Hey" ],
	"contextSet" : ""
})