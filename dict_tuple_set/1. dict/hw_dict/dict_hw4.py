# На вход программе подаются данные в формате ключ=значение, записанные через пробел.
# Необходимо прочитать строку с этими данными и на их основе сформировать словарь d.
# Затем удалить из этого словаря ключи 'False' и '3', если они существуют.
# Ключами и значениями словаря являются строки. Вывести полученный словарь на экран командой:
#
# print(*sorted(d.items()))

st = input().split()

d = dict([x.split('=') for x in st])

keys = ['3', 'False']

for i in keys:
    if i in d:
        del d[i]


print(*sorted(d.items()))


