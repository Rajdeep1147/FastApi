from .model import Blog
from sqlalchemy.orm import Session
from .schema import BlogCreate
from fastapi import HTTPException

def create_blog(db:Session,data:BlogCreate):
    new_blog = Blog(**data.model_dump())
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def get_all(db:Session):
    blogs = db.query(Blog).all()
    return blogs

def get_blog(db:Session,blog_id:int):
    blog = db.query(Blog).filter(Blog.id == blog_id).first()
    return blog

def update_blog(db: Session, data: BlogCreate, blog_id: int):
    blog_query = db.query(Blog).filter(Blog.id == blog_id).first()
    if blog_query:
        # Update the blog fields
        for key, value in data.model_dump().items():
            setattr(blog_query, key, value)
        db.commit()
        db.refresh(blog_query)
        return blog_query
    else:
        raise HTTPException(status_code=404, detail="Blog not found")


def delete_blog(db: Session, blog_id: int):
    blog_query = db.query(Blog).filter(Blog.id == blog_id).first()
    if not blog_query:
        raise HTTPException(status_code=404, detail="Blog not found")
    db.delete(blog_query)
    db.commit()
    return {"message": "Blog deleted successfully"}