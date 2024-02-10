#!/usr/bin/python3
""" Module for FileStorage class """

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

class FileStorage:
    """ Class for serializing and deserializing instances to a JSON file """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """ Serializes __objects to the JSON file (__file_path) """
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(new_dict, f)

    def reload(self):
        """ Deserializes the JSON file to __objects """
        try:
            with open(self.__file_path, "r") as f:
                json_dict = json.load(f)
                for key, value in json_dict.items():
                    class_name, obj_id = key.split('.')
                    class_dict = eval(class_name).__dict__
                    for k, v in value.items():
                        if k in class_dict:
                            value[k] = class_dict[k](**v)
                        else:
                            value[k] = v
                    self.__objects[key] = eval(class_name)(**value)
        except FileNotFoundError:
            pass
