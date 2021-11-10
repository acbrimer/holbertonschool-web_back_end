#!/usr/bin/env python3
""" Module for 0-basic_cache """
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache - simple cache class inherited from BaseCaching """

    def put(self, key, item):
        """ put - save item to cache """
        if (key or item is not None):
            self.cache_data[key] = item

    def get(self, key):
        """ get - retrieve item from cache """
        if (key is None or key not in self.cache_data.keys()):
            return None
        return self.cache_data[key]
