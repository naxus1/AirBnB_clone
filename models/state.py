#!/usr/bin/env python3
"""class state"""
from models.base_model import BaseModel


class State(BaseModel):
    """class to create the State"""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
