#!/usr/bin/env python3
"""
Defines a function Simple helper function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculates start index and an end index
    """
    nxtI = page * page_size
    return nxtI - page_size, nxtI
