import os
import json
import datetime
from models.base_model import BaseModel
from models.user import User

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    CLASSES = {
        'BaseModel': BaseModel,
        'User': User
    }

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
                    if class_name in self.CLASSES:
                        class_ = self.CLASSES[class_name]
                        self.__objects[key] = class_(**value)
        except (FileNotFoundError, json.JSONDecodeError):
            pass

    def attributes(self):
        """Returns the valid attributes and their types for classname."""
        attributes = {
            "BaseModel": {
                "id": str,
                "created_at": datetime.datetime,
                "updated_at": datetime.datetime
            },
            "User": {
                "email": str,
                "password": str,
                "first_name": str,
                "last_name": str
            },
            # ... (other classes)
        }
        return attributes

