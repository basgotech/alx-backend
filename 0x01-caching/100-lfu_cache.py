#!/usr/bin/env python3
"""Least Frequently Used caching module.
"""
from collections import OrderedDict

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFUCache class that inherits from
    BaseCaching and implements
    a LFU (Least Frequently Used) caching system.
    """
    def __init__(self):
        """Initializes the cache.
        """
        super().__init__()
        self.cache_data = OrderedDict()
        self.keys_freq = []

    def __reorder_items(self, mru_key):
        """Reorders the items in this cache based on the most
        recently used item.
        """
        max = []
        freq = 0
        mru_pos = 0
        pos_ = 0
        for x, key_gra in enumerate(self.keys_freq):
            if key_gra[0] == mru_key:
                freq = key_gra[1] + 1
                mru_pos = x
                break
            elif len(max) == 0:
                max.append(x)
            elif key_gra[1] < self.keys_freq[max[-1]][1]:
                max.append(x)
        max.reverse()
        for pos in max:
            if self.keys_freq[pos][1] > freq:
                break
            pos_ = pos
        self.keys_freq.pop(mru_pos)
        self.keys_freq.insert(pos_, [mru_key, freq])

    def put(self, key, item):
        """Adds an item in the cache.
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                lfu_key, _ = self.keys_freq[-1]
                self.cache_data.pop(lfu_key)
                self.keys_freq.pop()
                print("DISCARD:", lfu_key)
            self.cache_data[key] = item
            ins_index = len(self.keys_freq)
            for i, key_freq in enumerate(self.keys_freq):
                if key_freq[1] == 0:
                    ins_index = i
                    break
            self.keys_freq.insert(ins_index, [key, 0])
        else:
            self.cache_data[key] = item
            self.__reorder_items(key)

    def get(self, key):
        """Retrieves an item by key.
        """
        if key is not None and key in self.cache_data:
            self.__reorder_items(key)
        return self.cache_data.get(key, None)
