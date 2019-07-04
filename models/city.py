#!/usr/bin/env python3
"""Class City"""
from models.base_model import BaseModel


class City(BaseModel):
    """class City to crete a City object"""

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Comment"""
        super().__init__(self, *args, **kwargs)
