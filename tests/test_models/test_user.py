#!/usr/bin/python3
"""Unittest module for User Class"""

import unittest
from datetime import datetime
import time
from models.user import User
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class TestUser(unittest.TestCase):

    """Tests Cases for the User class"""

    def setUp(self):
        """Sets up the test methods"""
        pass

    def tearDown(self):
        """Tear down the test methods"""
        self.resetStorage()
        pass

    def resetStorage(self):
        """Resets FileStorage data"""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test8_instantiation(self):
        """Test instantiation of the User class"""

        bs = User()
        self.assertEqual(str(type(bs)), "<class 'models.user.User'>")
        self.assertIsInstance(bs, User)
        self.assertTrue(issubclass(type(bs), BaseModel))

    def test8_attributes(self):
        """Tests the attributes of the User class"""
        attributes = storage.attributes()["User"]
        bs = User()
        for ky, v in attributes.items():
            self.assertTrue(hasattr(bs, ky))
            self.assertEqual(type(getattr(bs, ky, None)), v)


if __name__ == "__main__":
    unittest.main()
