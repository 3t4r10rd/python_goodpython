# На вход программе поступают две строки. В каждой строке записаны слова через пробел.
# Прочитайте эти строки и сохраните их в двух переменных.
#
# Объявите функцию с двумя параметрами, которой передаются строки со словами и преобразовываются в два списка из слов.
# Функция должна возвращать кортеж с этими списками в порядке: сначала первый список (первой строки), затем - второй.
#
# Определите декоратор для этой функции, который из двух списков формирует словарь, в котором ключами являются слова
# из первого списка, а значениями - соответствующие элементы из второго списка. Длины списков полагаются равными.
# Полученный словарь должен возвращаться при вызове декоратора.
#
# Примените декоратор к первой функции и вызовите ее для прочитанных строк.
# Результат (словарь d) отобразите на экране командой:
#
# print(*sorted(d.items()))


def decorator_dict(func):
    def wrapper(*args, **kwargs):
        a, b = func(*args, **kwargs)

        return {
            a[i]: b[i] for i in range(len(a))
        }

    return wrapper


@decorator_dict
def get_list(a, b):
    lst1, lst2 = a.split(), b.split()
    res = (lst1, lst2)
    print(res)
    return res


a = input()
b = input()

d = get_list(a, b)

print(*sorted(d.items()))

# print(*sorted(d.items()))