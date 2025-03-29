from fastapi import FastAPI
from fastapi import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating:Optional[float] = None

@app.get("/")
def root():
    return {"message": "Welcome to FastAPI!"}

@app.get("/post")
def get_posts():
    return {"data": "List of posts"}

@app.post("/createposts")
def create_post(new_posts: Post):
    print(new_posts)
    print(new_posts.dict())
    return {"data": new_posts}