#!/usr/bin/python3
"""The Unittest module for Amenity Class"""

import unittest
from datetime import datetime
import time
from models.amenity import Amenity
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):

    """Tests Cases for Amenity class"""

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
        """Test the instantiation of the Amenity class"""

        bs = Amenity()
        self.assertEqual(str(type(bs)), "<class 'models.amenity.Amenity'>")
        self.assertIsInstance(bs, Amenity)
        self.assertTrue(issubclass(type(bs), BaseModel))

    def test_8_attributes(self):
        """Test attributes of the Amenity class"""
        attributes = storage.attributes()["Amenity"]
        bs = Amenity()
        for ky, v in attributes.items():
            self.assertTrue(hasattr(bs, ky))
            self.assertEqual(type(getattr(bs, ky, None)), v)

if __name__ == "__main__":
    unittest.main()
