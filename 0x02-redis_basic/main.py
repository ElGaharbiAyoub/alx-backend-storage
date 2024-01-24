#!/usr/bin/env python3
# """
# Main file
# """
# import redis

# Cache = __import__('exercise').Cache

# cache = Cache()

# data = b"hello"
# key = cache.store(data)
# print(key)

# local_redis = redis.Redis()
# print(local_redis.get(key))

# TEST_CASES = {
#     b"foo": None,
#     123: int,
#     "bar": lambda d: d.decode("utf-8")
# }

# for value, fn in TEST_CASES.items():
#     key = cache.store(value)
#     assert cache.get(key, fn=fn) == value


# =============== task 2 - Incrementing values================



# """ Main file """

# Cache = __import__('exercise').Cache

# cache = Cache()

# cache.store(b"first")
# print(cache.get(cache.store.__qualname__))

# cache.store(b"second")
# cache.store(b"third")
# print(cache.get(cache.store.__qualname__))

# ========== task 3 - Storing lists ===========

""" Main file """

# Cache = __import__('exercise').Cache

# cache = Cache()

# s1 = cache.store("first")
# print(s1)
# s2 = cache.store("secont")
# print(s2)
# s3 = cache.store("third")
# print(s3)

# inputs = cache._redis.lrange("{}:inputs".format(cache.store.__qualname__), 0, -1)
# outputs = cache._redis.lrange("{}:outputs".format(cache.store.__qualname__), 0, -1)

# print("inputs: {}".format(inputs))
# print("outputs: {}".format(outputs))


# =====task 4 - Retrieving lists =========


# """ Main file """

# Cache = __import__('exercise').Cache
# replay = __import__('exercise').replay
# cache = Cache()
# cache.store("foo")
# cache.store("bar")
# cache.store(42)
# replay(cache.store)

# =====task 5 - Implementing an expiring web cache and tracker =========    

""" Main file """

get_page = __import__('web').get_page
# Test URLs
url1 = "http://slowwly.robertomurray.co.uk"
url2 = "http://slowwly.robertomurray.co.uk"

# Test the get_page function with slow responses
print(get_page(url1))
print(get_page(url1))
print(get_page(url2))
