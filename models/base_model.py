#!/usr/bin/python3
"""
Module: base.py
"""
import models
import uuid
from datetime import datetime


class BaseModel:
    """
    Base class which defines all common
    attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        instantiates an object with its
        attributes
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

            models.storage.new(self)

    def __str__(self):
        """
        Returns the string representation
        of the instance
        """
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def save(self):
        """
        updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        dict_repr = self.__dict__.copy()
        dict_repr['__class__'] = type(self).__name__
        dict_repr['created_at'] = self.created_at.isoformat()
        dict_repr['updated_at'] = self.updated_at.isoformat()
        return dict_repr


# Update models/__init__.py to create a unique FileStorage instance for your application
# Update models/base_model.py to link your BaseModel to FileStorage by using the variable storage
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
