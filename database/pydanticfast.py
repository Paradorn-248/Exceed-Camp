from http.client import HTTPException
from pymongo import MongoClient

from fastapi import FastAPI,HTTPException
from typing import Optional #parameterเพิ่มเติม ไม่จำเปนต้องใส่ก้ได้ โดยถ้าไม่ใส่จะให้ค่าเริ่มต้นเปนตัวหลัง=
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder

app = FastAPI()

client = MongoClient('mongodb://localhost', 27018)

db = client["Erk_database"]
menu_collection = db["menu"]

class Menu(BaseModel) :
    name : str
    price : int 
    amount : int

@app.post("/new_menu")
def add_menu(menu:Menu) :
    m = jsonable_encoder(menu)
    print(m)
    menu_collection.insert_one(m)
    return {"result" : "done"}

@app.get("/menu/{name}")
def get_menu(name:str):
    result = menu_collection.find_one({"name":name},{"_id":0})
    print(result)
    if result != None :
        return {"result" : result}
    else : 
        raise HTTPException(404,f"Couldn't find menu with name: {name}")


