#!/usr/bin/python3
"""The Unittest module for City Class"""

import unittest
from datetime import datetime
import time
from models.city import City
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class TestCity(unittest.TestCase):

    """Tests Case for the City class"""

    def setUp(self):
        """Set up the test methods"""
        pass

    def tearDown(self):
        """Tear down the test methods."""
        self.resetStorage()
        pass

    def resetStorage(self):
        """Reset the FileStorage data"""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test8_instantiation(self):
        """Test instantiation of the City class"""

        bs = City()
        self.assertEqual(str(type(bs)), "<class 'models.city.City'>")
        self.assertIsInstance(bs, City)
        self.assertTrue(issubclass(type(bs), BaseModel))

    def test8_attributes(self):
        """Test attributes of the City class"""
        attributes = storage.attributes()["City"]
        bs = City()
        for ky, v in attributes.items():
            self.assertTrue(hasattr(bs, ky))
            self.assertEqual(type(getattr(bs, ky, None)), v)

if __name__ == "__main__":
    unittest.main()
