from typing import List
from pydantic import BaseModel

# Item 模型
class ItemBase(BaseModel):
    title: str
    description: str = None

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int
    owner_id: int
    class Config:
        orm_mode = True

# User 模型
class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    psaasword: str

class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []
    class Config:
        orm_mode = True