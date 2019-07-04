#!/usr/bin/env python3
from models.base_model import BaseModel


class User(BaseModel):
    """Create users"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
