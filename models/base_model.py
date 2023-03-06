#!/usr/bin/python3
import uuid
from datetime import datetime
"""This is the BaseModel of the AirBnB console project"""


class BaseModel:
    """This defines a BaseModel class"""

    id = ""
    created_at = ""
    updated_at = ""

    def __init__(self):
        """This initializes a BaseModel instance on create/update"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Returns a human readable representation of the class"""
        # [<class name>] (<self.id>) <self.__dict__>
        return f"{self.__class__} {self.id} {self.__dict__}"
    
    def save(self):
        """updates the public instance attribute 'updated_at' with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of the instance"""
        return self.__dict__
