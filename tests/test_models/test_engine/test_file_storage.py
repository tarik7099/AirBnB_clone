#!/usr/bin/python3
"""Defines unittests for models/engine/file_storage.py.

"""
import os
import json
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review



class TestFileStorage_methods(unittest.TestCase):
    """Unittests for testing methods of the FileStorage class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_all_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new(self):
        baseModel = BaseModel()
        user = User()
        state = State()
        place = Place()
        city = City()
        amenity = Amenity()
        review = Review()
        models.storage.new(baseModel)
        models.storage.new(user)
        models.storage.new(state)
        models.storage.new(place)
        models.storage.new(city)
        models.storage.new(amenity)
        models.storage.new(review)
        self.assertIn(user, models.storage.all().values())
        self.assertIn("State." + state.id, models.storage.all().keys())
        self.assertIn(state, models.storage.all().values())
        self.assertIn("Place." + place.id, models.storage.all().keys())
        self.assertIn(place, models.storage.all().values())
        self.assertIn("City." + city.id, models.storage.all().keys())
        self.assertIn(city, models.storage.all().values())
        self.assertIn("Amenity." + amenity.id, models.storage.all().keys())
        self.assertIn(amenity, models.storage.all().values())
        self.assertIn("Review." + review.id, models.storage.all().keys())
        self.assertIn(review, models.storage.all().values())
        self.assertIn("BaseModel." + baseModel.id, models.storage.all().keys())
        self.assertIn(baseModel, models.storage.all().values())
        self.assertIn("User." + user.id, models.storage.all().keys())

    def test_new_args(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_new_with(self):
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_save(self):
        baseModel = BaseModel()
        user = User()
        state = State()
        place = Place()
        city = City()
        amenity = Amenity()
        review = Review()
        models.storage.new(baseModel)
        models.storage.new(user)
        models.storage.new(state)
        models.storage.new(place)
        models.storage.new(city)
        models.storage.new(amenity)
        models.storage.new(review)
        models.storage.save()
        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("Place." + place.id, save_text)
            self.assertIn("City." + city.id, save_text)
            self.assertIn("Amenity." + amenity.id, save_text)
            self.assertIn("Review." + review.id, save_text)
            self.assertIn("BaseModel." + baseModel.id, save_text)
            self.assertIn("User." + user.id, save_text)
            self.assertIn("State." + state.id, save_text)

    def test_save_with(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def tst_reload(self):
        baseModel = BaseModel()
        user = User()
        state = State()
        place = Place()
        city = City()
        amenity = Amenity()
        review = Review()
        models.storage.new(baseModel)
        models.storage.new(user)
        models.storage.new(state)
        models.storage.new(place)
        models.storage.new(city)
        models.storage.new(amenity)
        models.storage.new(review)
        models.storage.save()
        models.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("Amenity." + amenity.id, objs)
        self.assertIn("Review." + review.id, objs)
        self.assertIn("BaseModel." + baseModel.id, objs)
        self.assertIn("User." + user.id, objs)
        self.assertIn("State." + state.id, objs)
        self.assertIn("Place." + place.id, objs)
        self.assertIn("City." + city.id, objs)

    def test_reload_no(self):
        with self.assertRaises(FileNotFoundError):
            models.storage.reload()

    def test_reload_with(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()
