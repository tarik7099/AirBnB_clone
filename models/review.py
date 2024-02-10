#!/usr/bin/python3
""" Class review that inherits from Base"""


from models.base_model import BaseModel


class Review(BaseModel):
    """Class for Review"""
    place_id = ""
    user_id = ""
    text = ""
