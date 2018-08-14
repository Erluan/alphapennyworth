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

ai_intents = db.ai_intents

# Simple Collection 'Select' command
cursor = ai_intents.find({})
for document in cursor:
	print(document)