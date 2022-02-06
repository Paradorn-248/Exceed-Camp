from pymongo import MongoClient

from fastapi import FastAPI
from typing import Optional #parameterเพิ่มเติม ไม่จำเปนต้องใส่ก้ได้ โดยถ้าไม่ใส่จะให้ค่าเริ่มต้นเปนตัวหลัง=
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder 

app = FastAPI()

client = MongoClient('mongodb://localhost', 27018)
db = client["Erk_database"] #ใส่ชื่อdatabase
user_collection = db["user"] #ใส่ชื่อcollection
menu_collection = db['menu']

@app.get("/fruit/all")
def get_all_fruit():
    r = menu_collection.find({},{"_id":0,"name":1})
    my_result = list()
    for i in r:
        # print(i)
        my_result.append(i)
    return {'result':my_result}

@app.post("/fruit/add/{name}/{price}")
def add_new_fruit(name:str,price:int):
    new_fruit = {
        'name':name,
        'price':price
    }
    menu_collection.insert_one(new_fruit)
    return {'result':'done'}

@app.delete("/fruit/del/{name}")
def remove_one_fruit(name:str) :
    query = {'name':name}
    menu_collection.delete_one(query)
    return {'result':'done'}

@app.put("/fruit/update/{name}/{new_price}")
def update_one_fruit(name:str,new_price:int) :
    query = {'name':name}
    new_value = {'$set':{'price':new_price}}
    menu_collection.update_one(query,new_value)
    return {'result':'done'}
