from enum import unique
from .db import Base
from sqlalchemy import Column, Integer, String
from tabulate import tabulate

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(200), nullable=False)
    email = Column(String(100), nullable=False, unique=True)

    def __repr__(self):
        return f"<User {self.id}>"
    
    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password,
            'email': self.email
        }
    
    def to_list(self):
        return [
            self.id,
            self.username,
            self.password,
            self.email
        ]

    @classmethod
    def pretty_print(cls, data):
        data = [item.to_list() for item in data]
        print(tabulate(data, headers=cls.__table__.columns.keys(), tablefmt='pretty'))
