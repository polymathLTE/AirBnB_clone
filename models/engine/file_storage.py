#!/usr/bin/python3
import json
from os import path as pt
"""serializes instances to a JSON file and deserializes JSON file to instances for storage/recovery"""


class FileStorage:
    """Defines the Filestorage class"""
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """initializes the FileStorage instance"""

    def new(self, obj):
        """sets in '__objects the obj with key '<obj class name>.id"""
        tmp_obj = {}
        tmp_obj[f"{type(obj).__name__}.{obj.get('id')}"] = obj
        self.__objects.update(tmp_obj)

    def all(self):
        """returns the dictionary '__objects"""
        return __objects
    
    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(__file_path, 'w', encoding='utf-8') as doc:
            doc.write(json.dumps(__objects))

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file (__file_path) exists;
        otherwise, do nothing. If the file doesn’t exist, no exception should be raised)
        """
        # checks if file exists
        if pt.exists(__file_path):
            with open(__file_path, 'r', encoding='utf-8') as doc:
                __objects = json.loads(doc.read())

