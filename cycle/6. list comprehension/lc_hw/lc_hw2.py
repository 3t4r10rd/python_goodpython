# На вход программе подается натуральное число N. Прочитайте его и с помощью list
# comprehension сформируйте двумерный список размером N x N,  состоящий из нулей,
# а по главной диагонали - единицы. (Главная диагональ - это элементы, идущие по диагонали
# от верхнего левого угла матрицы до ее нижнего правого угла).
# Полученный двумерный список отобразите в виде таблицы чисел, как показано в примере ниже.

# 1 0 0 0
# 0 1 0 0
# 0 0 1 0
# 0 0 0 1

N = int(input())

lst = [[1 if x == i else 0 for x in range(N)] for i in range(N)]
[print(*i) for i in lst]

#ИЛИ

N = int(input())
for i in range(N):
    lst.append([1 if x == i else 0 for x in range(N)])
    print(*lst[i])