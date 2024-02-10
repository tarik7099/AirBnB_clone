#!/usr/bin/python3
"""Module for the FileStorage class"""
import datetime
import json
import os


class FileStorage:

    """A Class for serializtion and deserialization of the base classes"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return -> __objects dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """Set new objct in __objects dict"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialzes the __objects to JSON file"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as fl:
            dr = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(dr, fl)

    def classes(self):
        """Return -> dict of valid classes and references"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review}
        return classes

    def reload(self):
        """Deserializes the JSON file into __objects"""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as fl:
            objct_dct = json.load(f)
            objct_dct = {k: self.classes()[v["__class__"]](**v)
                        for k, v in objct_dct.items()}
            FileStorage.__objects = objct_dct

    def attributes(self):
        """Return -> valid attributes and  types for class name"""
        attributes = {
            "BaseModel":
                     {"id": str,
                      "created_at": datetime.datetime,
                      "updated_at": datetime.datetime},
            "User":
                     {"email": str,
                      "password": str,
                      "first_name": str,
                      "last_name": str},
            "State":
                     {"name": str},
            "City":
                     {"state_id": str,
                      "name": str},
            "Amenity":
                     {"name": str},
            "Place":
                     {"city_id": str,
                      "user_id": str,
                      "name": str,
                      "description": str,
                      "number_rooms": int,
                      "number_bathrooms": int,
                      "max_guest": int,
                      "price_by_night": int,
                      "latitude": float,
                      "longitude": float,
                      "amenity_ids": list},
            "Review":
            {"place_id": str,
                         "user_id": str,
                         "text": str}
        }
        return attributes
