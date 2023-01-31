#!/usr/bin/python3
    """
    Write a class LockedClass with no class or object attribute,
    that prevents the user from dynamically creating new instance attributes,
    """
class ckedClas:
    """
    except if the new instance attribute is called first_name
    """
    __slots__ = ['first_name']
