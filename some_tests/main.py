# #print('hello from python')
#
# def my_name(name='no name'):
#     print('Name value is', name)
#     return name.upper()
# print(my_name('Nik'))
# print(my_name())

# def person_info(name, age):
#     print(name)
#     print(age)

#person_info('nik', 30) - #позиционніе аргументі
#person_info(name='nik', age=30) #именованные аргументы

# def sum(*args):
#     total = 0
#     for arg in args:
#         total += arg
#     return total
# print(sum(5, 2, 10, 15))



# def person_info(**args):
#     print(args['city'])
#     print(args.get('country'))  # ишу чего нет но ощибки не будет будет None
#     print(type(args))
#
# person_info(name='nik', age=30, city='KR')

# def sum(a, b):
#     """Sums two numbers"""
#     return a + b
# print(sum(2, 5))


# a = 10
# b = 12
# print(a == b)
# print(a != b)
# print(a > b)
# print(a < b)
# print(a >= b)
# print(a <= b)


# a = 'abc'
# b = 0
# print(a and b)



# name = ''
# surname = 'Solo'
#
# if name:            # если это истина
#     print(name)
# elif surname:       # если if не истина а elif истина то сработает это
#     print(surname)
# else:                # если не то не то не истина то сработает else
#     print('Name and surname id empty')


# name = 'Nikita'
# drink = 'tea'
#
# print(f'{name} likes to drink {drink}') # форматирование строк (можно вставлять функции)



# # 10/0          # что бы избужать ошибку потомучто дальше код даже если он верен не будет обробатываться
# try:
#     10/0
# except ZeroDivisionError as e:
#     print(e)
#                                        # обошли ошибку деления на ноль и напечатили Continue
# print('Continue...')

# num1 = int(input("число первое: "))
# num2 = int(input("число второе: "))
# print(num1 + num2)
#

# b = 3
# for i in range(1, 11):
#     print(f'{b} * {i} = {b * i}')


# num = int(input("Введите число: "))
# while num != 0:
#     num = int(input("Введите число: "))
# print("Программа завершена.")

# for i in range(5):
#     if i == 2:
#         continue  # пропустит 2
#     print(i)

# file = open('texxt.txt', 'w')
# file.write('hello')
# file.close()

