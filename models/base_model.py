#!/usr/bin/python3
"""
Module: base.py
"""
import models
import uuid
from datetime import datetime


class BaseModel():
    """
    Base class which defines all common
    attributes/methods for other classes
    """
class BaseModel():
    """
    Base class which defines all common
    attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        Instantiates an object with its
        attributes
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' and 'created_at' in kwargs:
                    value = datetime.fromisoformat(value)
                if key == 'updated_at' and 'updated_at' in kwargs:
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
            return

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
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        my_dict = {**self.__dict__}
        if '__class__' not in my_dict:
            my_dict['__class__'] = self.__class__.__name__
        if 'created_at' in my_dict:
            my_dict['created_at'] = my_dict['created_at'].isoformat()
        if 'updated_at' in my_dict:
            my_dict['updated_at'] = my_dict['updated_at'].isoformat()

        return my_dict
