#!/usr/bin/python3

""" Class city that inherits Base """



from models.base_model import BaseModel


class City(BaseModel):
    """Class for City"""
    state_id = ""
    name = ""
    def __init__(self, *args, **kwargs):
        """ Constructor """
        super().__init__(self, *args, **kwargs)
