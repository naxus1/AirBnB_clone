#!/usr/bin/env python3

from models.base_model import BaseModel


class User(BaseModel):
    """Create users"""

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)

        email = ""
        password = ""
        first_name = ""
        last_name = ""
