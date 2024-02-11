#!/usr/bin/python3
"""Unittest module for State Class"""

import unittest
from datetime import datetime
import time
from models.state import State
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class TestState(unittest.TestCase):

    """Tests Cases for State class"""

    def setUp(self):
        """Sets up the test methods"""
        pass

    def tearDown(self):
        """Tear down the test methods"""
        self.resetStorage()
        pass

    def resetStorage(self):
        """Resets the FileStorage data"""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test8_instantiation(self):
        """Test the instantiation of the State class"""

        bs = State()
        self.assertEqual(str(type(bs)), "<class 'models.state.State'>")
        self.assertIsInstance(bs, State)
        self.assertTrue(issubclass(type(bs), BaseModel))

    def test8_attributes(self):
        """Test the attributes of the State class"""
        attributes = storage.attributes()["State"]
        bs = State()
        for ky, v in attributes.items():
            self.assertTrue(hasattr(bs, ky))
            self.assertEqual(type(getattr(bs, ky, None)), v)


if __name__ == "__main__":
    unittest.main()
