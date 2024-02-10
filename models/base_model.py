#!/usr/bin/python3
"""
Module: base.py
"""
import models
import uuid
from datetime import datetime

from models.__init__ import storage

class BaseModel:
    def __init__(self, *args, **kwargs):
        """Initialize BaseModel instance"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            self.created_at = datetime.strptime(self.created_at, "%Y-%m-%dT%H:%M:%S.%f")
            self.updated_at = datetime.strptime(self.updated_at, "%Y-%m-%dT%H:%M:%S.%f")
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)  # Add this line to save the new instance
            storage.save()  # Add this line to ensure the new instance is saved immediately

    def save(self):
        """Update updated_at attribute and save to storage"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Return dictionary representation of BaseModel"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = obj_dict['created_at'].isoformat()
        obj_dict['updated_at'] = obj_dict['updated_at'].isoformat()
        return obj_dict