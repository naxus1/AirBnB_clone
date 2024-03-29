#!/usr/bin/env python3

import uuid
from datetime import datetime, date, time
from models import *


class BaseModel():
    """Class inherit other class"""
    def __str__(self):
        """String representacion object"""
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """This Function save object"""
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """This function change objest to dict"""
        self.__name__ = self.__class__.__name__
        if type(self.created_at) == datetime:
            self.created_at = self.created_at.isoformat()
        if type(self.updated_at) == datetime:
            self.updated_at = self.updated_at.isoformat()
        return self.__dict__

    def __init__(self, *args, **kwargs):
        """Constructor"""
        if len(kwargs) > 0:
            self.__dict__ = kwargs
            self.created_at = datetime.strptime(self.created_at,
                                                "%Y-%m-%dT%H:%M:%S.%f")
            self.updated_at = datetime.strptime(self.updated_at,
                                                "%Y-%m-%dT%H:%M:%S.%f")
        else:
            ct = datetime.now()
            self.id = str(uuid.uuid4())
            self.created_at = ct
            self.updated_at = ct
