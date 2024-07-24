#!/usr/bin/env python3

'''
Basic dictionary
'''


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache class that inherits from BaseCaching and implements
        basic dictionary storage with put and get methods.
    """

    def put(self, key, item):
        """ Adds the item to the cache with the key.
            If either key or item is None, nothing is added.
        """
        
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Retrieves the item from the cache with the specified key.
            If the key is None or doesn't exist, returns None.
        """
        
        return self.cache_data.get(key, None)
