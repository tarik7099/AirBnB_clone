#!/usr/bin/python3
"""Module for Base class
"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:

    """Class for the basemodel of object """

    def __init__(self, *args, **kwargs):
        """Initialization of Base instance.

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
        """Returns the human-readable str representation
        of instance"""

        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Update updated_at attribute
        with current datetime"""

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Return dictionary representation of instance"""

        mdict = self.__dict__.copy()
        mdict["__class__"] = type(self).__name__
        mdict["created_at"] = my_dict["created_at"].isoformat()
        mdict["updated_at"] = my_dict["updated_at"].isoformat()
        return mdict
