#!usr/bin/python3
""" Module for Base class."""
import json


class Base:

    __nb_objects = 0

    def __init__(self, id=None):
        """initialization"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
    
    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list): list of dict respersentaion.

        Returns:
            (str): Json represantation
        """
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file.

        Args:
            cls: class
            list_objs (list): is list of instances.

        Returns:
            None
        """
        filename = cls.__name__ + ".json"
        li = []
        for i in list_objs:
            li.append(cls.to_dictionary(i))

        with open(filename, 'w') as f:
            f.write(cls.to_json_string(li))

    @staticmethod
    def from_json_string(json_string):
        """Represent json string"""
        if json_string is None:
            json_string = []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        