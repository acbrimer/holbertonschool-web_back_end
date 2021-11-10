#!/usr/bin/env python3
""" Module for 1-fifo_cache """
from base_caching import BaseCaching
import collections


class LRUCache(BaseCaching):
    """ LRUCache - least recently used cache"""

    def __init__(self):
        super().__init__()
        self.cache_data = collections.OrderedDict()

    def put(self, key, item):
        """ put - save item to cache """
        if (not key or not item):
            return
        if (len(self.cache_data.keys()) == self.MAX_ITEMS):
            discard = self.cache_data.popitem(last=True)
            print('DISCARD: {}'.format(discard[0]))
        if (key in self.cache_data.keys()):
            del self.cache_data[key]
        self.cache_data[key] = item

    def get(self, key):
        """ get - retrieve item from cache """
        if (key is None or key not in self.cache_data.keys()):
            return None
        val = self.cache_data[key]
        del self.cache_data[key]
        self.cache_data[key] = val
        return val
