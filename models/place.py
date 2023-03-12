#!/usr/bin/python3
"""
Place Class from Models Module
"""

from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import DateTime, Table, MetaData, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import os


class Place(BaseModel, Base):
    """Place class handles all application places"""

    if os.getenv('HBNB_TYPE_STORAGE', 'fs') == 'db':
        metadata = Base.metadata
        __tablename__ = 'places'
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float)
        longitude = Column(Float)
        amenity_ids = ['', '']
        amenities = relationship('Amenity',
                                 secondary='place_amenity',
                                 viewonly=False)
        reviews = relationship('Review',
                               cascade="all, delete", backref='place')
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

    def __init__(self, *args, **kwargs):
        """instantiates a new place"""
        super().__init__(self, *args, **kwargs)


class PlaceAmenity(Base):
    """ place amenity """

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        metadata = Base.metadata
        __tablename__ = "place_amenity"
        place_id = Column(String(60), ForeignKey('places.id'),
                          primary_key=True, nullable=False)
        amenity_id = Column('amenity_id', String(60),
                            ForeignKey('amenities.id'),
                            primary_key=True, nullable=False)
