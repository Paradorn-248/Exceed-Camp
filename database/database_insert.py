from pymongo import MongoClient

client = MongoClient('mongodb://localhost', 27018)

db = client["Erk_database"] #ใส่ชื่อdatabase
user_collection = db["user"] #ใส่ชื่อcollection
menu_collection = db['menu']

# เรียกดูชื่อ
mylist = client.list_database_names()
print(mylist)
print(db.list_collection_names())

# insert to db
# run แต่ละครั้งจะinsertเพิ่มตอลด
orange = {
    "name": "Orange",
    "price": 40,
}

banana = {
    "name": "Banana",
    'price': 20
}
apple = {
    "name": "Apple",
    'price': 30
}
grape = {
    "name": "Grape",
    'price': 90
}
# menu_collection.insert_one(orange)
fruit_list = [orange,banana,apple,grape]
x = menu_collection.insert_many(fruit_list)  # insertหลายdictพร้อมกัน
print(x.inserted_ids)

chicken = {
    'name' : 'Chicken'
}
menu_collection.insert_one(chicken)
