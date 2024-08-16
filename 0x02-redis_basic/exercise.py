#!/usr/bin/env python3
"""Module on how to use redis as cache"""


import redis
import uuid
from functools import wraps
from typing import Any, Union, Optional, Callable


def call_history(method: Callable) -> Callable:
    """Decorator to store the history of inputs and outputs for
    a particular function."""
    method_name = method.__qualname__
    ins = method_name + ":inputs"
    outs = method_name + ":outputs"

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Wrapper for decorator functionality """
        self._redis.rpush(ins, str(args))
        data = method(self, *args, **kwargs)
        self._redis.rpush(outs, str(data))
        return data

    return wrapper


def count_calls(method: Callable) -> Callable:
    """Keeps count of many times the method is called"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """A wrapper function of the store method"""
        method_name = method.__qualname__
        self._redis.incr(method_name)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    """A cache class for redis"""
    def __init__(self) -> None:
        """Initializaes a redis instance."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Generates a random key and store the data using that key"""
        id = str(uuid.uuid4())
        self._redis.set(id, data)
        return id

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """Return value if it exists in redis"""
        x = self._redis.get(key)
        if fn:
            x = fn(x)
        return x

    def get_str(self, key: str) -> str:
        """Corrects the conversion function to string"""
        res = self._redis.get(key)
        return res.decode('utf-8')

    def get_int(self, key: str) -> int:
        """Corrects the conversion function to int"""
        res = self._redis.get(key)
        try:
            value = int(res.decode('utf-8'))
        except Exception:
            res = 0
        return res
