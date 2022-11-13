import random
from typing import List


def get_unique_list_numbers() -> list[int]:
    list_: list[int] = [] # TODO написать функцию для получения списка уникальных целых чисел
    index = 0
    while len(list_) < 15:
        val = random.randint(-10, 10)
        index += 1
        if val not in list_:
            list_.append(val)
    print(index)
    return list_

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
