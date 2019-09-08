print('Hello world')
# Программа про умного попугайчика (Зачем нужны переменные?)
# Имя
name = 'Кузя'
# Возраст
age = 1
# Период, после которого он научился говорить
period = 2

print('Попугайчик')
print(name)
print('в')
print(age)
print('года')
print('научился говорить')
print('свое имя')
print(name)
print()
print('Через')
print(period)
print('года')
print('Он научился говорить')
print('Сколько ему лет')
print()
print(age + period)

# Типы переменных
person_name = 'Max'
print(type(person_name))
age = 30
print(type(age))
period = 3.3
print(type(period))
is_good = True
print(type(is_good))
person = None
print(type(person))

# Преобразование типов
birthday_year = '1988'
print(type(birthday_year))

period = 20
print(type(period))

age = int(birthday_year) + period
print(age)
some_str = birthday_year + str(period)
print(some_str)

# Ввод, вывод
# result = input()
# print('Пользователь ввел', result)
name = input('Как тебя зовут: ')
print('Привет', name)

# Арифметические и  логиеские операции
ale = 71
age = int(input('Сколько Вам лет?'))

print('Ваш возраст равен средней продолжительности жизни',ale == age)
print('Ваш возраст НЕ равен средней продолжительности жизни',ale != age)
print('Ваш возраст меньше средней продолжительности жизни',ale < age)
print('Ваш возраст больше средней продолжительности жизни',ale > age)
print('Ваш взраст меньше или равен средней продолжительности жизни',ale <= age)
print('Ваш взраст больше или равен средней продолжительности жизни',ale >= age)

print('У Вас юбилей:', age % 5 ==0)



