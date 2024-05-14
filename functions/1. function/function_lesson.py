# Функция - объект, который выполняет заданный фрагмент программы
# Ссылка на этот объект - имя функции
#
# () - оператор вызова функции
#
# <переменная> = print - можно создать еще одну ссылку на функцию
#
# DRY - Don't repeat yourself - если какой-то код повторяется в программе - это ошибка

# создание функции
# def <имя функции> ([список аргументов]):
#     оператор 1
#     ...
#     оператор None

# текст программы должен отделяться от объявления функций двумя пустыми строками

def send_mail(from_name):
    text = f'hello от {from_name}а'
    print(text)


send_mail('Иван')

