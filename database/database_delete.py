from pymongo import MongoClient

client = MongoClient('mongodb://localhost', 27018)

db = client["Erk_database"] #ใส่ชื่อdatabase
user_collection = db["user"] #ใส่ชื่อcollection
menu_collection = db['menu']

query = {'name':'Chicken'}
menu_collection.delete_one(query)

