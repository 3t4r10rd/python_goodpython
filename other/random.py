# # Модуль random
#
# import random
#
# a = random.random() - возвращает случайные числа с плавающей точкой от 0 до 1
#
#
# random.uniform(a,b) - случайное число с плавающей точкой в диапазоне между a и b
#
#
# random.randint(a,b) - случайное ЦЕЛОЕ число от a до b
#
# a = random.randrange(a, b, c) - генерирует целые числа между a и b с шагом c
#
#
# Гауссовские случайные величины
# gauss(mu, sigma)
# mi - математическое ожидание
# sigma - среднеквадратичное отклонение
#
# a = random.gauss(0, 3.5)
#
#
#
# a = random.choice(<имя списка>) - выбор случайного элемента из списка
# a = random.shuffle(<имя_списка>) - перемешивание списка
# random.sample(<имя_списка>, x) - новый список из неповторяющихся элементов указанного списка, x - количество элементов,
# которые необходимо выбрать
#
#
# Формирование одинаковых случайных последовательностей при каждом новом запуске программы
# random.seed(<число>) - фиксирует датчик генератора случайных чисел