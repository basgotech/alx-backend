#!/usr/bin/env python3

'''Task 1: FIFO caching
'''


from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    '''FIFOCache class that inherits from BaseCaching and implements
        a FIFO (First In, First Out) caching system.
    '''

    def __init__(self):
        '''
         Initialize the cache with an ordered dictionary to maintain
            the order of insertion.
        '''
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        '''Adds the item to the cache with the specified key.
        '''

        if key is None or item is None:
            return

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(last=False)
            print(f"DISCARD: {first_key}")

        self.cache_data[key] = item

    def get(self, key):
        ''' Retrieves the item from the cache with the specified key.
        '''
        return self.cache_data.get(key, None)
