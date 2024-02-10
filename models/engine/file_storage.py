#!/usr/bin/python3
"""
Module: file_storage.py

Defines a `FileStorage` class.
"""
import os
import json
import datetime
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    CLASSES = {
        'BaseModel': BaseModel,
        'User': User,
        # Add other classes here
    }

    def __init__(self, file_path="file.json"):
        self.__file_path = os.path.join(os.getcwd(), file_path)
        self.__objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        serialized_objs = {}
        for key, obj in self.__objects.items():
            serialized_objs[key] = obj.to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(serialized_objs, file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, "r") as file:
                serialized_objs = json.load(file)
                for key, value in serialized_objs.items():
                    class_name, obj_id = key.split('.')
                    class_ = self.CLASSES.get(class_name)
                    if class_:
                        self.__objects[key] = class_(**value)
        except FileNotFoundError:
            # Handle file not found error
            pass
        except json.JSONDecodeError as e:
            # Handle JSON decoding error
            print(f"Error decoding JSON: {e}")

    def attributes(self):
        """Returns the valid attributes and their types for classname."""
        attributes = {
            "BaseModel": {"id": str, "created_at": datetime.datetime, "updated_at": datetime.datetime},
            "User": {"email": str, "password": str, "first_name": str, "last_name": str},
            # Add attributes for other classes here
        }
        return attributes

