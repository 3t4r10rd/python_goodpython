# Вводится список в виде вещественных чисел в одну строку через пробел.
# С помощью цикла for необходимо найти наименьшее значение в этом списке.
# Полученный результат вывести на экран.
# Реализовать программу без использования функции min, max и сортировки.

s = list(map(float, input().split()))
a = s[0]

for i, d in enumerate(s):
    a = d if a > s[i] else a

print(a)



