import pymongo
from pymongo import MongoClient
import json
from spellchecker import SpellChecker
import re

client = pymongo.MongoClient("")

db = client['Matrimonial']
collection = db['Matrimonial_data']

def insert_data(data):
	try:
		collection.insert_one(data)
		return True
	except Exception as e:
		print(e)
		return False

def check_id_duplicate(data):
	query = {"Ad_content": {"$eq": data['Ad_content']},'Categorised_under':{"$eq": data['Categorised_under']},
			'Newspaper_name':{"$eq": data['Newspaper_name']},'Url':{"$eq": data['Url']}}
	count = get_document_count(query)
	if count == 0:
		return False
	return True

def get_document_count(filters):
	query = {}
	if filters:
		query.update(filters)
	collection_count = collection.count_documents(query)
	return collection_count

def query():
	data_ob = collection.find({})
	return data_ob

def insert_data_check(data):
	status = check_id_duplicate(data)
	if status == False:
		if(insert_data(data)):
			print("Success - Inserted the data! ",data['Ad_content'])
		else:
			print("Insertion failed!")
	else:
		print("Duplicate Data")

def query_db(word):
	word = ".* "+word+" .*"
	temp = list(collection.find({'Ad_content_lower': {'$regex': word}}, {'_id': 0}))
	return temp

def get_db():
	temp = list(collection.find({}, {'_id': 0}))
	return temp

def query_words(words):
	words = [i.strip().lower() for i in words.split(',') if len(i.strip())>0]
	query = []
	for word in words:
		word = ".* "+word+" .*"
		query.append({'Ad_content_lower': {'$regex': word}})
	temp = list(collection.find({'$or':query}, {'_id': 0}))
	return temp

def plot_graph(X,Y):
	import numpy as np
	import matplotlib.pyplot as plt
	plt.plot(X, Y)
	plt.xticks(rotation='vertical')
	plt.show()

def parse_Data(datas):
	X={}
	for data in datas:
		# key = data['Date'].strftime("%Y-%m-%d")
		# key = data['Date'].strftime("%Y-%m")
		key = data['Date'].strftime("%Y")
		if key=='1970':
			continue
		if key not in X.keys():
			X[key]=0;
		X[key]+=1
	return X

if __name__=="__main__":
	# text = str(input("Enter query: ")).lower()
	text = "beautiful,bful,white,fair,wheatish,yellow,slim"
	datas = query_words(text)
	
	# get all the data in the db and map it
	all_data = get_db()
	X =parse_Data(datas)
	tX =parse_Data(all_data)
	for key in X.keys():
		X[key]=tX[key]/X[key]

	x = sorted(X.keys())
	y = [X[i] for i in x]
	plot_graph(x,y)


# db.Newspaper_Data.updateMany({},[{'$addFields': {'Date': {'$dateFromString': {'dateString': '$Published_on'}}}}])
# db.Newspaper_Data.updateMany({},[{'$addFields': {'Split_Date': {"$split": ["$Published_on", " " ]}}}}}])

# db.Matrimonial_data.updateMany({},[{'$addFields': {'Split_Date':{'$split': ['$Published_on', ' ' ]}}}])
# db.Matrimonial_data.updateMany({},[{'$set': { 'Published_on': {$replaceOne: { input: "$Published_on", find: "th ", replacement: " " }}}}])