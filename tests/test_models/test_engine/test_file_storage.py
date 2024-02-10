#!/usr/bin/python3
"""
Test for file storage
"""
from datetime import datetime
import unittest
from time import sleep
import json
from models.engine.file_storage import FileStorage


class tests_fileStorage(unittest.TestCase):
    """Tests the File Storage Class"""
    def tests_instances(self):
        objct = FileStorage()
        self.assertIsInstance(objct, FileStorage)

    def tests_docs(self):
        """Tests doc strings"""
        self.assertIsNotNone(FileStorage.all)
        self.assertIsNotNone(FileStorage.new)
        self.assertIsNotNone(FileStorage.save)
        self.assertIsNotNone(FileStorage.reload)

    if __name__ == '__main__':
        unittest.main()
