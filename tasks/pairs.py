from typing import Any

__all__ = (
    'corresponding_pairs',
)


def corresponding_pairs(arr1: list[Any], arr2: list[Any]) -> list[tuple[Any, Any]]:
    """
    Функция должна возвращать соответствующие элементы двух массивов:
    corresponding_pairs([1, 2], [3, 4]) == [(1, 3), (2, 4)]
    """
    len1 = len(arr1)
    len2 = len(arr2)
    new_arr = []
    if len1 >= len2:
        for i in range(len2):
            new_elem = (arr1[i], arr2[i])
            new_arr.append(new_elem)
    elif len1 < len2:
        for i in range(len1):
            new_elem = (arr1[i], arr2[i])
            new_arr.append(new_elem)
    return new_arr

#arr1 = [1, 2, 5, 6]
#arr2 = [3, 4]
#print(corresponding_pairs(arr1, arr2))