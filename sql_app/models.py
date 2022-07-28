from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .database import Base


# 定义User类
class User(Base):
    __tablename__: str = 'users'  # 定义表名
    # 定义属性
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True)
    hashed_password = Column(String(255))
    is_active = Column(Boolean, default=True)
    items = relationship('Item', back_populates='owner')  # 关联Item表

# 定义Item类
class Item(Base):
    __tablename__: str = 'Item'  # 定义表名
    # 定义属性
    id = Column(Interger, primary_key=True, index=True)
    title = Column(String(255), index=True)
    description = Column(String(255), index=True)
    owner_id = Column(Integer, ForeignKey('users.id'))
    owner = relationship('User', back_populates='items')  # 关联User表
