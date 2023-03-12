#!/usr/bin/python3
"""
City Class from Models Module
"""

from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Table
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import os


class City(BaseModel, Base):
    """City class handles all application cities"""

    if os.getenv('HBNB_TYPE_STORAGE', 'fs') == 'db':
        __tablename__ = 'cities'
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship('Place', cascade="all, delete", backref="cities")
    else:
        name = ""
        state_id = ""

    def __init__(self, *args, **kwargs):
        """instantiates a new city"""
        super().__init__(self, *args, **kwargs)
