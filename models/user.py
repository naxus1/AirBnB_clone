#!/usr/bin/env python3
"""Class User"""
import models
from models.base_model import BaseModel


class User(BaseModel):
    """This class create users"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
