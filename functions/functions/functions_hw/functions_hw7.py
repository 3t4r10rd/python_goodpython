# На вход программе подаются целые числа, записанные в одну строчку
# через пробел. Необходимо их прочитать и сохранить в списке digs.
# Затем (или в самом начале программы), объявить функцию,
# которая имеет два параметра (будут передаваться максимальное и минимальное
# значения из сформированного списка digs) и возвращающую произведение двух переданных аргументов.
#
# Вызовите эту функцию с передачей ей в качестве аргументов минимального
# и максимального числового значения из списка digs.
# Отобразите на экране значение, возвращенное функцией.
#
# Подсказка: для передачи аргументов функции используйте стандартные функции
# max и min языка Python.

def get_mult(a, b):
    return a * b


digs = list(map(int, input().split()))
print(get_mult(max(digs), min(digs)))

