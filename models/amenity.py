#!/usr/bin/env python3
"""model Amenity"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Class to create the Amenity"""

    name = ""

    def __init__(self, *args, **kwargs):
        """Comment"""
        super().__init__(self, *args, **kwargs)
