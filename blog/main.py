from fastapi import FastAPI, Depends,HTTPException
from . import service, model, schema
from typing import List
from sqlalchemy.orm import sessionmaker, Session
from .database import engine, SessionLocal, Base
from pydantic import BaseModel
import uvicorn

# Pydantic schemas

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
app = FastAPI()



@app.get("/a")
def check_db_connected():
    return {"message": "DB connected"}

@app.get("/blog/",response_model=List[schema.Blog])
def get_all_blogs(db: Session = Depends(get_db)):
    blogs = db.query(model.Blog).all()
    return blogs

@app.post("/blog/",response_model=schema.Blog)
def create_blog(request: schema.BlogCreate,db: Session = Depends(get_db)):
    return service.create_blog(db,request)

@app.get("/blog/{id}",response_model=schema.Blog)
def get_blog(id:int,db: Session = Depends(get_db)):
    blog = db.query(model.Blog).filter(model.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=404,detail="Blog not found")
    return blog

@app.put("/blog/{id}", response_model=schema.Blog)
def update_blog(id: int, request: schema.BlogCreate, db: Session = Depends(get_db)):
    return service.update_blog(db, request, id)


@app.delete("/blog/{id}")
def delete_blog(id: int, db: Session = Depends(get_db)):
    return service.delete_blog(db, id)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
