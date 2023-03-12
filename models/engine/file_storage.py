#!/usr/bin/python3
import json
from os import path as pt
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.city import City
"""serializes instances to a JSON file and deserializes JSON file to instances for storage/recovery"""


class FileStorage:
    """Defines the Filestorage class"""
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """initializes the FileStorage instance"""

    def new(self, obj):
        """sets in '__objects the obj with key '<obj class name>.id"""
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def all(self):
        """returns the dictionary '__objects"""
        return self.__objects
    
    def save(self):
        objtmp = self.__objects
        """serializes __objects to the JSON file (path: __file_path)"""
        obj_dict = {obj: objtmp[obj].to_dict() for obj in objtmp.keys()}
        with open(self.__file_path, 'w', encoding='utf-8') as doc:
            json.dump(obj_dict, doc)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file (__file_path) exists;
        otherwise, do nothing. If the file doesn’t exist, no exception should be raised)
        """
        # checks if file exists
        try:
            if pt.exists(self.__file_path):
                with open(self.__file_path, 'r', encoding='utf-8') as doc:
                    dictobj = json.load(doc)
                    for v in dictobj.values():
                        class_name = v['__class__']
                        del v['__class__']
                        self.new(eval(class_name)(**v))
                    
        except FileNotFoundError:
            return
