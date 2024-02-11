#!/usr/bin/python3
"""The Unittest module for Place Class"""

import unittest
from datetime import datetime
import time
from models.place import Place
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):

    """Tests Cases for the Place class"""

    def setUp(self):
        """Set up the test methods"""
        pass

    def tearDown(self):
        """Tear down the test methods"""
        self.resetStorage()
        pass

    def resetStorage(self):
        """Reset the FileStorage data"""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test8_instantiation(self):
        """Test the instantiation of Place class"""

        bs = Place()
        self.assertEqual(str(type(bs)), "<class 'models.place.Place'>")
        self.assertIsInstance(bs, Place)
        self.assertTrue(issubclass(type(bs), BaseModel))

    def test8_attributes(self):
        """Test attributes of the Place class"""
        attributes = storage.attributes()["Place"]
        bs = Place()
        for ky, v in attributes.items():
            self.assertTrue(hasattr(bs, ky))
            self.assertEqual(type(getattr(bs, ky, None)), v)


if __name__ == "__main__":
    unittest.main()
