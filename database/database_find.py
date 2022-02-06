from traceback import print_tb
from pymongo import MongoClient

client = MongoClient('mongodb://localhost', 27018)

db = client["Erk_database"] #ใส่ชื่อdatabase
user_collection = db["user"] #ใส่ชื่อcollection
menu_collection = db['menu']

result_one = menu_collection.find_one() #show first
print(result_one)

r = menu_collection.find()
for fruit in r:
    print(fruit)

r2 = menu_collection.find({},{"_id":0,"name":1,"price":1}) #0ไม่เอา1เอา
for fruit in r2:
    print(fruit)

query = {'name':"Orange","price" :40}
result = menu_collection.find(query,{"_id":0,"name":1})
# print(result)
for i in result :
    print(i)
result = menu_collection.find_one(query)
print(result)
print('--------------------')
#ขอผลไม้ที่มีpriceไม่เกิน40
lt = menu_collection.find({'price':{'$lt':40}})
for i in lt:
    print(i)
#ขอผลไม้ที่มีpriceน้อยกว่า40 หรือมากกว่า80
res = menu_collection.find({'$or':{'price':{'$lt':40}},{'price':{'$gt':80}}})
for i in res:
    print(i)