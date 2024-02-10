import os
import json
import datetime
from models.base_model import BaseModel

class FileStorage:
    """ serializes instances to json """


    __file_path = "file.json"
    __objects = {}


    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects


    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + str(obj.id)
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
                    module_name = class_name.lower()  # Assuming module names are lowercase
                    class_ = globals()[class_name]  # Assuming classes are defined globally
                    self.__objects[key] = class_(**value)
        except FileNotFoundError:
            pass

