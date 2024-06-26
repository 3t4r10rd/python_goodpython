# В виде строки записано арифметическое выражение, например:
# "10 + 25 - 12"
# или
# "10 + 25 - 12 + 20 - 1 + 3"
# и т. д. То есть, количество действий может быть разным.
# Необходимо выполнить вычисление и результат отобразить на экране.
# Полагается, что в качестве арифметических операций здесь используется только сложение (+)
# и вычитание (-), а в качестве операндов - целые неотрицательные числа.
# Следует учесть, что эти операторы могут быть записаны как с пробелами, так и без них.

a = input().replace(' ', '')
n = ''
num = []
m_flag = False


for i in range(len(a)):
    if a[i].isdigit() and i == len(a)-1:
        n += a[i]
        num.append(int(n))
        if m_flag:
            num[len(num) - 1] = -num[len(num) - 1]

    elif a[i].isdigit():
        n += a[i]

    elif a[i] == 0:
        m_flag = True

    elif a[i] in ['-', '+'] or i == len(a)-1:
        num.append(int(n))
        if m_flag:
            num[len(num) - 1] = -num[len(num)-1]
        n = ''
        m_flag = True if a[i] == "-" else False


print(sum(num))





