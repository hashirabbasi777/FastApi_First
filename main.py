from fastapi import FastAPI
from pydantic import BaseModel
from typing import List


app = FastAPI()


class Item(BaseModel):
    id: int
    name: str
    description: str = None

items_db: List[Item] = []


# Decorator to create a new item
@app.get("/")
def read_root():
    return {"message": "Welcome to the Item API"}

@app.get("/blogs")
def read_posts():
    return items_db

@app.post("/blogs")
def create_post(blogs : Item):
    items_db.append(blogs)
    return blogs


@app.put("/blogs/{id}")
def update_post(id: int, blogs: Item):
    for index, item in enumerate(items_db):
        if item.id == id:
            items_db[index] = blogs
            return blogs
    return {"error": "Item not found"}

@app.delete("/blogs/{id}") 
def delete_post(id: int):
    for index, item in enumerate(items_db):
        if item.id == id:
            deleted =  items_db.pop(index)
            return deleted
    return {"error": "Item not found"}
