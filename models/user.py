#!/usr/bin/env python3

import uuid
from datetime import datetime, date, time
from models import *
from models.base_model import BaseModel


class User(BaseModel):

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)


