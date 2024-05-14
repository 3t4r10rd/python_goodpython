# Объявите в программе функцию с именем get_sq,
# которая имеет один параметр (принимает вещественное число).
# В теле функции значение параметра возводится в квадрат и возвращается функцией.
#
# После объявления функции прочитайте (с помощью функции input) вещественное число
# из входного потока и вызовите функцию с прочитанным значением.
# Выведите на экран число, которое возвратила функция.

def get_sq(x):
    return x ** 2


print(get_sq(float(input())))

# Объявите функцию с именем is_triangle, которая принимает три стороны треугольника
# (целые числа) и проверяет, можно ли из переданных аргументов составить треугольник.
# (Напомню, что у любого треугольника длина любой его стороны должна быть меньше суммы
# двух других). Если  проверка проходит, функция должна возвращать булево значение True,
# а иначе False.
# # Вызывать функцию не нужно, только объявить.

def is_triangle(a, b, c):
    lst = [a, b, c]
    return True if lst.pop(lst.index(max(lst))) < sum(lst) else False

# Объявите функцию с именем is_large, которая принимает строку (в качестве параметра)
# и возвращает булево значение False, если длина строки меньше трех символов, иначе True.
#
# Вызывать функцию не нужно, только объявить.

def is_large(x):
    return len(x) >= 3
