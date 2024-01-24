#!/usr/bin/env python3
"""
This is our module
"""


def schools_by_topic(mongo_collection, topic):
    """
    This is a function
    """
    mylist = mongo_collection.find()
    return mylist
