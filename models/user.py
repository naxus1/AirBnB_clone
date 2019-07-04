#!/usr/bin/env python3
"""User module"""
from models.base_model import BaseModel


class User(BaseModel):
    """Create users
    Attributes:
        email (str): email.
        password (str): password.
        first_name (str): first name.
        last_name (str): last name.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
