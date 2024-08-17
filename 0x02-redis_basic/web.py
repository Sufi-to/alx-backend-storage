#!/usr/bin/env python3
""" Redis Module """

from functools import wraps
import redis
import requests
from typing import Callable


redis_ = redis.Redis()


def count_reqs(method: Callable) -> Callable:
    """ Keeps the count of the methods """
    @wraps(method)
    def wrapper(url):
        """ Wrapper for decorator """
        redis_.incr(f"count:{url}")
        cached_page = redis_.get(f"cached:{url}")
        if cached_page:
            return cached_page.decode('utf-8')
        html = method(url)
        redis_.setex(f"cached:{url}", 10, html)
        return html
    return wrapper


@count_reqs
def get_page(url: str) -> str:
    """ Get the html content """
    return requests.get(url).text
