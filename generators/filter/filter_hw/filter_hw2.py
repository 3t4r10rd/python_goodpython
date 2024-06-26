# На вход программе подается список предметов в виде строк формата:
#
# название_1=вес_1
# ...
# название_N=вес_N
#
# В программе уже реализовано их считывание в список lst_in:
#
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# С помощью функции map, необходимо сначала преобразовать этот список строк в кортеж, элементами которого
# также являются кортежи, то есть, представить список в формате:
#
# (('название_1', 'вес_1'), ..., ('название_N', 'вес_N'))
#
# А, затем, отфильтровать (исключить) все предметы с весом менее 500, используя функцию filter.
# Вывести на экран список оставшихся предметов (только их названия) в одну строчку
# через пробел в порядке их следования во входных данных.

import sys
lst_in = list(map(str.strip, sys.stdin.readlines()))

l1 = tuple(map(tuple, [x.split('=') for x in lst_in]))

l2 = dict(filter(lambda x: int(x[-1]) > 500, l1))

print(*l2.keys())
