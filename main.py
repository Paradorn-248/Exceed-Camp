from fastapi import FastAPI
from typing import Optional #parameterเพิ่มเติม ไม่จำเปนต้องใส่ก้ได้ โดยถ้าไม่ใส่จะให้ค่าเริ่มต้นเปนตัวหลัง=
from pydantic import BaseModel

app = FastAPI()

class Model(BaseModel) :
    name : str
    price : float
    discount : Optional[float] = 0


@app.get("/")
def root():
    return {"Hello":"Exceed"}

@app.post("/")
def root_post():
    name = "POST"
    return {"Hello":f"Exceed from {name}"}

@app.put("/")
def root_put():
    name = "PUT"
    return {"Hello":f"Exceed from {name}"}

@app.delete("/")
def root_delete():
    name = "DELETE"
    return {"Hello":f"Exceed from {name}"}

@app.get("/items/{item_id}")
def get_item(item_id : int,q : Optional[str]=None ):
    return {"Hello":item_id,"From get":q}

@app.post("/items/{item_id}")
def post_item(item_id : int,q : Optional[str]=None ):
    return {"Hello":item_id,"From post":q}

@app.put("/items/{item_id}")
def put_item(item_id : int,q : Optional[str]=None ):
    return {"Hello":item_id,"From put":q}

@app.delete("/items/{item_id}")
def delete_item(item_id : int,q : Optional[str]=None ):
    return {"Hello":item_id,"From delete":q}

@app.get("/models/{model_id}")
def get_item(model_id : int,model:Model):
    return {"Hello":model_id,
            "Name":model.name,
            "Price":model.price,
            "discount":model.discount}