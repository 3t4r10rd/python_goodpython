# Объявите функцию с именем get_list, одним параметром и следующим описанием в теле функции:
# '''Функция для формирования списка целых значений'''
#
# Сама функция должна формировать и возвращать список целых чисел, который передается ей на вход
# в виде строки из целых чисел, записанных через пробел.
# Определите декоратор, который выполняет суммирование значений списка, возвращаемого декорируемой
# функцией и возвращает результат. Внутри декоратора декорируйте переданную функцию
# с помощью команды @wraps (не забудьте сделать импорт: from functools import wraps).
# Такое декорирование необходимо, чтобы исходная функция get_list сохраняла свои локальные свойства: __name__ и __doc__.
# Примените декоратор к функции get_list, но не вызывайте ее.
from functools import wraps

def dec_sum(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return sum(func(*args, **kwargs))

    return wrapper



@dec_sum
def get_list(x):
    """
    Функция для формирования списка целых значений
    """

    return [int(i) for i in x.split()]