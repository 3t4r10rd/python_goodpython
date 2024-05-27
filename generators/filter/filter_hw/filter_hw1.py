# На вход программе подается строка с названиями городов, записанных через пробел. Необходимо прочитать
# эту строку и применить функцию filter, которая бы возвращала только названия длиной более 5 символов.
# Извлеките первые три полученных значения с помощью функции next и отобразите их на экране в одну строчку через пробел.
# (Полагается, что минимум три значения имеются).

l = "Тула Ульяновск Хабаровск Владивосток Омск Уфа"
l2 = "Воронеж Омск Тверь Москва Краснодар Владивосток"

a = filter(lambda x: len(x) > 5, l2.split())

print(*list(a)[:3])