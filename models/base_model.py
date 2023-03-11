#!/usr/bin/python3
import uuid
from datetime import datetime
import models
"""This is the BaseModel of the AirBnB console project"""


class BaseModel:
    """This defines a BaseModel class"""

    id = ""
    created_at = ""
    updated_at = ""

    def __init__(self, *args, **kwargs):
        """This initializes a BaseModel instance on create/update"""
        tm_format = '%Y-%m-%dT%H:%M:%S.%f'
        if len(kwargs) != 0:
            kwargs['created_at'] = datetime.strptime(kwargs.get('created_at'), tm_format)
            kwargs['updated_at'] = datetime.strptime(kwargs.get('updated_at'), tm_format)
            for k, v in kwargs.items():
                if k != "__class__":
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Returns a human readable representation of the class"""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"
    
    def save(self):
        """updates the public instance attribute 'updated_at' with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of the instance"""
        cls_dict = dict(self.__dict__)
        cls_dict.update({'__class__':self.__class__.__name__})
        cls_dict['created_at'] = datetime.isoformat(cls_dict.get('created_at'))
        cls_dict['updated_at'] = datetime.isoformat(cls_dict.get('updated_at'))
        return cls_dict
