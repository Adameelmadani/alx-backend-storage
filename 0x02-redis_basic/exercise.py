#!/usr/bin/env python3
"""
This is our module
"""
import redis, uuid
from typing import Union
"""
This is redis module
This is uuid module
"""


class Cache:
    """
    This is cache class
    """
    def __init__(self):
        """
        This is the constructor function
        """
        _redis = redis.Redis()
        _redis.flushdb()
    def store(data: Union[str, bytes, int, float]) -> str:
        """
        store function
        """
        key = str(uuid.uuid4())
        _redis.set(key, data)
        return key
