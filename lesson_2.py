# Задание 1
li_1 = [696, 'apple', True, '74', 65.65]
print(type(li_1)) # проверка типа массива
for i in li_1: # проверка типа элементов списка
    print(type(i))

# Задание 2
a = input('Кто занял первое место? ')
b = input('Кто занял второе место? ')
c = input('Кто занял третье место? ')
d = input('Кто занял четвертое место? ')
e = input('Кто занял пятое место? ')
li_2 = [a, b, c, d, e]
print(li_2)
li_2[0], li_2[1] = li_2[1], li_2[0]
li_2[2], li_2[3] = li_2[3], li_2[2]
print(li_2)

#Задание 3
# с использованием списка
li_winter = [1, 2, 12]
li_spring = [3, 4, 5]
li_summer = [6, 7, 8]
li_autumn = [9, 10, 11]
month = int(input('Введите порядковый номер месяца '))
if month in li_winter:
    print('зима')
elif month in li_spring:
    print('весна')
elif month in li_summer:
    print('лето')
elif month in li_autumn:
    print('осень')
else:
    print('Вы ввели несуществующее значение')

# с использованием словаря
dic = {'зима': [12, 1, 2], 'весна': [3, 4, 5], 'лето': [6, 7, 8], 'осень': [9, 10, 11]}
month = int(input('Введите порядковый номер месяца '))
for elem in dic:
    if month in dic[elem]:
        print(elem)
        break
if month not in dic[elem]:
        print('Вы ввели несуществующее значение')

#Задание 4
team_members = input('Введите список членов команды через пробел без запятых: ').split(' ')
n = 0 # нумерация с помощью переменной
for el in team_members:
    print(n+1, el[0:10])
    n+=1

team_members = input('Введите список членов команды через пробел без запятых: ').split(' ')
for i, el in enumerate (team_members, 1): # нумерация с помощью функции enumerate
    print(i, el[0:10])

#Задание 5
my_list = [7, 4, 4, 3, 2]
a = int(input('Рейтинг: '))
my_list.append(a)
my_list.sort(reverse = True)
print(my_list)

#Задание 5
name_1 = input('Название ')
price_1 = input('Цена ')
weight_1 = input('Вес ')
unit_1 = input('Единица измерения ')
product_dic_1 = {'Название' : name_1, 'Цена' : price_1, 'Вес' : weight_1, 'Единица измерения' : unit_1}

name_2 = input('Название ')
price_2 = input('Цена ')
weight_2 = input('Вес ')
unit_2 = input('Единица измерения ')
product_dic_2 = {'Название' : name_2, 'Цена' : price_2, 'Вес' : weight_2, 'Единица измерения' : unit_2}

name_3 = input('Название ')
price_3 = input('Цена ')
weight_3 = input('Вес ')
unit_3 = input('Единица измерения ')
product_dic_3 = {'Название' : name_3, 'Цена' : price_3, 'Вес' : weight_3, 'Единица измерения' : unit_3}

product_1 = (1, product_dic_1)
product_2 = (2, product_dic_2)
product_3 = (3, product_dic_3)

print('Товары:', product_1, product_2, sep = '\n')

products = {'Название' : [name_1, name_2, name_3], 'Цена' : [price_1, price_2, price_3], 'Вес' : [weight_1, weight_2, weight_3], 'Единица измерения' : [unit_1, unit_2, unit_3]}
print('Товары:', products)
