from typing import Any
import itertools
from itertools import product

__all__ = (
    'cartesian_product',
)

def cartesian_product(arr1: list[Any], arr2: list[Any]) -> list:
    """
    Должна возвращать все пары элементы двух массивов:
    cartesian_product([1, 2], [3, 4]) == [(1, 3), (1, 4), (2, 3), (2, 4)]
    """
    len1 = len(arr1)
    len2 = len(arr2)
    new_arr = []
    for i in range(len1):
        for j in range(len2):
            new_elem = (arr1[i], arr2[j])
            new_arr.append(new_elem)

    return new_arr

# Второй способ
"""
def cartesian_product(arr1: list[Any], arr2: list[Any]) -> list:
    
    Должна возвращать все пары элементы двух массивов:
    cartesian_product([1, 2], [3, 4]) == [(1, 3), (1, 4), (2, 3), (2, 4)]
    
    return list(product(arr1, arr2))
"""
