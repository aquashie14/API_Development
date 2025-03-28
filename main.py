from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to FastAPI!"}

@app.get("/post")
def get_posts():
    return {"data": "List of posts"}

@app.post("/createposts")
def create_post():
    return {"message": "Post created successfully"}