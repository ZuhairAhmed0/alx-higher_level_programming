#!/usr/bin/python3
""" 3-to_json_string.py """
import json


def to_json_string(my_obj):
    """
    function that returns the JSON representation of an object (string)
    """

    data_json = json.dumps(my_obj)
    return (data_json)
