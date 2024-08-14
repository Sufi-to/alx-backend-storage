#!/usr/bin/env python3
"""Module on how to use redis as cache"""


import redis
import uuid
from typing import Any, Union


class Cache:
    """A cache class for redis"""
    def __init__(self) -> None:
        """Initializaes a redis instance."""
        self._redis = redis.Redis()
        self._redis.flushdb

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Generates a random key and store the data using that key"""
        id = str(uuid.uuid4())
        self._redis.set(id, data)
        return id
