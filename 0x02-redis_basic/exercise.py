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
        self._redis = redis.Redis()
        self._redis.flushdb()
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        store function
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
