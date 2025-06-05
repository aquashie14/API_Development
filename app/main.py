from fastapi import FastAPI, Response,status, HTTPException, Depends
from fastapi import Body
from typing import Optional, List
from random import randrange
import psycopg2
import os
from dotenv import load_dotenv
from psycopg2.extras import RealDictCursor
import time 
from . import model, schema,utilis
from .database import engine, get_db
from sqlalchemy.orm import Session
from .routers import auth, posts, users

# Load environment variables from .env file
load_dotenv()
DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')



model.Base.metadata.create_all(bind=engine)

app = FastAPI()


    
while True:
    try:
        conn= psycopg2.connect(host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASSWORD, cursor_factory=RealDictCursor)
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

app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)

@app.get("/")
def root():   
    return {"message": "Welcome to FastAPI!"}



