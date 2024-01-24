#!/usr/bin/env python3
"""
This is our module
"""
import redis
"""
This is redis module
"""


class Cache:
    """
    This is cache class
    """
    def __init__():
        """
        This is the constructor function
        """
        _redis = redis.Redis(host = "localhost", port = "6379")
        _redis.flushdb()
