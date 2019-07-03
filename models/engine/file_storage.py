#!/usr/bin/env python3
import json


class FileStorage():
    """Serialization class"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Print representacion of objects"""
        return self.__objects

    def new(self, obj):
        """Create id for new object """
        if isinstance(obj, dict):
            __key = obj['__name__']+'.' + obj['id']
            self.__objects[__key] = obj
        else:
            __key = obj.__class__.__name__ + '.' + obj.id
            self.__objects[__key] = obj.to_dict()

    def save(self):
        """Serialization object """
        try:
            with open(self.__file_path, "w", encoding="utf-8") as file:
                json.dump(self.__objects, file)
        except:
            pass

    def reload(self):
        """Des Serialization object"""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                self.__objects = json.load(file)
        except:
            pass
