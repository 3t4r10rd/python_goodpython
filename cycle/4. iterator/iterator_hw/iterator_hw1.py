# Вводится список городов в одну строчку через пробел.
# Необходимо создать итератор для этого списка и с помощью итератора
# вывести на экран в столбик первые два значения (названия городов).

i = iter(input().split())
print(next(i))
print(next(i))

# Вводится строка. Нужно создать итератор для перебора символов этой строки.
# Затем, перебрать через созданный итератор все символы до первого пробела.
# В процессе перебора символы выводить на экран в одну строчку друг за другом (без пробелов).
# Гарантируется, что во введенной строке имеется хотя бы один пробел.

i = iter(input())
flag = True
while flag:
    c = next(i)
    if c == ' ':
        flag = False
    print(c, end="")

# Вводится четырехзначное целое положительное число.
# Подумайте, как можно определить итератор для перебора его цифр.
# Выведите цифры этого введенного числа (с помощью итератора) в одну строчку через пробел.

a = int(input())
s = str(a)
it = iter(s)
for i in s:
    print(next(it), end=" ")