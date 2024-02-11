#!/usr/bin/python3
"""Unittest module for Review Class"""

import unittest
from datetime import datetime
import time
from models.review import Review
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class TestReview(unittest.TestCase):

    """Tests Cases for Review Class"""

    def setUp(self):
        """Sets up the test methods"""
        pass

    def tearDown(self):
        """Tears down the test methods"""
        self.resetStorage()
        pass

    def resetStorage(self):
        """Resets the FileStorage data"""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test8_instantiation(self):
        """Tests instantiation of the Review Class"""

        bs = Review()
        self.assertEqual(str(type(bs)), "<class 'models.review.Review'>")
        self.assertIsInstance(bs, Review)
        self.assertTrue(issubclass(type(bs), BaseModel))

    def test8_attributes(self):
        """Tests attributes of the Review Class"""
        attributes = storage.attributes()["Review"]
        bs = Review()
        for ky, v in attributes.items():
            self.assertTrue(hasattr(bs, ky))
            self.assertEqual(type(getattr(bs, ky, None)), v)


if __name__ == "__main__":
    unittest.main()
