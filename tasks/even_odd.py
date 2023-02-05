__all__ = (
    'even_odd',
)


def even_odd(arr: list[int]) -> float:
    """
    Функция возвращает отношение суммы четных элементов массив к сумме нечетных
    Пример:
    even_odd([1, 2, 3, 4, 5]) == 0.8889
    """
    even_numbers = 0
    odd_number = 0
    if len(arr) == 0:
        return 0
    for i in arr:
        if i % 2 == 0:
            even_numbers += i
        else:
            odd_number += i
    if odd_number == 0:
        return 0
    return even_numbers/odd_number
