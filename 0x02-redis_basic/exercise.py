#!/usr/bin/env python3
"""Exercise for Redis"""
import redis
import uuid
from typing import Union, Callable, Optional
import functools


def count_calls(method: Callable) -> Callable:
    """ count calls decorator """
    key = method.__qualname__

    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """ wrapper function """
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper

class Cache:
    """ claass for redis cache """

    def __init__(self):
        """ constructor """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ store data in redis """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """ get data from redis """
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """ get string data from redis """
        return self.get(key, str)
    
    def get_int(self, key: str) -> int:
        """ get int data from redis """
        return self.get(key, int)
