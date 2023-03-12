#!/usr/bin/python3

from models.base_model import BaseModel
from models.user import User
from models.place import Place

class Review(BaseModel, Place, User):
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self):
        place_id = Place.id
        user_id = User.id
