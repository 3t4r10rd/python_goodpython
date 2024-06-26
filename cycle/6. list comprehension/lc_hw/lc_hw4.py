# На вход программе подается натуральное число n. Необходимо его прочитать
# и сформировать список с помощью list comprehension, состоящий из делителей числа n
# (включая и само число n). Элементы полученного списка вывести в одну строчку через пробел.
# Ликбез: делителями числа n называются целые числа, которые делят n нацело (без остатка).

n = int(input())

print(*[x for x in range(1, n+1) if n % x == 0])