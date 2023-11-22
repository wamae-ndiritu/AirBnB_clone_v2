#!/usr/bin/python3
"""This module defines a class User"""
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.place import Place
from models.review import Review

<<<<<<< HEAD
class User(BaseModel, Base):
    """This class defines a user by various 
    Attributes:
        email: email address
        password: password for your login
        first_name: first name
        last_name: last name
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship("Place", cascade='all, delete, delete-orphan', backref="user")
    reviews = relationship("Review", cascade='all, delete, delete-orphan', backref="user")
=======

class User(BaseModel):
    """This class defines a user by various attributes"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''
>>>>>>> parent of 46146d0... update user to be in dbs
