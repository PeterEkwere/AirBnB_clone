#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
    This is a file storgae class
    Author: Peter Ekwere

"""
import sys
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
sys.path.append("..")


class FileStorage:
    """ This is the FileStorage class"""

    __file_path = "./file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary of the objects """
        return self.__objects

    def new(self, obj):
        """ This function sets the object in the dictionary with its id """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """ serializes objects to json file """
        with open(self.__file_path, mode='w', encoding="utf-8") as a:
            new_dict = {}
            for key, obj in self.__objects.items():
                new_dict[key] = obj.to_dict()
            json.dump(new_dict, a)

    def reload(self):
        """ Deserializes objects from json file """
        try:
            serialized_dict = {}
            with open(self.__file_path, mode='r', encoding="utf-8") as f:
                serialized_dict = json.load(f)
                for values in serialized_dict.values():
                    class_name = values["__class__"]
                    a_object = eval(class_name)(**values)
                    self.new(a_object)
        except FileNotFoundError:
            pass
