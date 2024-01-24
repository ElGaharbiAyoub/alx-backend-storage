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
        cached_html = r.get("cached:{}".format(url))
        if cached_html:
            return cached_html.decode('utf-8')
        html = method(url)
        r.incr("count:{}".format(url))
        r.setex("cached:{}".format(url), 10, html)
        return html
    return wrapper


@count_requests
def get_page(url: str) -> str:
    """ get page """
    r = requests.get(url)
    return r.text
