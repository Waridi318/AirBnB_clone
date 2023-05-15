#!/usr/bin/python3
'''File Storage'''
import json
from models.base_model import BaseModel


class FileStorage:
    '''serializes and deserialzes json files'''

    __file_path = 'file.json'
    __objects = {}
    class_dict = {"BaseModel": BaseModel}

    def all(self):
        '''Return dictionary of <class>.<id> : object instance'''
        return self.__objects

    def new(self, obj):
        '''Add new obj to existing dictionary of instances'''
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (__file_path)"""
        with open(self.__file_path, "w", encoding="utf-8") as f:
            dic = {k: v.to_dict() for k, v in self.__objects.items()}
            json.dump(dic, f)

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists"""
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                new_dict = json.load(f)
            for key, value in new_dict.items():
                obj = self.class_dict[value['__class__']](**value)
                self.__objects[key] = obj
        except FileNotFoundError:
            pass
