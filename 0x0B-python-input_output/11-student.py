#!/usr/bin/python3
"""
Module for student class.
"""
import json


class Student:

    def __init__(self, first_name, last_name, age):
        """ initialization"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieve a dictionary"""
        return self.__dict__
