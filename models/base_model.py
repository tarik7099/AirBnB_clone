#!/usr/bin/python3
"""Module for the Base class
"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:

    """Class for the base model of object"""

    def __init__(self, *args, **kwargs):
        """Initialization of the Base instance

        Args:
            - *args: A list of args
            - **kwargs: A dict of key-values ars
        """

        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Returns -> human-readable str representation
        of  instance"""

        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Update updated_at attribute
        with current datetime"""

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Return  -> dictionary representation of instance"""

        mdct = self.__dict__.copy()
        mdct["__class__"] = type(self).__name__
        mdct["created_at"] = mdct["created_at"].isoformat()
        mdct["updated_at"] = mdct["updated_at"].isoformat()
        return mdct
