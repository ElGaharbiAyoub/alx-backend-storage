#!/usr/bin/env python3
""" Implementing an expiring web cache and tracker """
import redis
import requests
from typing import Callable
from functools import wraps


r = redis.Redis()


def count_requests(method: Callable) -> Callable:
    """ count requests decorator """
    @wraps(method)
    def wrapper(url):
        """ wrapper function """
        cached_html = r.get(f"cached:{url}")
        if cached_html:
            return cached_html.decode('utf-8')
        html = method(url)
        r.incr(f"count:{url}")
        # r.setex(f"cached:{url}", 10, html)
        r.set(f"cached:{url}", html)
        r.expire(f"cached:{url}", 10)
        return html
    return wrapper


@count_requests
def get_page(url: str) -> str:
    """ get page """
    r = requests.get(url)
    return r.text
