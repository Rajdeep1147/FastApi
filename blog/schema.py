from pydantic import BaseModel

class Blog(BaseModel):
    title: str
    body: str
    user_id: int

class User(BaseModel):
    name: str
    email: str
    password: str


class CreateUser(BaseModel):
    name: str
    email: str
    password: str

class BlogBase(BaseModel):
    title: str
    body: str = "This is Test Body"
    user_id: int


class BlogCreate(BlogBase):
    pass

class Blog(BlogBase):
    id: int
    class Config:
        from_attributes = True

class User(BaseModel):
    id : int

    class Config:
        form_attribute = True