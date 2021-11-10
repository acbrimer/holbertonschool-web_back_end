#!/usr/bin/env python3
""" Module for 0-basic_cache """
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache class

        Attributes:
            cache_data: dict of cache items
    """

    def __init__(self):
        super().__init__

    def put(self, key, item):
        if (key or item is not None):
            self.cache_data[key] = item

    def get(self, key):
        if (key is None or key not in self.cache_data.keys()):
            return None
        return self.cache_data[key]
