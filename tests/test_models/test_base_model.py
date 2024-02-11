#!/usr/bin/python3
"""The Unittest module for BaseModel Class"""

from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime
import json
import os
import re
import time
import unittest
import uuid


class TestBaseModel(unittest.TestCase):

    """Tests Cases for BaseModel class"""

    def setUp(self):
        """Sets up the test methods"""
        pass

    def tearDown(self):
        """Tears down the test methods"""
        self.resetStorage()
        pass

    def resetStorage(self):
        """Reset the FileStorage data"""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test3_instantiation(self):
        """Test the instantiation of the BaseModel class"""
        bs = BaseModel()
        expected_type = "<class 'models.base_model.BaseModel'>"
        self.assertEqual(str(type(bs)), expected_type)

        self.assertIsInstance(bs, BaseModel)
        self.assertTrue(issubclass(type(bs), BaseModel))

    def test3_init_no_args(self):
        """Test __init__ with no args."""
        self.resetStorage()
        with self.assertRaises(TypeError) as ee:
            BaseModel.__init__()
        mesg = "__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(ee.exception), mesg)

    def test3_init_many_args(self):
        """Test the __init__ with many args"""
        self.resetStorage()
        args = [ix for ix in range(1000)]
        bs = BaseModel(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        bs = BaseModel(*args)

    def test3_attributes(self):
        """Test the attributes value for instance of BaseModel class"""
        attributes = storage.attributes()["BaseModel"]
        bs = BaseModel()
        for ky, v in attributes.items():
            self.assertTrue(hasattr(bs, ky))
            self.assertEqual(type(getattr(bs, ky, None)), v)

    def test3_datetime_created(self):
        """Test updated_at & created_at if are current at the creation"""
        dt_now = datetime.now()
        bs = BaseModel()
        df = bs.updated_at - bs.created_at
        self.assertTrue(abs(df.total_seconds()) < 0.01)
        df = bs.created_at - dt_now
        self.assertTrue(abs(df.total_seconds()) < 0.1)

    def test3_id(self):
        """Tests for UUID."""
        ld = [BaseModel().id for i in range(1000)]
        self.assertEqual(len(set(ld)), len(ld))

    def test3_save(self):
        """Tests public instance method save()"""
        bs = BaseModel()
        time.sleep(0.5)
        dt_now = datetime.now()
        bs.save()
        df = bs.updated_at - dt_now
        self.assertTrue(abs(df.total_seconds()) < 0.01)

    def test3_str(self):
        """Tests for __str__ method."""
        bs = BaseModel()
        rex = re.compile(r"^\[(.*)\] \((.*)\) (.*)$")
        rs = rex.match(str(bs))
        self.assertIsNotNone(rs)
        self.assertEqual(rs.group(1), "BaseModel")
        self.assertEqual(rs.group(2), bs.id)
        s = rs.group(3)
        s = re.sub(r"(datetime\.datetime\([^)]*\))", "'\\1'", s)
        df = json.loads(s.replace("'", '"'))
        ds = bs.__dict__.copy()
        ds["created_at"] = repr(ds["created_at"])
        ds["updated_at"] = repr(ds["updated_at"])
        self.assertEqual(df, ds)

    def test3_to_dict(self):
        """Test public instance method to_dict()"""
        bs = BaseModel()
        bs.name = "Laura"
        bs.age = 23
        d = bs.to_dict()
        self.assertEqual(d["id"], bs.id)
        self.assertEqual(d["__class__"], type(bs).__name__)
        self.assertEqual(d["created_at"], bs.created_at.isoformat())
        self.assertEqual(d["updated_at"], bs.updated_at.isoformat())
        self.assertEqual(d["name"], bs.name)
        self.assertEqual(d["age"], bs.age)

    def test3_to_dict_no_args(self):
        """Test to_dict() with no args"""
        self.resetStorage()
        with self.assertRaises(TypeError) as ee:
            BaseModel.to_dict()
        mesg = "to_dict() missing 1 required positional argument: 'self'"
        self.assertEqual(str(ee.exception), mesg)

    def test3_to_dict_excess_args(self):
        """Test to_dict() with many args."""
        self.resetStorage()
        with self.assertRaises(TypeError) as ee:
            BaseModel.to_dict(self, 98)
        mesg = "to_dict() takes 1 positional argument but 2 were given"
        self.assertEqual(str(ee.exception), mesg)

    def test4_instantiation(self):
        """Test the instantiation with **kwargs"""
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()
        my_new_model = BaseModel(**my_model_json)
        self.assertEqual(my_new_model.to_dict(), my_model.to_dict())

    def test4_instantiation_dict(self):
        """Test the instantiation with **kwargs frm custom dict"""
        dct = {
            "__class__": "BaseModel",
            "updated_at": datetime(2050, 12, 30, 23, 59, 59).isoformat(),
            "created_at": datetime.now().isoformat(),
            "id": uuid.uuid4(),
            "var": "foobar",
            "int": 108,
            "float": 3.14
        }
        bs = BaseModel(**dct)
        self.assertEqual(bs.to_dict(), dct)

    def test5_save(self):
        """Test storage.save() is called frm save()"""
        self.resetStorage()
        basemodel = BaseModel()
        basemodel.save()
        key = "{}.{}".format(type(basemodel).__name__, basemodel.id)
        dct = {key: basemodel.to_dict()}

        self.assertTrue(os.path.isfile(FileStorage._FileStorage__file_path))
        with open(
            FileStorage._FileStorage__file_path, "r", encoding="utf-8"
        ) as fl:

            self.assertEqual(len(fl.read()), len(json.dumps(dct)))
            fl.seek(0)
            self.assertEqual(json.load(fl), dct)

    def test5_save_no_args(self):
        """Test save() with no args"""
        self.resetStorage()
        with self.assertRaises(TypeError) as ee:
            BaseModel.save()
        mesg = "save() missing 1 required positional argument: 'self'"
        self.assertEqual(str(ee.exception), mesg)

    def test5_save_excess_args(self):
        """Test save() with too many args"""
        self.resetStorage()
        with self.assertRaises(TypeError) as ee:
            BaseModel.save(self, 98)
        mesg = "save() takes 1 positional argument but 2 were given"
        self.assertEqual(str(ee.exception), mesg)


if __name__ == '__main__':
    unittest.main()
