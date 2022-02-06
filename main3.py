from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

student = {}

class Student(BaseModel) :
    id : str
    name : str
    age : Optional[int]

@app.post("/new/")
def new_student(student: Student) :
    student[student.id] = student
    return student

@app.get("/all")
def get_all_student():
    return student

@app.get("/find/{student_id}")
def find_by_id(student_id: str) :
    return student[student_id]