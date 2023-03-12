#!/usr/bin/python3


from models.base_model import BaseModel
"""A User defines a individual whose info is being managed"""


class User(BaseModel):
    """this defines a user class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
