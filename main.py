from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn # Corrected import statement

app = FastAPI()

@app.get('/blog')
def index(limit= 10,published: bool=True ,short: Optional[str]= None):
    if published:
        return {"data": f'{limit} published blogs from the database with limit {limit}'}
    else:   
        return {"data":f'All blogs from the database'}


@app.get('/about')
def about():
    return {"data": {"This is a simple FastAPI application."}}


@app.get('/name/{name}')
def parameter(name :str):
    return {"data": {"Hello, " + name + "!"}}

@app.get("/blog/{id}/comments")
def comment(id: int):
    return {"data": ["1", "2", "3"]}


@app.get('/raj/{id}')
def raj(id: int):
    return {"data": {"id": id, "name": "Raj"}}


class Blog(BaseModel):
    title: str
    body: str
    published_at: Optional[bool] = True


@app.post('/blog')
def create_blog(request: Blog):
    return {"message": f"Blog is created with title `{request.title}` and body `{request.body}`. Published: {request.published_at}"}



# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=9000)  # Corrected the host and port 


class User(BaseModel):
    username: str
    password: str
    email: Optional[str] = None
@app.post('/user')
def create_user(user: User):
    return {"message": f"User created with username `{user.username}` and email `{user.email}`."}