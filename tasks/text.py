from typing import Optional

__all__ = (
    'find_shortest_longest_word',
)


def find_shortest_longest_word(text: str) -> tuple[Optional[str], Optional[str]]:
    """
    В переданном тексте вернуть слово имеющее наименьшую и наибольшую длину.
    Если такого слова нет - вернуть None
    """
    word_list = text.split()
    max_lenght = 0
    max_lenght_word = ''
    min_lenght = 100
    min_lenght_word = ''
    if len(word_list) == 0:
        return (None, None)
    for i in range(len(word_list)):
        if len(word_list[i]) > max_lenght:
            max_lenght = len(word_list[i])
            max_lenght_word = word_list[i]
            print(max_lenght, max_lenght_word)
        if len(word_list[i]) < min_lenght:
            min_lenght = len(word_list[i])
            min_lenght_word = word_list[i]
    return min_lenght_word, max_lenght_word
