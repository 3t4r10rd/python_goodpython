
#  (На использование цикла while). Начав тренировки, лыжник в первый день пробежал
#  10 км. Каждый следующий день он увеличивал пробег на 10 % от пробега предыдущего дня.
#  Определить в какой день он пробежит больше x км (натуральное число x вводится с клавиатуры).
#  Результат (искомый день) вывести на экран.

x = int(input())
i = 1
km = 10

while km < x:
    i += 1
    km += 0.1 * km

print(i)