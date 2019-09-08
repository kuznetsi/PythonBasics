# print('Hello world')
# # Программа про умного попугайчика (Зачем нужны переменные?)
# # Имя
# name = 'Кузя'
# # Возраст
# age = 1
# # Период, после которого он научился говорить
# period = 2
#
# print('Попугайчик')
# print(name)
# print('в')
# print(age)
# print('года')
# print('научился говорить')
# print('свое имя')
# print(name)
# print()
# print('Через')
# print(period)
# print('года')
# print('Он научился говорить')
# print('Сколько ему лет')
# print()
# print(age + period)
#
# # Типы переменных
# person_name = 'Max'
# print(type(person_name))
# age = 30
# print(type(age))
# period = 3.3
# print(type(period))
# is_good = True
# print(type(is_good))
# person = None
# print(type(person))
#
# # Преобразование типов
# birthday_year = '1988'
# print(type(birthday_year))
#
# period = 20
# print(type(period))
#
# age = int(birthday_year) + period
# print(age)
# some_str = birthday_year + str(period)
# print(some_str)
#
# # Ввод, вывод
# # result = input()
# # print('Пользователь ввел', result)
# name = input('Как тебя зовут: ')
# print('Привет', name)
#
# # Арифметические и  логиеские операции
# ale = 71
# age = int(input('Сколько Вам лет?'))
#
# print('Ваш возраст равен средней продолжительности жизни',ale == age)
# print('Ваш возраст НЕ равен средней продолжительности жизни',ale != age)
# print('Ваш возраст меньше средней продолжительности жизни',ale < age)
# print('Ваш возраст больше средней продолжительности жизни',ale > age)
# print('Ваш взраст меньше или равен средней продолжительности жизни',ale <= age)
# print('Ваш взраст больше или равен средней продолжительности жизни',ale >= age)
#
# print('У Вас юбилей:', age % 5 == 0)
#
# # Условные операторы
# age = int(input('Введите свой возраст: '))
# if age < 18:
#     print('Доступ запрещен')
#     print('Доступ закрт')
# elif age == 18:
#     print('Вам ровно 18 лет')
#     print('Что с Вами делать?')
# elif age > 18 and age < 25:
#     print('Категория пользователей')
# else:
#     print('Доступ разрешен')
#     # Проверка не юбилей
#     if age % 5 == 0:
#         print('Поздравляем, у Вас юбилей')
# print('Какие-то действия')
#
# Понятие циклов. Цикл while
# Вывод четных чисел от 0 до n
number = 0
n = int(input('Введите n: '))

while number <= n:
    if number % 2 == 0:
        print(number)
    number += 1
