#!/usr/bin/python3

from models.base_model import BaseModel
from models.user import User
from models.place import Place
"""the Review class defines attributes for review left by users"""


class Review(BaseModel):
    """defines the Review class"""
    place_id = ""
    user_id = ""
    text = ""
