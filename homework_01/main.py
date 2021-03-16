"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*args):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """

    return [i ** 2 for i in args]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def filter_numbers(numbers, key):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """

    # https://betterprogramming.pub/how-to-check-if-a-number-is-prime-in-python-9855e87cd9f8
    def is_prime(n):
        if n <= 1 or n % 1 > 0:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    if key == "odd":
        return [i for i in numbers if i % 2 != 0]
    elif key == "even":
        return [i for i in numbers if i % 2 == 0]
    elif key == "prime":
        return [i for i in numbers if is_prime(i)]
