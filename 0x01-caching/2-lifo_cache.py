#!/usr/bin/env python3
"""LIFO Caching.
"""
from collections import OrderedDict

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache class that inherits
       from BaseCaching and implements
       a LIFO (Last In, First Out) caching system.
    """
    def __init__(self):
        """Initialize the cache with an
           ordered dictionary to maintain
           the order of insertion.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds the item to the cache with the specified key.
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                last_key, _ = self.cache_data.popitem(True)
                print("DISCARD:", last_key)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """Retrieves the item from the cache with the specified key.
        """
        return self.cache_data.get(key, None)
