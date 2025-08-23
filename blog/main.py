from fastapi import FastAPI
from typing import List
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from . import model
from .database import engine, SessionLocal
import uvicorn

model.Base.metadata.create_all(bind=engine)
app = FastAPI()

@app.get("/a")
def check_db_connected():
    return {"message": "DB connected"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
  