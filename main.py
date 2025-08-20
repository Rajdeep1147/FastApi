from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {"data":{ "Hello, World!"}}

@app.get('/about')
def about():
    return {"data": {"This is a simple FastAPI application."}}
