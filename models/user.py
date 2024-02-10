#!usr/bin/python3
""" Class city that inherits Base"""


from models.base_model import BaseModel


class User(BaseModel):
    """Creates a new user"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
