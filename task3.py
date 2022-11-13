from random import sample
import string
from string import ascii_letters, digits


def get_random_password(i=8) -> str:
    # TODO написать функцию генерации случайных паролей
    str = string.ascii_letters + string.digits
    return "" .join(sample(ascii_letters + digits, i))

print(get_random_password())
