from fastapi import FastAPI, Response,status, HTTPException
from fastapi import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange
import psycopg2
import os
from dotenv import load_dotenv
from psycopg2.extras import RealDictCursor
import time

# Load environment variables from .env file
load_dotenv()
password = os.getenv('DB_PASSWORD')

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    
while True:
    try:
        conn= psycopg2.connect(host='localhost', database='fastapi', user='postgres', password=password, cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was successful")
        break
    except Exception as error:
        print("Connection to database failed")
        print("Error:", error)
        time.sleep(2)


my_posts =[{"title": "title of post 1", "content": "content of post 1", "id":1},{"title": "title of post 2", "content": "content of post 2", "id":2}]

def find_post(id):
    for p in my_posts:
        if p['id'] == id:
            return p

def find_index(id):
    for i,p in enumerate(my_posts):
        if p["id"] == id:
            return i

@app.get("/")
def root():
    return {"message": "Welcome to FastAPI!"}

@app.get("/posts")
def get_posts():
    cursor.execute("""SELECT * FROM posts""")
    posts = cursor.fetchall()
    return {"data": posts}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 1000000)
    my_posts.append(post_dict)
    return {"data": my_posts}

@app.get("/posts/{id}")
def get_post(id: int):
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} was not found")
    return {"post_details": post}

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    index = find_index(id)
    if index==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} does not exist")
    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/{id}")
def update_post(id: int, post:Post):
    print(f"id: {id}")
    print(f"post: {post}")
    
    index = find_index(id)
    print(f"index: {index}")

    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} does not exist")
    post_dict = post.dict()
    post_dict['id'] = id
    my_posts[index] = post_dict
    return{"data": "post_dict"}